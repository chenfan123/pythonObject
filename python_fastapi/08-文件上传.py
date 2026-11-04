# 文件上传
# pip install aiofiles
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
import uvicorn
import aiofiles
from pathlib import Path


app = FastAPI()

# 始终写到本文件同级的 data 目录，不依赖启动时的 cwd
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# 方式一：bytes类型（适合小文件）
# 文件以二进制形式读取，适合小于10MB的文件
# 内存占用高，大文件可能导致崩溃


@app.post("/upload")
def upload_bytes(file: bytes = File(...)):
    # bytes 只有文件内容，没有 filename / content_type
    save_path = DATA_DIR / "file.png"
    save_path.write_bytes(file)
    print(f"文件保存成功: {save_path}")
    return {
        "file_size": len(file),
        "save_path": str(save_path),
    }


# 方式二：UploadFile类型（推荐）
# 自动处理内存和磁盘存储（超过阈值存磁盘）
# 支持文件元数据（filename、content-type）
# 提供异步文件操作方法（read()、write())


@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:  # 1MB 为单位读取
        # chunk = await file.read(1024 * 1024)  # await 读取数据
        # while chunk:  # 直到读取完为止
        #     await f.write(chunk)
        #     chunk = await file.read(1024 * 1024)
        while chunk := await file.read(1024 * 1024):  # 上述的缩写
            await f.write(chunk)
    print(f"文件保存成功: {file.filename}")
    return {
        "filename": file.filename,
    }


@app.post("/batch-upload")
async def batch_upload(files: list[UploadFile] = File(...)):
    for file in files:
        async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:
            while chunk := await file.read(1024 * 1024):
                await f.write(chunk)
            print(f"文件保存成功: {file.filename}")
    return {
        "count": len(files),
        "names": [f.filename for f in files],
    }

# 限制上传格式
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@app.post("/batch-upload-form")
async def batch_upload_form(files: list[UploadFile] = File(...)):
    for file in files:
        # 提取后缀名
        # 也可以使用：Path(file.filename).suffix.lower()
        if file.filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail="不支持的文件格式")
        async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:
            while chunk := await file.read(1024 * 1024):
                await f.write(chunk)
            print(f"文件保存成功: {file.filename}")
    return {
        "count": len(files),
        "names": [f.filename for f in files],
    }


@app.post('/submit')
def submit(username: str = Form(...), file: UploadFile = File(...)):
    return {
        "username": username,
        "filename": file.filename,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
