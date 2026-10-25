# python查找名称时遵循L → E → G → B
# Local：当前函数内部。
# Enclosing：外层函数作用域。
# Global：当前模块的全局作用域。
# Built-in：Python 内置名称，如 len、print。

# 操作全局变量 global 与 nonlocal
# global：操作模块级全局名称。
# nonlocal：操作最近一层外部函数作用域中的名称。nonlocal 不会操作全局变量。
