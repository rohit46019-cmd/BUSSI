from telethon import Button
from config import config

class ButtonManager:
    @staticmethod
    def main_menu():
        """Main menu buttons"""
        return [
            [
                Button.text("🔐 LOGIN", resize=True),
                Button.text("📊 DASHBOARD", resize=True)
            ],
            [
                Button.text("➕ ADD GROUP", resize=True),
                Button.text("📋 MANAGE GROUPS", resize=True)
            ],
            [
                Button.text("👁️ LIVE MONITORING", resize=True),
                Button.text("⚙️ SETTINGS", resize=True)
            ],
            [
                Button.text("❓ HELP", resize=True),
                Button.text("🚪 LOGOUT", resize=True)
            ]
        ]
    
    @staticmethod
    def login_menu():
        """Login menu buttons"""
        return [
            [
                Button.text("📱 ENTER PHONE", resize=True)
            ],
            [
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def dashboard_menu():
        """Dashboard buttons"""
        return [
            [
                Button.text("📈 STATS", resize=True),
                Button.text("🔔 ALERTS", resize=True)
            ],
            [
                Button.text("📊 GROUPS LIST", resize=True),
                Button.text("⚡ QUICK ACTIONS", resize=True)
            ],
            [
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def add_group_menu():
        """Add group menu"""
        return [
            [
                Button.text("🔍 QUICK ADD", resize=True)
            ],
            [
                Button.text("📋 PASTE USERNAME", resize=True)
            ],
            [
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def manage_groups_menu(groups, page=0):
        """Manage groups with pagination"""
        buttons = []
        
        # Calculate start and end indices
        start = page * config.ROWS_PER_PAGE
        end = start + config.ROWS_PER_PAGE
        page_groups = groups[start:end]
        
        # Add group buttons
        for group in page_groups:
            status = "🟢" if group.get("is_active", True) else "⏸️"
            button_text = f"{status} {group['username']}"
            buttons.append([Button.text(button_text, resize=True)])
        
        # Add navigation buttons
        nav_buttons = []
        if page > 0:
            nav_buttons.append(Button.text("⬅️ PREV", resize=True))
        
        nav_buttons.append(Button.text(f"📄 {page+1}", resize=True))
        
        if end < len(groups):
            nav_buttons.append(Button.text("➡️ NEXT", resize=True))
        
        if nav_buttons:
            buttons.append(nav_buttons)
        
        # Add action buttons
        buttons.append([
            Button.text("⏸️ PAUSE ALL", resize=True),
            Button.text("▶️ RESUME ALL", resize=True)
        ])
        
        buttons.append([
            Button.text("🗑️ REMOVE SELECTED", resize=True),
            Button.text("🔙 BACK", resize=True)
        ])
        
        return buttons
    
    @staticmethod
    def group_actions_menu(group_username):
        """Individual group actions"""
        return [
            [
                Button.text(f"⏸️ PAUSE {group_username}", resize=True),
                Button.text(f"▶️ RESUME {group_username}", resize=True)
            ],
            [
                Button.text(f"⚙️ SETTINGS {group_username}", resize=True),
                Button.text(f"🗑️ REMOVE {group_username}", resize=True)
            ],
            [
                Button.text("📊 STATS", resize=True),
                Button.text("👥 MEMBERS", resize=True)
            ],
            [
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def settings_menu():
        """Settings menu"""
        return [
            [
                Button.text("🔔 NOTIFICATIONS", resize=True),
                Button.text("📁 FOLDERS", resize=True)
            ],
            [
                Button.text("💾 STORAGE", resize=True),
                Button.text("🎨 APPEARANCE", resize=True)
            ],
            [
                Button.text("🔐 SECURITY", resize=True),
                Button.text("🔄 UPDATES", resize=True)
            ],
            [
                Button.text("💾 SAVE", resize=True),
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def notification_settings():
        """Notification settings"""
        return [
            [
                Button.text("✅ MESSAGES ON", resize=True),
                Button.text("✅ MEMBERS ON", resize=True)
            ],
            [
                Button.text("✅ USERNAME ON", resize=True),
                Button.text("🔕 MUTE ALL", resize=True)
            ],
            [
                Button.text("🕐 SET SCHEDULE", resize=True),
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def quick_actions_menu():
        """Quick actions menu"""
        return [
            [
                Button.text("🔄 REFRESH ALL", resize=True),
                Button.text("📥 BACKUP NOW", resize=True)
            ],
            [
                Button.text("🚫 PAUSE ALL", resize=True),
                Button.text("🧹 CLEAN LOGS", resize=True)
            ],
            [
                Button.text("📤 EXPORT DATA", resize=True),
                Button.text("🔍 SEARCH", resize=True)
            ],
            [
                Button.text("⚠️ EMERGENCY STOP", resize=True),
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def help_menu():
        """Help menu"""
        return [
            [
                Button.text("📖 USER GUIDE", resize=True),
                Button.text("🎥 VIDEO TUTORIAL", resize=True)
            ],
            [
                Button.text("❓ FAQ", resize=True),
                Button.text("🐛 REPORT BUG", resize=True)
            ],
            [
                Button.text("💡 FEATURE REQUEST", resize=True),
                Button.text("📞 CONTACT SUPPORT", resize=True)
            ],
            [
                Button.text("🔙 BACK", resize=True)
            ]
        ]
    
    @staticmethod
    def yes_no_menu():
        """Yes/No confirmation"""
        return [
            [
                Button.text("✅ YES", resize=True),
                Button.text("❌ NO", resize=True)
            ]
        ]
    
    @staticmethod
    def numeric_keypad():
        """Numeric keypad for OTP"""
        return [
            [
                Button.text("1", resize=True),
                Button.text("2", resize=True),
                Button.text("3", resize=True)
            ],
            [
                Button.text("4", resize=True),
                Button.text("5", resize=True),
                Button.text("6", resize=True)
            ],
            [
                Button.text("7", resize=True),
                Button.text("8", resize=True),
                Button.text("9", resize=True)
            ],
            [
                Button.text("0", resize=True),
                Button.text("🔙 BACK", resize=True)
            ]
        ]

buttons = ButtonManager()
