# ./main.py



import asyncio
import logging

import config
import logger

from hydrogram import Client



async def main():
    app = Client("Telesms", api_id=config.APP_API_ID, api_hash=config.APP_API_HASH)

    async with app:
        me = await app.get_me()
        log.info(f"Succesfully login: {me.first_name} (@{me.username})")

        await app.send_message("me", "[Telesms] Userbot started")
        log.info("Test init msg sent")

if __name__ == "__main__":
    logger.setup_logging()
    log = logging.getLogger()
    log.info(f"Starting {config.APP_TITLE}")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Stopped by user")