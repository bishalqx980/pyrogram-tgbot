import asyncio
from pyrogram import idle
from pyrogram.errors import FloodWait
from app import app, logger, config
from app.handlers import *

async def app_init():
    try:
        await app.send_message(config.owner_id, "Bot Started!")
        logger.info("Bot Started!")
    except Exception as e:
        logger.error(e)
    
    await idle()


async def main():
    try:
        await app.start()
        await app_init()
    except FloodWait as e:
        logger.info(f"FloodWait: {e}")
        await asyncio.sleep(e.value)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    app.run(main())
