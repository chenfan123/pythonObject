# 列表格式
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from typing import List, Optional
from fastapi import Query

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_active: bool = True
    category: str


DB = [Item(id=i, name=f"Item {i}", price=i * 100, is_active=True if i %
           2 == 0 else False, category="apple" if i % 3 == 0 else "banana" if i % 5 == 0 else "orange") for i in range(1, 1001)]


@app.get('/items')
async def list_response():
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

# 过滤


@app.get('/items2')
async def list_response2(category: Optional[str] = Query(None, description="分类")):
    filter_items = DB
    if category:
        filter_items = [
            item for item in DB if item.category == category]
    return filter_items

# 分页


@app.get('/items3')
async def get_items3(
    page: int = Query(1, description="页码"),
    page_size: int = Query(10, description="每页条数"),
    category: Optional[str] = Query(None, description="分类")
):
    filter_items = DB
    if category:
        filter_items = [
            item for item in DB if item.category == category]
    total = len(filter_items)
    total_pages = (total + page_size - 1) // page_size  # // 整除
    start = (page - 1) * page_size
    end = start + page_size
    return filter_items[start:end]
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
