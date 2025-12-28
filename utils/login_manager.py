from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from config import config
from database.mongo import db
import asyncio

class LoginManager:
    def __init__(self):
        self.client = None
        self.login_states = {}
        
    async def start_login(self, user_id, phone):
        """Start login process"""
        self.login_states[user_id] = {
            "phone": phone,
            "stage": "otp",
            "client": TelegramClient(f"sessions/{user_id}", config.API_ID, config.API_HASH)
        }
        
        client = self.login_states[user_id]["client"]
        await client.connect()
        
        try:
            sent_code = await client.send_code_request(phone)
            return {"success": True, "phone_code_hash": sent_code.phone_code_hash}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def verify_otp(self, user_id, code, phone_code_hash):
        """Verify OTP"""
        if user_id not in self.login_states:
            return {"success": False, "error": "Session expired"}
        
        client = self.login_states[user_id]["client"]
        
        try:
            await client.sign_in(phone=self.login_states[user_id]["phone"], 
                                code=code, 
                                phone_code_hash=phone_code_hash)
            
            # Get session string
            session_string = await client.session.save()
            
            # Save to database
            db.save_user_session(user_id, session_string)
            
            # Update stage
            self.login_states[user_id]["stage"] = "logged_in"
            
            return {"success": True, "message": "Login successful!"}
            
        except SessionPasswordNeededError:
            self.login_states[user_id]["stage"] = "2fa"
            return {"success": False, "require_2fa": True}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def verify_2fa(self, user_id, password):
        """Verify 2FA password"""
        if user_id not in self.login_states:
            return {"success": False, "error": "Session expired"}
        
        client = self.login_states[user_id]["client"]
        
        try:
            await client.sign_in(password=password)
            
            # Get session string
            session_string = await client.session.save()
            
            # Save to database
            db.save_user_session(user_id, session_string)
            
            # Cleanup
            del self.login_states[user_id]
            
            return {"success": True, "message": "2FA verified! Login successful!"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}

login_manager = LoginManager()
