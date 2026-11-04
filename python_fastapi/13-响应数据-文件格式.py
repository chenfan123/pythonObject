import fastapi
from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.responses import Response, FileResponse, StreamingResponse

app = fastapi.FastAPI()


@app.get('/custom-file')
async def get_custom_file():
    info = b'File content'
    return Response(
        content=info,
        media_type='text/plain',  # 文本内容
        # attachment 直接下载
        headers={'Content-Disposition': 'attachment; filename="info.txt"'}
    )


@app.get('/download_pdf')
async def download_pdf():
    path = './data/陈健华-agent工程师简历.pdf'
    return FileResponse(
        path=path,
        media_type='application/pdf',
        headers={'Content-Disposition': 'attachment; filename="report.pdf"'}
    )

# 下载mp4文件,本次没有mp4文件，大文件进行拆分成流


def generate_chunks(file_path: str, chunk_size: int = 1024*1024*5):
    with open(file_path, 'rb') as f:  # rb表示二进制读取
        while chunk := f.read(chunk_size):  # 读取文件，每次读取chunk_size大小的数据
            yield chunk  # 返回数据


@app.get('/download_mp4')
async def download_mp4():
    file_path = './data/test.mp4'
    return StreamingResponse(
        content=generate_chunks(file_path),
        media_type='video/mp4',
        headers={'Content-Disposition': 'attachment; filename="test.mp4"'}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
