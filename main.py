# ./main.py



import asyncio
import logging
import threading

import config
import logger


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
from hydrogram import Client, idle

from Telegram.output_handler import output
from Telegram.input_handler import _input



app = Client("Telesms", api_id=config.APP_API_ID, api_hash=config.APP_API_HASH)


# MAIN
async def main():
    await app.start()

    me = await app.get_me()
    log.info(f"Succesfully login: {me.first_name} (@{me.username})")

    output(app, log)

    input_thread = threading.Thread(target=_input, args=(app, loop, log))
    input_thread.start()


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
