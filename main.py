# ./main.py



import asyncio
import logging

import config
import logger


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


from hydrogram import Client, filters, idle



app = Client("Telesms", api_id=config.APP_API_ID, api_hash=config.APP_API_HASH)



# LISTENERs

@app.on_message(filters.private)
async def hello(client, message):
    
    await message.reply("Hello")



# MAIN
async def main():
    await app.start()

    me = await app.get_me()
    log.info(f"Succesfully login: {me.first_name} (@{me.username})")

    await idle()
    await app.stop()



# ENTRY POINT
if __name__ == "__main__":
    logger.setup_logging()
    log = logging.getLogger()

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        log.info("Stopped by user")
