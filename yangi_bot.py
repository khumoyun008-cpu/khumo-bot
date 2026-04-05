import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiohttp import web

# 1. @BotFather dan olgan tokeningizni mana shu yerga qo'ying:
TOKEN = "8680511025:AAFyIEMFOKsOBFbKzF-FWC3Z7lQHdYUuTR8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    
    # YouTube kanal
    builder.row(types.InlineKeyboardButton(
        text="📺 YouTube kanal", 
        url="https://www.youtube.com/channel/UCQHDnJq_WNBrOXQaaySiu3w")
    )
    
    # Telegram kanal
    builder.row(types.InlineKeyboardButton(
        text="📢 Telegram kanal", 
        url="https://t.me/khumominecraft")
    )
    
    # Admin bilan bog'lanish
    builder.row(types.InlineKeyboardButton(
        text="👨‍💻 Admin bilan bog'lanish", 
        url="https://t.me/closeone1")
    )
    
    # Sayt
    builder.row(types.InlineKeyboardButton(
        text="🌐 Rasmiy saytimiz", 
        url="https://khumoyun008-cpu.github.io/khumomcportofolio1/")
    )
    
    # Premium xizmatlar
    builder.row(types.InlineKeyboardButton(
        text="💎 Premium xizmatlar", 
        url="https://t.me/khumopremium")
    )

    await message.answer(
        f"Salom {message.from_user.full_name}! 👋\n\n"
        "**Khumo Minecraft** rasmiy botiga xush kelibsiz!\n"
        "Kerakli bo'limni tanlash uchun tugmalardan foydalaning:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

# Render uchun veb-server (Port ochiq turishi uchun)
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    port = int(os.environ.get("PORT", 8080))
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
