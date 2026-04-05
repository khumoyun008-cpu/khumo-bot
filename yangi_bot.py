import os
from aiohttp import web

# Render uchun kichik veb-server (uyg'otib turish uchun)
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    # Veb-serverni sozlash
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render beradigan PORT-ni olish (8080 - zaxira)
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    print(f"Bot ishga tushdi va port {port} ochildi...")
    
    # Botingizni ishga tushirish (polling rejimida)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi!")