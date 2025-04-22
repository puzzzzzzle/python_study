from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 定义请求体模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/{item_id}")
async def create_item(
        item_id: int,  # 路径参数
        item: Item,  # 请求体
        q: Optional[str] = None,  # 查询参数
        skip: int = 0  # 带默认值的查询参数
):
    """
    创建新项目
    :param item_id: 项目ID(路径参数)
    :param item: 项目数据(请求体)
    :param q: 可选查询参数
    :param skip: 带默认值的查询参数
    :return: 包含所有参数的响应
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    result.update({"skip": skip})
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
