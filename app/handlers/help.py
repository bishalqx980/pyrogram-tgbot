from pyrogram import Client, filters
from pyrogram.filters import Message
from pyrogram.enums import ChatType
from pyrogram.errors import BadRequest
from app import app, logger, ORIGINAL_BOT_ID, ORIGINAL_BOT_USERNAME
from app.helpers.button_maker import ButtonMaker

class HelpMenuData:
    TEXT = (
        "<blockquote><b>Help Menu</b></blockquote>\n\n"
        "Hey! Welcome to the bot help section.\n"
        "I'm a Telegram bot that manages groups and handles various tasks effortlessly.\n\n"
        "• /start - Start the bot\n"
        "• /help - To see this message"
    )

    BUTTONS = [
        {"Group Management": "help_menu_gm1", "AI/Info": "help_menu_ai_knowledge"},
        {"Misc": "help_menu_misc", "Owner/Sudo": "help_menu_owner"},
        {"» bot.info()": "help_menu_botinfo", "Close": "help_menu_close"}
    ]

@app.on_message(filters.command("help", ["/", "!", "-", "."]))
async def func_help(client: Client, message: Message):
    user = message.from_user
    chat = message.chat
    bot = await client.get_me()

    if chat.type != ChatType.PRIVATE:
        btn = ButtonMaker.ubutton([{"Start me in PM": f"https://t.me/{bot.username}?start=help"}])
        await message.reply_text(f"Hey, {user.first_name}\nContact me in PM for help!", reply_markup=btn)
        return
    
    bot_photo = None

    try:
        async for photo in client.get_chat_photos("me"):
            bot_photo = photo.file_id
            break
    except Exception as e:
        logger.error(e)
    

    btn = ButtonMaker.cbutton(HelpMenuData.BUTTONS)
    
    if bot_photo:
        try:
            await message.reply_photo(bot_photo, caption=HelpMenuData.TEXT, reply_markup=btn)
            return
        except BadRequest:
            pass
        except Exception as e:
            logger.error(e)
    
    # if BadRequest or No Photo or Other error
    await message.reply_text(HelpMenuData.TEXT, disable_web_page_preview=True, reply_markup=btn)
