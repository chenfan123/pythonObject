# FastAPI 项目结构：APIRouter + Tortoise 整合
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise

from integrate_models import User

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")
user_router = APIRouter(tags=["用户应用"], prefix="/user")
item_router = APIRouter(tags=["商品应用"])


class UserSchema(BaseModel):
    name: str
    email: str
    age: int


class ItemSchema(BaseModel):
    name: str
    price: float


@user_router.post("/create")
async def create_user(user: UserSchema):
    # 使用 model_dump() 将 Pydantic 模型转换为字典
    obj = await User.create(**user.model_dump())
    return {
        "message": "用户创建成功",
        "user": obj,
    }


@user_router.get('/firstInfo')
async def first_info():
    obj = await User.first()
    user = UserSchema.model_validate(obj.__dict__)  # 将模型转换为 Pydantic 模型,提取相关字段
    return {
        "message": "用户信息",
        "user": user
    }


@user_router.get("/list")
async def list_users():
    users = await User.all()
    return {
        "users": [
            {"id": u.id, "name": u.name, "email": u.email, "age": u.age}
            for u in users
        ]
    }


@item_router.post("/create")
async def create_item(item: ItemSchema):
    return {
        "message": "商品创建成功",
        "item": item.model_dump(),
    }


@item_router.get("/list")
async def list_items():
    return {"items": [{"name": "demo", "price": 9.9}]}


v1_router.include_router(user_router)
v1_router.include_router(item_router)
app.include_router(v1_router)

# 文件名含中文无法作为模块导入，模型放在 integrate_models.py
register_tortoise(
    app,
    db_url="postgres://learn:learn@127.0.0.1:5433/fastapi_integrate_db",
    modules={"models": ["integrate_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
