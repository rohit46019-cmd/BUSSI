📱 Usage Guide
Step 1: Login
Start bot: /start

Click "🔐 LOGIN"

Enter phone number (with +91)

Enter OTP from Telegram

Enter 2FA password (if enabled)

Step 2: Setup Log Group
Create a SUPERGROUP

Enable TOPICS in group settings

Add bot as admin

Send /setlog in that group

Step 3: Add Groups
Click "➕ ADD GROUP"

Enter group username: @groupname

Bot creates topic for that group

Step 4: Monitor
Messages auto-forward to topics

Member joins notified

Username changes alerted

🎮 Button Interface
Main Menu:
🔐 LOGIN - Login with 2FA

📊 DASHBOARD - System overview

➕ ADD GROUP - Add new group

📋 MANAGE GROUPS - View/remove groups

👁️ LIVE MONITORING - Real-time status

⚙️ SETTINGS - Configure bot

❓ HELP - Documentation

🚪 LOGOUT - Logout session

Group Management:
⏸️ PAUSE - Pause monitoring

▶️ RESUME - Resume monitoring

⚙️ SETTINGS - Group settings

🗑️ REMOVE - Remove group

📊 STATS - Group statistics

👥 MEMBERS - View members

🛠️ Commands
Command	Description
/start	Start the bot
/login	Login with phone + 2FA
/setlog	Set log group
/add @group	Add group to monitor
/remove @group	Remove group
/list	Show all groups
/stats	System statistics
/help	Show help
☁️ Deployment on Render
1. Push to GitHub
bash
git add .
git commit -m "Initial commit"
git push origin main
2. Deploy on Render
Go to https://render.com

New Web Service

Connect GitHub repo

Configure:

Name: group-monitor-bot

Environment: Python

Build Command: pip install -r requirements.txt

Start Command: python main.py

Add environment variables

Deploy!

⚙️ Environment Variables
Variable	Description	Required
API_ID	Telegram API ID	✅
API_HASH	Telegram API Hash	✅
BOT_TOKEN	Bot token from @BotFather	✅
ADMIN_ID	Your Telegram ID	✅
MONGO_URI	MongoDB connection string	❌
LOG_GROUP_ID	Log group ID (auto-set)	❌
📁 Folder Structure
text
group-monitor-bot/
├── config/          # Configuration
├── handlers/        # Command & button handlers
├── database/        # MongoDB connection
├── utils/          # Utility functions
├── sessions/       # Telegram sessions
├── main.py         # Entry point
├── requirements.txt # Dependencies
└── README.md       # This file
🔧 Troubleshooting
Bot not responding?
Check if bot is running: ps aux | grep python

Check logs on Render dashboard

Verify environment variables

Can't login?
Ensure phone number format: +919876543210

Check OTP is from Telegram

2FA password correct

Groups not monitoring?
Groups must be public with @username

Bot needs proper login session

Check topic creation in log group

📞 Support
Report issues: GitHub Issues

Feature requests: GitHub Discussions

Contact: Your Telegram

📄 License
MIT License - Free to use and modify

🚀 Advanced Features (Future)
AI message filtering

Sentiment analysis

User behavior tracking

Scheduled reports

Multiple users support

Web dashboard

API access

🙏 Credits
Developed with ❤️ using:

Telethon - Telegram client library

Pyrogram - MTProto framework

MongoDB - Database

Render - Cloud hosting

text

## 🚀 **DEPLOYMENT STEPS:**

### **Step 1: Setup Locally**
```bash
# 1. Clone or create project
mkdir group-monitor-bot
cd group-monitor-bot

# 2. Create all files from above
# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your credentials

# 5. Run bot
python main.py
Step 2: Deploy to Render
bash
# 1. Initialize git
git init
git add .
git commit -m "Initial commit"

# 2. Create GitHub repository
# 3. Push to GitHub
git remote add origin https://github.com/yourusername/group-monitor-bot.git
git branch -M main
git push -u origin main

# 4. Go to render.com
# 5. Click "New Web Service"
# 6. Connect GitHub repository
# 7. Configure as shown above
# 8. Add environment variables
# 9. Deploy!
Step 3: Keep Bot Alive
Since Render free tier sleeps after 15 mins:

Go to https://uptimerobot.com

Create free account

Add monitor for your Render URL

Set interval: 5 minutes

Bot will stay awake!

🎯 BOT USAGE FLOW:
First Time Setup:
/start - Show main menu

🔐 LOGIN - Start login process

Enter phone → OTP → 2FA password

⚙️ SETTINGS → /setlog - Set log group

➕ ADD GROUP - Add first group

Bot creates topic and starts monitoring

Daily Use:
Open Telegram

Message your bot

Use buttons to manage

Check log group for updates

Add/remove groups as needed

⚡ QUICK START SCRIPT:
Create setup.sh:

bash
#!/bin/bash
echo "🚀 Setting up Group Monitor Bot..."

# Install dependencies
pip install -r requirements.txt

# Create .env if not exists
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Please edit .env file with your credentials"
    echo "Required: API_ID, API_HASH, BOT_TOKEN, ADMIN_ID"
fi

# Create sessions directory
mkdir -p sessions

echo "✅ Setup complete!"
echo "👉 Run: python main.py"
🎉 YOUR BOT IS READY!
What you get:
✅ Complete button-based interface
✅ 2FA login support
✅ Topic/folder organization
✅ 25 groups monitoring
✅ Free hosting on Render
✅ No coding required to use

Next Steps:
Fill .env with your credentials

Run python main.py

Login with phone/OTP/2FA

Set log group

Start adding groups!

Bot chalane ke liye ready hain?
