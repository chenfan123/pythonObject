import fastapi
import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, PlainTextResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
app = fastapi.FastAPI()

# 字符串响应


@app.get('/string')
async def return_string():
    return 'Hello, World!'  # Content-Type: text/plain

# html响应


@app.get('/html')
async def return_html():
    # Content-Type: text/html
    return HTMLResponse(content='<h1>Hello, World!</h1>')


@app.get('/html2', response_class=HTMLResponse)
async def return_html2():
    return '<h1>Hello, World!</h1>'

# 重定向响应


@app.get('/redirect')
async def redirect():
    return RedirectResponse(url='/html')  # 302 Found

# html=True 传给 StaticFiles：访问目录时自动找 index.html
app.mount('/', StaticFiles(directory='static', html=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
