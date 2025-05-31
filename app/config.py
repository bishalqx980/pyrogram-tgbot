import os
from dotenv import load_dotenv
from typing import Optional

class CONFIG:
    def __init__(self):
        """Initialize with None values"""
        self.bot_token: Optional[str] = None
        self.owner_id: Optional[int] = None

        self.api_id: Optional[int] = None
        self.api_hash: Optional[str] = None


    def load_config(self, config_file) -> None:
        """
        Load configuration from .env file\n
        :param config_file: .env file path
        """
        load_dotenv(config_file)

        # ----- BOT CONFIGURATION -----
        self.bot_token = os.getenv("BOT_TOKEN")
        self.owner_id = int(os.getenv("OWNER_ID") or 0)

        # ----- MTProto CONFIGURATION -----
        self.api_id = int(os.getenv("API_ID"))
        self.api_hash = os.getenv("API_HASH")
    

    def validate(self) -> bool:
        """Check if required configurations are present"""
        required = [
            self.bot_token,
            self.api_id,
            self.api_hash
        ]

        return all(required)
