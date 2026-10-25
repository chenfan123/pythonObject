def request(method, path, /, *, timeout=5, retries=3):
    print(method, path, timeout, retries)


request("GET", "/users", timeout=10)
# /：左侧只能按位置传递
# *：右侧只能按关键字传递
