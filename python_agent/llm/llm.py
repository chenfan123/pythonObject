import asyncio
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from langchain_qwq import ChatQwen

# 从 python_agent/.env 加载环境变量
load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)


def create_qwen_model() -> ChatQwen:
    """创建通义千问聊天模型（DashScope）。"""
    return ChatQwen(
        # 普通对话可用 qwen-plus / qwen-turbo；OCR 场景可换成 qwen3.5-ocr
        model=os.getenv("DASHSCOPE_MODEL", "qwen-plus"),
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # 国内 Key 必须用国内地址
        api_base=os.getenv(
            "DASHSCOPE_API_BASE",
            "https://dashscope.aliyuncs.com/compatible-mode/v1",
        ),
    )


model = create_qwen_model()


class QwenClient:
    """旅行 Agent 使用的同步封装：system + user -> 文本回复。"""

    def __init__(self, chat_model: ChatQwen | None = None) -> None:
        self.model = chat_model or create_qwen_model()

    def generate(self, prompt: str, system_prompt: str) -> str:
        """调用千问生成回应。"""
        print("正在调用大语言模型...")
        try:
            # LangChain 消息：system + human
            messages = [
                ("system", system_prompt),
                ("human", prompt),
            ]
            response = self.model.invoke(messages)
            content = response.content if hasattr(
                response, "content") else str(response)
            print("大语言模型响应成功。")
            return content if isinstance(content, str) else str(content)
        except Exception as e:
            print(f"调用LLM API时发生错误: {e}")
            return "错误:调用语言模型服务时出错。"


async def demo_async_stream():
    """演示异步调用的非阻塞特性"""
    print("=== 演示：astream 的异步（非阻塞）效果 ===")
    start_time = time.perf_counter()  # 记录开始时间
    print("程序开始...")

    # 1. 发起异步流式请求
    # 注意：此时请求已发出，返回的是一个异步生成器
    print(">>> 发起异步流式调用 (astream)...")
    stream_resp = model.astream("请用一句话解释机器学习的基本概念。")

    # 2. 在等待流式响应的同时，执行其他任务
    print(">>> 流式请求已发送，程序无需等待，继续执行其他异步任务...")
    for i in range(3):
        # 使用 asyncio.sleep 而非 time.sleep
        # 这允许事件循环在等待时去处理上面的 stream_resp 网络 IO
        await asyncio.sleep(1)
        print(
            f">>> 正在执行第{i + 1}个任务... (已耗时 {time.perf_counter() - start_time:.2f}s)"
        )

    # 3. 现在开始处理流式结果
    print(">>> 模拟任务已完成，开始读取缓冲区中的流式结果...")
    end_time = time.perf_counter()
    print(">>> 流式输出: ", end="", flush=True)
    async for chunk in stream_resp:
        # LangChain 的消息块通常通过 .content 获取内容
        content = chunk.content if hasattr(chunk, "content") else str(chunk)
        print(content, end="", flush=True)

    print("\n>>> 流式输出结束\n")
    print(f"=== 总运行耗时: {end_time - start_time:.2f}s ===")


async def main():
    """主函数"""
    await demo_async_stream()


if __name__ == "__main__":
    asyncio.run(main())
