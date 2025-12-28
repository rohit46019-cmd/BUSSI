from datetime import datetime

class MessageFormatter:
    @staticmethod
    def format_message(message_type, data):
        """Format different types of messages"""
        templates = {
            "new_message": """
📨 **New Message**
━━━━━━━━━━━━━━━━━━━━
📌 **Group:** {group_title}
🔗 **Username:** {group_username}
👤 **From:** {sender_id}
⏰ **Time:** {time}
━━━━━━━━━━━━━━━━━━━━
💬 {message}
            """,
            
            "member_joined": """
👤 **New Member Joined**
━━━━━━━━━━━━━━━━━━━━
📌 **Group:** {group_title}
🔗 **Username:** {group_username}
🆔 **User ID:** {user_id}
👤 **Username:** {username}
⏰ **Time:** {time}
━━━━━━━━━━━━━━━━━━━━
🔗 **Profile:** [Click Here](tg://user?id={user_id})
            """,
            
            "username_changed": """
⚠️ **Username Changed**
━━━━━━━━━━━━━━━━━━━━
📌 **Group:** {old_title}
🔄 **Old:** {old_username}
🔄 **New:** {new_username}
⏰ **Time:** {time}
━━━━━━━━━━━━━━━━━━━━
✅ Bot will now monitor: {new_username}
            """,
            
            "group_added": """
✅ **Group Added for Monitoring**
━━━━━━━━━━━━━━━━━━━━
📌 **Group:** {group_title}
🔗 **Username:** {group_username}
👥 **Members:** {members_count}
📅 **Added:** {time}
━━━━━━━━━━━━━━━━━━━━
📁 **Topic Created:** Yes
👁️ **Monitoring:** Active
            """
        }
        
        template = templates.get(message_type, "{message}")
        data["time"] = datetime.now().strftime("%H:%M:%S")
        return template.format(**data)

formatter = MessageFormatter()
