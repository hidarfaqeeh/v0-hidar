class DatabaseConfig:
    """إعدادات قاعدة البيانات"""
    
    # مسار قاعدة البيانات
    DATABASE_PATH = "bot_database.db"
    
    # جداول قاعدة البيانات
    TABLES = {
        "users": """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id BIGINT UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                phone_number VARCHAR(20),
                language_code VARCHAR(10) DEFAULT 'ar',
                timezone VARCHAR(50) DEFAULT 'Asia/Riyadh',
                is_premium BOOLEAN DEFAULT FALSE,
                premium_expires TIMESTAMP,
                trial_used BOOLEAN DEFAULT FALSE,
                preferences TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_ip VARCHAR(45),
                is_banned BOOLEAN DEFAULT FALSE,
                ban_reason TEXT
            )
        """,
        
        "tasks": """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id BIGINT NOT NULL,
                name VARCHAR(255) NOT NULL,
                source_chat_id BIGINT NOT NULL,
                target_chat_ids TEXT NOT NULL,
                forward_type VARCHAR(20) DEFAULT 'forward',
                settings TEXT,
                is_active BOOLEAN DEFAULT TRUE,
                priority INTEGER DEFAULT 1,
                retry_count INTEGER DEFAULT 0,
                last_error TEXT,
                performance_stats TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """,
        
        "messages": """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                source_message_id INTEGER NOT NULL,
                target_message_ids TEXT,
                forwarded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (task_id) REFERENCES tasks (id)
            )
        """,
        
        "chats": """
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id BIGINT UNIQUE NOT NULL,
                chat_type VARCHAR(20) NOT NULL,
                title TEXT,
                username TEXT,
                member_count INTEGER DEFAULT 0,
                chat_permissions TEXT,
                bot_permissions TEXT,
                last_message_id INTEGER,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        
        "admins": """
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id BIGINT UNIQUE NOT NULL,
                added_by BIGINT,
                permissions TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (added_by) REFERENCES users (user_id)
            )
        """,
        
        "scheduled_messages": """
            CREATE TABLE IF NOT EXISTS scheduled_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id BIGINT NOT NULL,
                message_text TEXT NOT NULL,
                target_type VARCHAR(20) NOT NULL,
                target_ids TEXT NOT NULL,
                schedule_time TIMESTAMP NOT NULL,
                interval_minutes INTEGER,
                timezone VARCHAR(50),
                retry_count INTEGER DEFAULT 0,
                last_attempt TIMESTAMP,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """,
        
        "bot_clones": """
            CREATE TABLE IF NOT EXISTS bot_clones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id BIGINT NOT NULL,
                bot_token TEXT NOT NULL,
                bot_username TEXT,
                config TEXT,
                performance_stats TEXT,
                last_heartbeat TIMESTAMP,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (owner_id) REFERENCES users (user_id)
            )
        """
    }
