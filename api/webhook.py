"""
معالج الويب هوك لتيليجرام
Telegram Webhook Handler
"""

from http.server import BaseHTTPRequestHandler
import json
import os
import asyncio
import logging
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# إعداد السجلات
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """معالجة طلبات الويب هوك من تيليجرام"""
        try:
            # قراءة البيانات
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_error(400, "No data received")
                return
                
            post_data = self.rfile.read(content_length)
            
            # التحقق من صحة JSON
            try:
                update_data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_error(400, "Invalid JSON")
                return
            
            # معالجة التحديث
            asyncio.run(self.process_telegram_update(update_data))
            
            # إرسال استجابة نجاح
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {"status": "ok"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            logger.error(f"خطأ في معالجة الويب هوك: {e}")
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))
    
    async def process_telegram_update(self, update_data):
        """معالجة تحديث من تيليجرام"""
        try:
            bot_token = os.getenv('BOT_TOKEN')
            if not bot_token:
                raise ValueError("BOT_TOKEN غير محدد في متغيرات البيئة")
            
            # إنشاء التطبيق
            application = Application.builder().token(bot_token).build()
            
            # إضافة المعالجات
            application.add_handler(CommandHandler("start", self.start_command))
            application.add_handler(CommandHandler("help", self.help_command))
            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
            
            # تحويل البيانات إلى كائن Update
            update = Update.de_json(update_data, application.bot)
            
            # معالجة التحديث
            await application.process_update(update)
            
        except Exception as e:
            logger.error(f"خطأ في معالجة التحديث: {e}")
            raise
    
    async def start_command(self, update, context):
        """معالج أمر /start"""
        welcome_message = """
🤖 مرحباً بك في البوت!

هذا البوت يعمل على Vercel ويمكنه:
• إعادة توجيه الرسائل
• جدولة الرسائل
• إدارة المهام
• والمزيد...

استخدم /help لرؤية جميع الأوامر المتاحة.
        """
        await update.message.reply_text(welcome_message.strip())
    
    async def help_command(self, update, context):
        """معالج أمر /help"""
        help_message = """
📋 الأوامر المتاحة:

/start - بدء استخدام البوت
/help - عرض هذه المساعدة
/status - حالة البوت

🔧 قيد التطوير:
• إعادة توجيه الرسائل
• جدولة الرسائل
• إدارة المهام
        """
        await update.message.reply_text(help_message.strip())
    
    async def handle_message(self, update, context):
        """معالج الرسائل العادية"""
        user_message = update.message.text
        response = f"تم استلام رسالتك: {user_message}\n\n🔄 البوت قيد التطوير..."
        await update.message.reply_text(response)
