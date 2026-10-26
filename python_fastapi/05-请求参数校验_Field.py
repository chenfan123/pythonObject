# 第一个fastapi程序
from re import S
from fastapi import FastAPI, Query
import uvicorn
from fastapi import Path  # 路径参数
from pydantic import BaseModel, Field, field_validator
from typing import List
from enum import Enum
import uuid

app = FastAPI()  # 创建一个FastAPI实例


class User(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(default=18, description="The age of the user")
    email: str = Field(..., description="The email of the user")


@app.post('/users')
def create_user(user: User):
    return user


class Product(BaseModel):
    price: float = Field(..., gt=0, le=1000,
                         description="The price of the product")


@app.post('/products')
def create_product(product: Product):
    return product


class Order(BaseModel):
    products: List[Product] = Field(...,
                                    description="The products of the order")


@app.post('/orders')
def create_order(order: Order):
    return order


class Item(BaseModel):
    name: str = Field(..., title='商品名称',
                      description="The name of the item", example='苹果')

# 自定义验证


class CustomItem(Item):
    email: str
    phone: str

    @field_validator('phone', mode='before')  # mode='before' 表示在验证之前执行
    def validate_phone(cls, v):  # cls 表示类本身，v 表示要验证的值
        if not v.startswith('1'):
            raise ValueError('Phone must start with 1')
        return v

    @field_validator('email', mode='before')  # mode='before' 表示在验证之前执行
    def validate_email(cls, v):  # cls 表示类本身，v 表示要验证的值
        if not v.endswith('@example.com'):
            raise ValueError('Email must end with @example.com')
        return v


class Order(BaseModel):
    items: list = Field(..., description="The items of the order")
    address: str = Field(..., description="The address of the order")


class Status(str, Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'


class Task(BaseModel):
    status: Status = Field(default=Status.PENDING,
                           description="The status of the task")

# 动态默认值


class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()),
                    description="The id of the document")


if __name__ == "__main__":
    # 传入 app 对象时不能开 reload，否则 uvicorn 会直接退出。
    # 需要改代码自动重启时，在本目录执行：fastapi dev "01-路径参数.py"
    uvicorn.run(app, host="0.0.0.0", port=8000)
