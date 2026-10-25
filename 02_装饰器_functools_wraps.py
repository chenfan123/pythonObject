"""第 2 章：装饰器与 functools.wraps。

核心结论：
1. 函数是一等对象，可以赋值、传参和返回。
2. 装饰器接收函数对象并返回新的函数对象。
3. @decorator 等价于 func = decorator(func)。
4. 外层装饰器在函数定义完成后执行，wrapper 在调用时执行。
5. @wraps(func) 保留原函数的名称、文档、注解等元数据。
"""

from functools import wraps


def function_object_demo() -> None:
    """演示函数对象与函数调用结果的区别。"""

    def greet(name: str) -> str:
        return f"Hello, {name}"

    handler = greet  # 保存函数对象，没有调用 greet。
    result = greet("Bob")  # 调用函数，保存返回值。

    print(handler("Alice"))
    print(handler is greet)
    print(result)


def log_call(func):
    """通用装饰器：在原函数调用前后输出日志。"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result  # 不返回 result 时，调用者会得到 None。

    return wrapper


@log_call
def add(a: int, b: int) -> int:
    """返回两个整数之和。"""

    return a + b


# 上面的装饰器语法等价于：
#
# def add(a: int, b: int) -> int:
#     return a + b
#
# add = log_call(add)
#
# 不能写成 log_call(add(2, 3))，因为这会把计算结果 5 传给装饰器，
# 而不是把原始 add 函数对象传给装饰器。


def metadata_demo() -> None:
    """演示 wraps 对原函数元数据的保留。"""

    print(add.__name__)  # add，而不是 wrapper。
    print(add.__doc__)  # 返回两个整数之和。
    print(add.__annotations__)
    print(add.__wrapped__)  # 指向原始 add 函数。


def phase_demo() -> None:
    """演示装饰阶段、属性读取阶段和调用阶段。"""

    def trace(func):
        # trace(job) 在 job 定义完成后立即执行，因此先输出 1。
        print("1：执行 trace")

        @wraps(func)
        def wrapper():
            # 定义 wrapper 不会执行这里；调用 job() 时才执行。
            print("2：执行 wrapper")
            return func()

        return wrapper

    @trace
    def job():
        print("3：执行原始 job")
        return "4：job 的结果"

    # 读取属性不会调用 wrapper 或原始 job。
    print(job.__name__)
    print(job())


def authorize(func):
    """模拟权限检查装饰器。"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("检查权限")
        return func(*args, **kwargs)

    return wrapper


@authorize
def delete_user(user_id: int) -> str:
    """删除指定用户。"""

    return f"deleted: {user_id}"


def authorization_demo() -> None:
    """读取元数据不会触发权限检查，调用函数时才会。"""

    print(delete_user.__name__)
    print(delete_user.__doc__)
    print(delete_user(10))


def interview_notes() -> None:
    """打印本节面试复习要点。"""

    notes = (
        "装饰器本质：接收函数并返回函数的可调用对象。",
        "语法糖：@decorator 等价于 func = decorator(func)。",
        "装饰阶段：执行外层装饰器并创建 wrapper，但不执行 wrapper 函数体。",
        "调用阶段：先执行 wrapper，再由闭包中的 func 调用原函数。",
        "参数转发：wrapper 用 *args 和 **kwargs 接收并展开参数。",
        "返回值：wrapper 必须返回原函数结果，否则调用者得到 None。",
        "wraps：保留 __name__、__doc__、__annotations__ 和 __wrapped__。",
        "FastAPI：依赖函数签名和类型注解进行校验、依赖分析和文档生成。",
    )

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


if __name__ == "__main__":
    print("=== 函数对象 ===")
    function_object_demo()

    print("\n=== 基础装饰器 ===")
    print(add(2, 3))

    print("\n=== wraps 元数据 ===")
    metadata_demo()

    print("\n=== 装饰阶段与调用阶段 ===")
    phase_demo()

    print("\n=== 权限装饰器 ===")
    authorization_demo()

    print("\n=== 面试复习 ===")
    interview_notes()
