# 第一个fastapi程序
from re import S
from fastapi import FastAPI, Query
import uvicorn
from fastapi import Path  # 路径参数
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Optional
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

# 自定义验证（单字段）
# field_validator：只校验某一个字段本身
# @classmethod：类方法，第一个参数是 cls（类本身），不是 self（实例）
#   因为校验时模型实例往往还没创建出来，所以校验器挂在「类」上执行


class CustomItem(Item):
    email: str
    phone: str

    @field_validator('phone', mode='before')  # mode='before' 表示在类型转换/验证之前执行
    @classmethod
    def validate_phone(cls, v):  # cls=类本身，v=当前字段值
        if not v.startswith('1'):
            raise ValueError('Phone must start with 1')
        return v

    @field_validator('email', mode='before')
    @classmethod
    def validate_email(cls, v):
        if not v.endswith('@example.com'):
            raise ValueError('Email must end with @example.com')
        return v

# 字段联动校验（跨字段）
# model_validator：能同时看到多个字段，适合密码确认、起止时间、条件必填等
# mode='after'：各字段先各自校验通过，再建好实例，用 self.xxx 做联动判断，必须 return self
# mode='before'：拿到的还是原始 dict，适合先改输入结构；通常配合 @classmethod


class RegisterForm(BaseModel):
    password: str = Field(..., min_length=6)
    confirm_password: str
    age: int = Field(..., ge=0)
    is_adult_only: bool = False
    backup_phone: Optional[str] = None
    phone: Optional[str] = None

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if v.isdigit():
            raise ValueError('密码不能是纯数字')
        return v

    @model_validator(mode='after')
    def check_relations(self):
        # 1) 两个字段必须一致
        if self.password != self.confirm_password:
            raise ValueError('两次密码不一致')
        # 2) 条件联动：勾选成人内容时，年龄必须 >= 18
        if self.is_adult_only and self.age < 18:
            raise ValueError('选择成人内容时，年龄必须满 18')
        # 3) 备用手机号不能和主手机号相同
        if self.backup_phone and self.phone and self.backup_phone == self.phone:
            raise ValueError('备用手机号不能和主手机号相同')
        return self


@app.post('/register')
def register(form: RegisterForm):
    return form


class OrderDetail(BaseModel):
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
