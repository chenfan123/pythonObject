# 可迭代对象 iterable：可以通过 iter() 获取迭代器。
# 迭代器 iterator：可以通过 next() 逐个获取元素，并保存当前遍历状态。

# 常见可迭代对象包括：
# list, tuple, str, dict, set

# 两者的协议区别:
# 可迭代对象通常实现: __iter__()
# 迭代器实现: __iter__()、__next__()
# 迭代器再次调用 iter()，通常返回它自己

# for 循环的底层逻辑
# for 循环会调用 iter() 获取迭代器；
# 不断调用 next()；
# 捕获 StopIteration；自动结束循环。

# 自定义迭代器 - 倒计时
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value

# 可迭代对象每次调用 iter()，可以生成相互独立的迭代器
