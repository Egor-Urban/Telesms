from hydrogram import Client, filters



def output(app, log):
    @app.on_message(filters.private)
    async def log_message(client, message):
        user = message.from_user
        username = f"@{user.username}" if user and user.username else "no_username"

        if message.text:
            log.info(f"Message from [{username}::{user.id}]: {message.text}")

        elif message.photo:
            log.info(f"Photo from [{username}::{user.id}]")

        elif message.video:
            log.info(f"Video from [{username}::{user.id}]")

        elif message.document:
            log.info(f"File from [{username}::{user.id}]: {message.document.file_name}")

        else:
            log.info(f"Other message from [{username}::{user.id}]")


    @app.on_edited_message(filters.private)
    async def log_edited(client, message):
        user = message.from_user
        username = f"@{user.username}" if user and user.username else "no_username"

        if message.text:
            log.info(f"EDITED message from [{username}::{user.id}]: {message.text}")

        elif message.photo:
            log.info(f"EDITED photo from [{username}::{user.id}]")

        elif message.video:
            log.info(f"EDITED video from [{username}::{user.id}]")

        elif message.document:
            log.info(f"EDITED file from [{username}::{user.id}]: {message.document.file_name}")

        else:
            log.info(f"EDITED other message from [{username}::{user.id}]")
