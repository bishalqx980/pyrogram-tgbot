import os
import shutil
from time import time
from pyrogram import Client, __version__ as pyro_version
from .logger import setup_logging
from .config import CONFIG

# constants
__version__ = "0.0.0.2-alpha" # major.minor.patch.commits
CONFIG_FILE = "config.env"
REQUIRED_DIRS = ["sys"]
ORIGINAL_BOT_USERNAME = "MissCiri_bot"
ORIGINAL_BOT_ID = 6845693976
BOT_UPTIME = time()

# Creating Required Folder/Directories
try:
    for dir_name in REQUIRED_DIRS:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.makedirs(dir_name, exist_ok=True)
except Exception as e:
    print(e)
    exit()

# logger & .env config file
logger = setup_logging() # need to execute after creating Required folders
config = CONFIG()
config.load_config(CONFIG_FILE)

if not config.validate():
    raise ValueError("Missing required configuration.")

# Main Client function
app = Client(
    name="pyrogram-tgbot",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token,
    in_memory=True
)

logger.info(f"""
Developed by
 ______     __     ______     __  __     ______     __        
/\  == \   /\ \   /\  ___\   /\ \_\ \   /\  __ \   /\ \       
\ \  __<   \ \ \  \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  
 \ \_____\  \ \_\  \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/ 
   
    Version: {__version__}
    Library: pyrogram {pyro_version}
    GitHub: https://github.com/bishalqx980
""")
