"""工具包。"""
from .attraction import get_attraction
from .weather import get_weather

# 将所有工具函数放入一个字典，方便后续调用
available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}


# 如果需要导出所有工具函数，可以使用以下方式
__all__ = list(available_tools.keys())
