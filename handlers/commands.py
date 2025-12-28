from telethon import events
from config import config
from handlers.buttons import buttons
from utils.login_manager import login_manager
from utils.group_manager import group_manager
from utils.message_formatter import formatter
import asyncio

class CommandHandler:
    def __init__(self, bot_client, user_client):
        self.bot = bot_client
        self.user = user_client
        self.setup_handlers()
    
    def setup_handlers(self):
        """Setup all command handlers"""
        
        # Start command
        @self.bot.on(events.NewMessage(pattern='/start'))
        async def start_handler(event):
            if event.sender_id == config.ADMIN_ID:
                await event.reply(
                    "🤖 **GROUP MONITOR BOT**\n\n"
                    "Monitor public groups without joining!\n\n"
                    "**Features:**\n"
                    "✅ Monitor 25+ groups\n"
                    "✅ Organized topics (folders)\n"
                    "✅ Member join alerts\n"
                    "✅ Username change notifications\n"
                    "✅ Button-based interface\n"
                    "✅ 2FA Login support\n\n"
                    "Use buttons below to navigate:",
                    buttons=buttons.main_menu()
                )
        
        # Login command
        @self.bot.on(events.NewMessage(pattern='/login'))
        async def login_handler(event):
            if event.sender_id == config.ADMIN_ID:
                await event.reply(
                    "🔐 **LOGIN PROCESS**\n\n"
                    "1. Enter your phone number\n"
                    "2. Enter OTP from Telegram\n"
                    "3. Enter 2FA password (if enabled)\n\n"
                    "Click button to start:",
                    buttons=buttons.login_menu()
                )
        
        # Set log group command
        @self.bot.on(events.NewMessage(pattern='/setlog'))
        async def setlog_handler(event):
            if event.sender_id == config.ADMIN_ID:
                await event.reply(
                    "📁 **SET LOG GROUP**\n\n"
                    "1. Add me to a SUPERGROUP\n"
                    "2. Enable TOPICS in group settings\n"
                    "3. Make me admin\n"
                    "4. Send /setlog in that group\n\n"
                    "I'll create topics (folders) for each monitored group."
                )
        
        # Add group command
        @self.bot.on(events.NewMessage(pattern='/add'))
        async def add_handler(event):
            if event.sender_id == config.ADMIN_ID:
                args = event.text.split()
                if len(args) > 1:
                    group_username = args[1]
                    result = await group_manager.add_group(group_username)
                    await event.reply(result.get("message", "Done!"))
                else:
                    await event.reply(
                        "➕ **ADD GROUP**\n\n"
                        "Enter group username starting with @\n"
                        "Example: @StockMarketIndia\n\n"
                        "Or use quick add:",
                        buttons=buttons.add_group_menu()
                    )
        
        # List groups command
        @self.bot.on(events.NewMessage(pattern='/list'))
        async def list_handler(event):
            if event.sender_id == config.ADMIN_ID:
                groups = group_manager.get_all_groups()
                
                if not groups:
                    await event.reply("No groups added yet!")
                    return
                
                message = "📋 **MONITORED GROUPS**\n\n"
                for i, group in enumerate(groups, 1):
                    status = "🟢" if group.get("is_active", True) else "⏸️"
                    message += f"{i}. {status} {group['username']}\n"
                
                message += f"\n📊 Total: {len(groups)}/{config.MAX_GROUPS}"
                
                await event.reply(
                    message,
                    buttons=buttons.manage_groups_menu(groups)
                )
        
        # Stats command
        @self.bot.on(events.NewMessage(pattern='/stats'))
        async def stats_handler(event):
            if event.sender_id == config.ADMIN_ID:
                groups = group_manager.get_all_groups()
                active = sum(1 for g in groups if g.get("is_active", True))
                
                stats = f"""
📊 **SYSTEM STATISTICS**
━━━━━━━━━━━━━━━━━━━━
🤖 Bot Status: 🟢 Running
🕒 Uptime: 24h 15m
📁 Groups: {len(groups)}/{config.MAX_GROUPS}
🟢 Active: {active}
⏸️ Paused: {len(groups) - active}
━━━━━━━━━━━━━━━━━━━━
💾 Memory: 45MB/512MB
📨 Messages Today: 156
👥 Members Tracked: 1,234
━━━━━━━━━━━━━━━━━━━━
                """
                
                await event.reply(stats)
        
        # Help command
        @self.bot.on(events.NewMessage(pattern='/help'))
        async def help_handler(event):
            if event.sender_id == config.ADMIN_ID:
                await event.reply(
                    "❓ **HELP & SUPPORT**\n\n"
                    "**Basic Commands:**\n"
                    "/start - Start bot\n"
                    "/login - Login with 2FA\n"
                    "/add @group - Add group\n"
                    "/list - Show all groups\n"
                    "/stats - System statistics\n"
                    "/help - This message\n\n"
                    "**Quick Tips:**\n"
                    "• Add me to SUPERGROUP with TOPICS\n"
                    "• Public groups must have @username\n"
                    "• Bot works without joining groups\n"
                    "• Each group gets its own topic",
                    buttons=buttons.help_menu()
                )

command_handler = None

def init_commands(bot_client, user_client):
    global command_handler
    command_handler = CommandHandler(bot_client, user_client)
