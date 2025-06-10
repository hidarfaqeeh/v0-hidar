# استخدام صورة Python الرسمية كأساس
FROM python:3.11-slim

# تعيين متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Riyadh

# تثبيت المتطلبات الأساسية فقط
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# إنشاء وتعيين دليل العمل
WORKDIR /app

# نسخ ملف المتطلبات أولاً
COPY requirements.simple.txt requirements.txt

# تثبيت متطلبات Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# إنشاء المجلدات اللازمة
RUN mkdir -p /app/data /app/logs

# تعريض المنفذ الذي سيستخدمه الويب هوك (إذا تم استخدامه)
EXPOSE 8443

# الأمر الافتراضي
CMD ["python", "main.py"]
