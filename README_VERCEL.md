# نشر البوت على Vercel

## الخطوات المطلوبة:

### 1. إعداد المتغيرات البيئية في Vercel:

\`\`\`bash
BOT_TOKEN=your_bot_token_here
DATABASE_URL=postgresql://username:password@host:port/database
WEBHOOK_URL=https://your-vercel-app.vercel.app
WEBHOOK_SECRET=your_webhook_secret
DEVELOPERS=123456789,987654321
ADMINS=111111111,222222222
\`\`\`

### 2. إعداد قاعدة البيانات:

يُنصح باستخدام:
- **Supabase** (مجاني)
- **Neon** (مجاني)
- **Railway** (مجاني جزئياً)

### 3. نشر البوت:

1. ارفع الكود إلى GitHub
2. اربط المستودع بـ Vercel
3. أضف المتغيرات البيئية
4. انشر البوت

### 4. إعداد الويب هوك:

بعد النشر، زر:
\`\`\`
https://your-vercel-app.vercel.app/api/setup
\`\`\`

### 5. اختبار البوت:

\`\`\`
https://your-vercel-app.vercel.app/api/index
\`\`\`

## الملفات المهمة:

- `vercel.json` - إعدادات Vercel
- `api/index.py` - نقطة الدخول الرئيسية
- `api/webhook.py` - معالج الويب هوك
- `api/setup.py` - إعداد الويب هوك
- `requirements.txt` - المتطلبات المحدثة

## ملاحظات مهمة:

1. **قاعدة البيانات**: يجب استخدام PostgreSQL بدلاً من SQLite
2. **الويب هوك**: مطلوب للعمل على Vercel
3. **المتغيرات البيئية**: يجب إضافتها في لوحة تحكم Vercel
4. **الحدود**: Vercel له حدود على وقت التنفيذ (10 ثانية للخطة المجانية)

## استكشاف الأخطاء:

1. تحقق من السجلات في لوحة تحكم Vercel
2. تأكد من صحة المتغيرات البيئية
3. تحقق من إعداد الويب هوك
4. اختبر الاتصال بقاعدة البيانات
