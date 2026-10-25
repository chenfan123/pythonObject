def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def say_hello():
    return "Hello"

#  其实就是 say_hello = log_call(say_hello)
# *args 接收任意位置参数；
# **kwargs 接收任意关键字参数；

# 注意：装饰器中的@log_call 会先执行，然后再执行 say_hello 函数。
# 然后@log_call执行后，实际上返回的是 wrapper 函数，所以 say_hello 函数实际上被 wrapper 函数替换。

# 带参数装饰器
# repeat(times)              接收装饰器配置
# └── decorator(func)        接收被装饰函数
#     └── wrapper(*args...)  接收函数调用参数
# 可以记成：配置参数 → 原函数 → 调用参数

# 多装饰器叠加
# 多装饰器的展开顺序是从下往上：
# decorator_a 的 wrapper
# └── decorator_b 的 wrapper
#     └── 原始 work
