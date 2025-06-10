import asyncio
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# تشغيل ترقيات قاعدة البيانات عند بدء التشغيل
async def run_database_migrations():
    """تشغيل ترقيات قاعدة البيانات"""
    try:
        from database.db_manager import DatabaseManager
        from database.migrations import MigrationManager
        
        # تهيئة قاعدة البيانات أولاً
        db = DatabaseManager()
        await db.initialize()
        
        # تشغيل الترقيات
        migration_manager = MigrationManager(db)
        
        logger.info("🔄 بدء تطبيق ترقيات قاعدة البيانات...")
        result = await migration_manager.run_migrations()
        
        if result['applied'] > 0:
            logger.info(f"✅ تم تطبيق {result['applied']} ترقية بنجاح")
        else:
            logger.info("✅ قاعدة البيانات محدثة - لا توجد ترقيات معلقة")
            
        if result['errors']:
            logger.warning(f"⚠️ حدثت أخطاء في {len(result['errors'])} ترقية")
            for error in result['errors']:
                logger.error(f"❌ {error}")
        
        return db
                
    except Exception as e:
        logger.error(f"❌ خطأ في تطبيق ترقيات قاعدة البيانات: {e}")
        raise

async def main():
    """Main function to run the bot."""
    try:
        # Initialize and run database migrations
        db = await run_database_migrations()

        # Your bot initialization and startup code goes here
        logger.info("🚀 Bot is starting...")
        
        # مثال على تهيئة البوت
        # from bot import TelegramBot
        # bot = TelegramBot(db)
        # await bot.start()
        
        logger.info("✅ Bot started successfully!")
        
        # إبقاء البوت يعمل
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ An error occurred during startup: {e}")

if __name__ == "__main__":
    asyncio.run(main())
