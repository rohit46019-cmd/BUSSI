import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API Credentials
    API_ID = int(os.getenv("API_ID", 0))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
    
    # MongoDB (Optional - for session storage)
    MONGO_URI = os.getenv("MONGO_URI", "")
    
    # Log Group (Set via command)
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))
    
    # Bot Settings
    MAX_GROUPS = 25
    SESSION_NAME = "group_monitor"
    
    # Button Settings
    ROWS_PER_PAGE = 5
    
config = Config()
