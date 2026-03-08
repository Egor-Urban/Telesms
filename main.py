import asyncio
import logging

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import config
import logger
from hydrogram import Client

async def main():
    app = Client(
        "Telesms", 
        api_id=config.APP_API_ID,
        api_hash=config.APP_API_HASH
    )

    async with app:
        me = await app.get_me()
        print(f"Успешный вход. Аккаунт: {me.first_name} (@{me.username})")

        await app.send_message("me", "Test")
        print("Сообщение отправлено в Избранное.")

if __name__ == "__main__":
    logger.setup_logging()
    log = logging.getLogger()
    log.info(f"Starting {config.APP_TITLE}")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Stopped by user")