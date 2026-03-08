from hydrogram import Client, filters


def output(app, log):

    def get_caption(message):
        return message.caption if message.caption else ""

    @app.on_message(filters.private)
    async def log_message(client, message):
        user = message.from_user
        username = f"@{user.username}" if user and user.username else "no_username"

        if message.text:
            log.info(f"Message from [{username}::{user.id}] ({message.id}): {message.text}")

        elif message.photo:
            log.info(f"Photo from [{username}::{user.id}] ({message.id}) caption: {get_caption(message)}")

        elif message.video:
            log.info(f"Video from [{username}::{user.id}] ({message.id}) caption: {get_caption(message)}")

        elif message.animation:  # gif
            log.info(f"GIF from [{username}::{user.id}] ({message.id}) caption: {get_caption(message)}")

        elif message.document:
            log.info(
                f"File from [{username}::{user.id}] ({message.id}): "
                f"{message.document.file_name} caption: {get_caption(message)}"
            )

        elif message.sticker:
            log.info(
                f"Sticker from [{username}::{user.id}] ({message.id}) "
                f"emoji: {message.sticker.emoji}"
            )

        else:
            log.info(f"Other message from [{username}::{user.id}] ({message.id})")


    @app.on_edited_message(filters.private)
    async def log_edited(client, message):
        user = message.from_user
        username = f"@{user.username}" if user and user.username else "no_username"

        if message.text:
            log.info(
                f"EDITED message from [{username}::{user.id}] ({message.id}): {message.text}"
            )

        elif message.photo:
            log.info(
                f"EDITED photo from [{username}::{user.id}] ({message.id}) "
                f"new caption: {get_caption(message)}"
            )

        elif message.video:
            log.info(
                f"EDITED video from [{username}::{user.id}] ({message.id}) "
                f"new caption: {get_caption(message)}"
            )

        elif message.animation:
            log.info(
                f"EDITED GIF from [{username}::{user.id}] ({message.id}) "
                f"new caption: {get_caption(message)}"
            )

        elif message.document:
            log.info(
                f"EDITED file from [{username}::{user.id}] ({message.id}) "
                f"{message.document.file_name} new caption: {get_caption(message)}"
            )

        else:
            log.info(
                f"EDITED other message from [{username}::{user.id}] ({message.id})"
            )
