"""
إعداد الويب هوك للبوت
Setup webhook for the bot
"""

from http.server import BaseHTTPRequestHandler
import json
import os
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """إعداد الويب هوك"""
        try:
            result = asyncio.run(self.setup_webhook())
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            logger.error(f"خطأ في إعداد الويب هوك: {e}")
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            error_response = {
                "status": "error",
                "message": str(e)
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    async def setup_webhook(self):
        """إعداد الويب هوك مع تيليجرام"""
        bot_token = os.getenv('BOT_TOKEN')
        webhook_url = os.getenv('WEBHOOK_URL')
        
        if not bot_token:
            raise ValueError("BOT_TOKEN غير محدد")
        
        if not webhook_url:
            # محاولة تخمين URL من headers
            host = self.headers.get('host', 'localhost')
            webhook_url = f"https://{host}/api/webhook"
        
        # إعداد الويب هوك
        telegram_api_url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
        
        payload = {
            "url": webhook_url,
            "allowed_updates": ["message", "callback_query", "inline_query"]
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(telegram_api_url, json=payload) as response:
                result = await response.json()
                
                if result.get('ok'):
                    return {
                        "status": "success",
                        "message": "تم إعداد الويب هوك بنجاح",
                        "webhook_url": webhook_url,
                        "telegram_response": result
                    }
                else:
                    raise Exception(f"فشل إعداد الويب هوك: {result}")
