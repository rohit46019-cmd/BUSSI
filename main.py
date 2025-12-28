import asyncio
import os
from telethon import TelegramClient
from flask import Flask
from threading import Thread
from config import config
from database.mongo import db
from handlers.commands import init_commands
from handlers.callbacks import init_callbacks
from utils.group_manager import group_manager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app for keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Group Monitor Bot is running!"

@app.route('/ping')
def ping():
    return "pong"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

class GroupMonitorBot:
    def __init__(self):
        self.bot_client = None
        self.user_client = None
        
    async def init_clients(self):
        """Initialize Telegram clients"""
        try:
            # Bot client
            self.bot_client = TelegramClient(
                'sessions/bot_session',
                config.API_ID,
                config.API_HASH
            ).start(bot_token=config.BOT_TOKEN)
            
            logger.info("🤖 Bot client started")
            
            # User client (from stored session)
            session_string = db.get_user_session(config.ADMIN_ID)
            
            if session_string:
                self.user_client = TelegramClient(
                    'sessions/user_session',
                    config.API_ID,
                    config.API_HASH
                )
                
                # Load session from string
                await self.user_client.start(
                    session_string=session_string
                )
                
                logger.info("👤 User client started (from session)")
            else:
                logger.info("👤 User client not logged in yet")
                self.user_client = None
            
            # Set clients in group manager
            if self.user_client:
                await group_manager.set_clients(
                    self.user_client, 
                    self.bot_client
                )
            
            # Initialize handlers
            if self.user_client:
                init_commands(self.bot_client, self.user_client)
                init_callbacks(self.bot_client, self.user_client)
            else:
                init_commands(self.bot_client, None)
                init_callbacks(self.bot_client, None)
            
            return True
            
        except Exception as e:
            logger.error(f"Client init error: {e}")
            return False
    
    async def run(self):
        """Run the bot"""
        # Start Flask in separate thread
        flask_thread = Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()
        
        logger.info("🚀 Starting Group Monitor Bot...")
        
        # Initialize clients
        if not await self.init_clients():
            logger.error("Failed to initialize clients")
            return
        
        # Send startup message to admin
        try:
            await self.bot_client.send_message(
                config.ADMIN_ID,
                "🤖 **Group Monitor Bot Started!**\n\n"
                f"🕒 Time: {asyncio.get_event_loop().time()}\n"
                f"📁 Groups: 0/{config.MAX_GROUPS}\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "Use /start to begin"
            )
        except:
            pass
        
        logger.info("✅ Bot is now running!")
        
        # Keep running
        await self.bot_client.run_until_disconnected()

async def main():
    bot = GroupMonitorBot()
    await bot.run()

if __name__ == "__main__":
    # Create sessions directory
    os.makedirs("sessions", exist_ok=True)
    
    # Run the bot
    asyncio.run(main())
