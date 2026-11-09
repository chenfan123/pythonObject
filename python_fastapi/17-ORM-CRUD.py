from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import TEST_ORM

app = FastAPI()

# 注册 Tortoise：启动时建连，关闭时断开
# 使用 aerich 迁移后，建议把 generate_schemas 改为 False
register_tortoise(
    app,
    config=TEST_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
