# 生成器其实就是特殊的迭代器，定义生成器最常见的方法是在函数中使用 yield

# yield 的作用
# 生成器会产出 value；
# 暂停函数执行；
# 保存局部变量和执行位置；
# 等待下一次 next()；
# 下一次从 yield 后面继续执行。
def numbers():
    yield 1
    yield 2
    yield 3


generator = numbers()
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(next(generator))  # StopIteration

# 生成器函数调用时只创建生成器，不执行函数体，只有调用 next() 时才执行。
# 第一次yield会在当前这条yield执行后暂停，不会进行后续的执行
