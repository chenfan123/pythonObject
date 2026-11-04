# JSON 响应

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi import Body
from typing import TypeVar, Generic, Union
app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str
    tags: list[str] = []


# 定义范型模型T=TypeVar
T = TypeVar('T')


class SuccessResponse(BaseModel, Generic[T]):
    status: str = "success"
    data: T


class ErrorResponse(BaseModel, Generic[T]):
    status: str = "error"
    message: str
    data: T
    code: int

# 通过返回字典类型


@app.post('/json')
async def json_response():
    return User(name="John", age=20, email="john@example.com")

# 通过response_model指定返回数据类型
# response_model_exclude_unset 排除未设置的值


@app.post('/json-list', response_model=list[User], response_model_exclude_unset=True)
async def json_list_response():
    return [User(name="John", age=20, email="john@example.com"), User(name="Jane", age=21, email="jane@example.com")]


@app.get('/items/{item_id}', response_model=Union[SuccessResponse[User], ErrorResponse[User]])
async def get_item(item_id: int):
    if item_id == 1:
        item = User(name="Item 1", price=100)
        return SuccessResponse(data=item)
    else:
        return ErrorResponse(message="Item not found", code=404, data=None)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
