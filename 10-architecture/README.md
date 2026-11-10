# 第 10 章：后端架构练习

运行前在 shell 中提供 `DATABASE_URL`，可参考 `.env.example`。

```bash
python -m uvicorn app.main:app --reload
```

数据库结构由 Alembic 管理：

```bash
alembic upgrade head
```

当前阶段建立 SQLAlchemy 的 Engine、Session、ORM Model、Repository 与首个 Alembic 迁移；Router、Service 和 DTO 会在后续小节加入。

## 测试

日常单元与接口测试不需要 PostgreSQL：

```bash
python -m pytest -q -m "not integration"
```

真实数据库集成测试默认跳过。先执行迁移，再显式提供测试数据库连接：

```bash
cd ../07-postgresql
docker compose --profile test up -d postgres_test

cd ../10-architecture
export INTEGRATION_DATABASE_URL="postgresql+asyncpg://learn:learn@127.0.0.1:5433/learn_test_db"
DATABASE_URL="$INTEGRATION_DATABASE_URL" alembic upgrade head
python -m pytest -q -m integration
```

集成测试使用随机邮箱，并在 `finally` 中删除本次创建的数据；仍应只指向专用测试数据库，绝不能指向开发或生产数据库。
