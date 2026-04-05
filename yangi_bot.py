import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# 1. Bot Tokeningizni bu yerga qo'ying
TOKEN = "BU_YERGA_TOKENINGIZNI_YOZING"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Oddiy /start buyrug'i
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Bot Render-da muvaffaqiyatli ishlayapti.")

# Render o'chib qolmasligi uchun kichik veb-server
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    # Render beradigan PORT-ni olish (8080 - zaxira)
    port = int(os.environ.get("PORT", 8080))
    
    # Veb-serverni sozlash
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    print(f"Bot ishga tushdi va {port}-port ochildi...")

    # Botni polling rejimida ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi!")
