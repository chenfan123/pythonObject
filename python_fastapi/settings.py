from typing import Dict

# aerich / Tortoise 共用配置
# 启动学习库：cd ../07-postgresql && docker compose up -d
TORTOISE_ORM: Dict = {
    "connections": {
        # "default": "sqlite://db.sqlite3",
        # "default": "mysql://root:123456@127.0.0.1:3306/dbname",
        "default": "postgres://learn:learn@127.0.0.1:5433/learn_db",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

TEST_ORM: Dict = {
    "connections": {
        "default": "postgres://learn:learn@127.0.0.1:5433/test_db",
    },
    "apps": {
        "models": {
            # testModel.Test + models.User/student
            "models": ["testModel", "models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

# 一对一关联练习库（与 test_db 的 students 表结构不同，单独建库）
RELATION_ORM: Dict = {
    "connections": {
        "default": "postgres://learn:learn@127.0.0.1:5433/relation_db",
    },
    "apps": {
        "models": {
            "models": ["relation_models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
