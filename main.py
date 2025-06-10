import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# تشغيل ترقيات قاعدة البيانات عند بدء التشغيل
async def run_database_migrations():
    """تشغيل ترقيات قاعدة البيانات"""
    try:
        from database.db_manager import DatabaseManager
        from database.migrations import MigrationManager
        
        db = DatabaseManager()
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
                
    except Exception as e:
        logger.error(f"❌ خطأ في تطبيق ترقيات قاعدة البيانات: {e}")
        raise

async def main():
    """Main function to run the bot."""
    try:
        # Initialize and run database migrations
        await run_database_migrations()

        # Your bot initialization and startup code goes here
        logger.info("🚀 Bot is starting...")
        # Example:
        # from bot import Bot
        # bot = Bot()
        # await bot.start()
        logger.info("✅ Bot started successfully!")

    except Exception as e:
        logger.error(f"❌ An error occurred during startup: {e}")

if __name__ == "__main__":
    asyncio.run(main())
