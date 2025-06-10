#!/bin/bash

# إنشاء المجلدات اللازمة إذا لم تكن موجودة
mkdir -p data logs

# نسخ ملف .env.simple إلى .env إذا لم يكن موجوداً
if [ ! -f .env ]; then
    cp .env.simple .env
    echo "تم إنشاء ملف .env، يرجى تعديله بالإعدادات الصحيحة"
fi

# تشغيل البوت
python main.py
