import asyncio
import logging
from aiogram import Bot, Dispatcher
import settings.config as cfg


async def main():
    from routers import router as main_router
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=cfg.TELEGRAM_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
