from pyrogram import Client, filters
from pyrogram.filters import Message
from pyrogram.enums import ChatType
from pyrogram.errors import BadRequest
from app import app, logger, ORIGINAL_BOT_ID, ORIGINAL_BOT_USERNAME
from app.helpers.button_maker import ButtonMaker

@app.on_message(filters.command("start", ["/", "!", "-", "."]))
async def func_start(client: Client, message: Message):
    user = message.from_user
    chat = message.chat
    bot = await client.get_me()

    if chat.type != ChatType.PRIVATE:
        btn = ButtonMaker.ubutton([{"Start me in PM": f"https://t.me/{bot.username}?start=start"}])
        await message.reply_text(f"Hey, {user.first_name}\nStart me in PM!", reply_markup=btn)
        return
    
    bot_photo = None

    try:
        async for photo in client.get_chat_photos("me"):
            bot_photo = photo.file_id
            break
    except Exception as e:
        logger.error(e)
    
    text = (
        f"Hey, {user.first_name}! I'm {bot.first_name}!\n\n"
        "I'm under development! Stay tuned for updates...\n"
        "• /help - Get bot help menu\n\n"
        "<b>• Source code:</b> <a href='https://github.com/bishalqx980/pyrogram-tgbot'>GitHub</a>\n"
        "<b>• Developer:</b> <a href='https://t.me/bishalqx680/22'>bishalqx980</a>"
    )

    if bot.id != ORIGINAL_BOT_ID:
        text += f"\n\n<blockquote>Cloned bot of @{ORIGINAL_BOT_USERNAME}</blockquote>"
    
    btn = ButtonMaker.ubutton([{"Add me to your chat": f"https://t.me/{bot.username}?startgroup=help"}])

    if bot_photo:
        try:
            await message.reply_photo(bot_photo, caption=text, reply_markup=btn)
            return
        except BadRequest:
            pass
        except Exception as e:
            logger.error(e)
    
    # if BadRequest or No Photo or Other error
    await message.reply_text(text, disable_web_page_preview=True, reply_markup=btn)
