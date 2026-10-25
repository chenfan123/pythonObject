"""
def example(a, b=10, *args, **kwargs):
    a：普通参数。
    b=10：默认参数。
    *args：接收多余的位置参数，函数内是 tuple。
    **kwargs：接收多余的关键字参数，函数内是 dict。
"""


def show(name, age=18, *skills, **profile):
    print(name)
    print(age)
    print(skills)
    print(profile)


show(
    "Alice",
    20,
    "Python",
    "FastAPI",
    city="Shanghai",
    level="junior",
)  # 运行结果：
# Alice
# 20
# ('Python', 'FastAPI')
# {'city': 'Shanghai', 'level': 'junior'}
