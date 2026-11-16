# 中间件的使用
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.middleware("http")
async def middleware1(request, call_next):
    print("middleware1")
    print(request.url, request.method)
    if request.url.path == '/middleware':
        # 返回的响应必须是Response对象
        return Response(content="你访问了/middleware,直接返回了", media_type="text/plain")
    response = await call_next(request)
    print("middleware1 end")
    return response


@app.get('/middleware')
async def get_middle():
    print("get_middle")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
