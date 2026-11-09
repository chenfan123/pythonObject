from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" VARCHAR(36) NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "uid_users_usernam_df2ee6" UNIQUE ("username", "email")
);
CREATE INDEX IF NOT EXISTS "idx_users_usernam_df2ee6" ON "users" ("username", "email");
        CREATE TABLE IF NOT EXISTS "students" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "age" INT,
    "email" VARCHAR(100) UNIQUE
);
COMMENT ON COLUMN "students"."id" IS '学生ID，主键';
COMMENT ON COLUMN "students"."name" IS '学生姓名';
COMMENT ON COLUMN "students"."age" IS '学生年龄，可为空';
COMMENT ON COLUMN "students"."email" IS '学生邮箱，唯一';
COMMENT ON TABLE "students" IS '学生模型，包含基本信息。';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";
        DROP TABLE IF EXISTS "students";"""
