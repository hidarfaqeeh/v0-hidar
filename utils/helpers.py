"""
مساعدات ووظائف مفيدة
Helper Functions and Utilities
"""

import re
import html
from datetime import datetime, time
from typing import Dict, Any, Optional

class TextProcessor:
    """معالج النصوص"""
    
    @staticmethod
    def clean_text(text: str, settings: Dict[str, Any]) -> str:
        """تنظيف النص"""
        if not text:
            return ""
        
        # إزالة الروابط إذا كان مطلوباً
        if settings.get('remove_links', False):
            text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$$\$$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        
        # إزالة المنشن إذا كان مطلوباً
        if settings.get('remove_mentions', False):
            text = re.sub(r'@\w+', '', text)
        
        # إزالة الهاشتاغ إذا كان مطلوباً
        if settings.get('remove_hashtags', False):
            text = re.sub(r'#\w+', '', text)
        
        # تنظيف المسافات الزائدة
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    @staticmethod
    def add_header_footer(text: str, header: Optional[str], footer: Optional[str]) -> str:
        """إضافة رأس وتذييل للنص"""
        result = text
        
        if header:
            result = f"{header}\n\n{result}"
        
        if footer:
            result = f"{result}\n\n{footer}"
        
        return result
    
    @staticmethod
    def limit_text_length(text: str, max_length: int) -> str:
        """تحديد طول النص"""
        if len(text) <= max_length:
            return text
        
        return text[:max_length-3] + "..."

class TimeHelper:
    """مساعد الوقت"""
    
    @staticmethod
    def is_working_hours(working_hours: Dict[str, Any]) -> bool:
        """فحص ساعات العمل"""
        if not working_hours.get('enabled', False):
            return True
        
        now = datetime.now().time()
        start_time = time.fromisoformat(working_hours.get('start', '00:00'))
        end_time = time.fromisoformat(working_hours.get('end', '23:59'))
        
        if start_time <= end_time:
            return start_time <= now <= end_time
        else:
            # العمل عبر منتصف الليل
            return now >= start_time or now <= end_time
