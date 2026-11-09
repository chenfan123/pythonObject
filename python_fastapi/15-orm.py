from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import TORTOISE_ORM

app = FastAPI()

# 注册 Tortoise：启动时建连，关闭时断开
# 使用 aerich 迁移后，建议把 generate_schemas 改为 False
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    from tortoise import Tortoise

    conn = Tortoise.get_connection("default")
    row = await conn.execute_query_dict(
        "SELECT current_database() AS db, current_user AS user"
    )
    return {"message": "PostgreSQL connected", "info": row[0]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
