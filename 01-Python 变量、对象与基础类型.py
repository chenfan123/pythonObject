# python 的变量是一个指向对象的名字
# type 可以获取对象的类型
age = 18
name = "Tom"
price = 99.9
is_admin = True
nothing = None
print(type(age))  # <class int>
print(type(name))  # <class str>
print(type(price))  # <class float>
print(type(is_admin))  # <class bool>
print(type(nothing))  # <class NoneType>

# == 和 is
# # == 比较的是值是否相等
# # is判断的是是不是同一个对象
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# 默认参数不能使用[]或者{}


def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("A"))  # ['A']
print(add_item("B"))  # ['A', 'B']
print(add_item("C"))  # ['A', 'B', 'C']
