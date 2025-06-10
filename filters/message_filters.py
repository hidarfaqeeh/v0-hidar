"""
فلاتر الرسائل
Message Filters
"""

from typing import Dict, Any
from telegram import Message

class MessageFilterManager:
    """مدير فلاتر الرسائل"""
    
    async def check_message(self, message: Message, filters: Dict[str, Any]) -> bool:
        """فحص الرسالة ضد الفلاتر"""
        if not filters:
            return True
        
        # فلتر نوع الرسالة
        if 'message_types' in filters:
            allowed_types = filters['message_types']
            message_type = self.get_message_type(message)
            if message_type not in allowed_types:
                return False
        
        # فلتر الكلمات المحظورة
        if 'blocked_words' in filters:
            blocked_words = filters['blocked_words']
            text = message.text or message.caption or ""
            for word in blocked_words:
                if word.lower() in text.lower():
                    return False
        
        # فلتر الكلمات المطلوبة
        if 'required_words' in filters:
            required_words = filters['required_words']
            text = message.text or message.caption or ""
            for word in required_words:
                if word.lower() not in text.lower():
                    return False
        
        # فلتر المستخدمين المحظورين
        if 'blocked_users' in filters:
            blocked_users = filters['blocked_users']
            if message.from_user and message.from_user.id in blocked_users:
                return False
        
        return True
    
    def get_message_type(self, message: Message) -> str:
        """تحديد نوع الرسالة"""
        if message.text:
            return 'text'
        elif message.photo:
            return 'photo'
        elif message.video:
            return 'video'
        elif message.document:
            return 'document'
        elif message.audio:
            return 'audio'
        elif message.voice:
            return 'voice'
        elif message.sticker:
            return 'sticker'
        elif message.location:
            return 'location'
        elif message.contact:
            return 'contact'
        else:
            return 'other'
