import asyncio

def _input(app, loop, log):
    while True:
        username, msg = input().split(maxsplit=1)
        asyncio.run_coroutine_threadsafe(
            app.send_message(username, msg),
            loop
        )

        log.info(f"Sent message to [{username}]: {msg}")

        
