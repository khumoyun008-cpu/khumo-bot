import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

# --- SOZLAMALAR ---
TOKEN = "8680511025:AAFyIEMFOKsOBFbKzF-FWC3Z7lQHdYUuTR8"
CHANNEL_ID = "@khumominecraft"  # Majburiy obuna uchun kanal
ADMIN_LINK = "https://t.me/closeone1"
CHANNEL_LINK = "https://t.me/khumominecraft"
PREMIUM_LINK = "https://t.me/khumopremium"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Obunani tekshirish funksiyasi
async def check_sub(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
        return False
    except Exception:
        return False

@dp.message()
async def start_cmd(message: types.Message):
    if message.text == "/start":
        user_id = message.from_user.id
        is_subscribed = await check_sub(user_id)
        
        if is_subscribed:
            # ASOSIY MENYU
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📢 Kanallar", url=CHANNEL_LINK)],
                [InlineKeyboardButton(text="👨‍💻 Admin bilan bog'lanish", url=ADMIN_LINK)],
                [InlineKeyboardButton(text="⭐ Premium xaridlar", callback_data="premium_info")]
            ])
            await message.answer(
                f"Salom {message.from_user.first_name}!\nKerakli bo'limni tanlang:", 
                reply_markup=keyboard
            )
        else:
            # OBUNA BO'LISH XABARI
            btn = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Obuna bo'lish ➕", url=CHANNEL_LINK)],
                [InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_sub")]
            ])
            await message.answer(
                "⚠️ Botdan foydalanish uchun kanalimizga obuna bo'lishingiz kerak!", 
                reply_markup=btn
            )

@dp.callback_query(F.data == "check_sub")
async def check_callback(callback: types.CallbackQuery):
    if await check_sub(callback.from_user.id):
        await callback.message.delete()
        await callback.message.answer("Tabriklaymiz! Obuna tasdiqlandi. /start bosing.")
    else:
        await callback.answer("❌ Hali obuna bo'lmadingiz!", show_alert=True)

@dp.callback_query(F.data == "premium_info")
async def premium_info(callback: types.CallbackQuery):
    premium_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 Premium Kanal", url=PREMIUM_LINK)],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main")]
    ])
    await callback.message.edit_text(
        "⭐ Premium bo'limiga xush kelibsiz!", 
        reply_markup=premium_kb
    )

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Kanallar", url=CHANNEL_LINK)],
        [InlineKeyboardButton(text="👨+💻 Admin bilan bog'lanish", url=ADMIN_LINK)],
        [InlineKeyboardButton(text="⭐ Premium xaridlar", callback_data="premium_info")]
    ])
    await callback.message.edit_text("Asosiy menyu:", reply_markup=keyboard)

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())