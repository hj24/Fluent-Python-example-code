"""
一等函数：函数作为一等对象
一等对象的定义：
1. 在运行时创建
2. 能赋值给变量或者数据结构中的元素
3. 能作为参数传给函数
4. 能作为函数的返回结果
"""

"""
把函数视为对象
"""
def factorial(n):
	"""return n!"""
	return 1 if n < 2 else n * factorial(n - 1)

print(factorial)
print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

"""
通过别名使用函数，再把函数作为参数传递
"""
fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))