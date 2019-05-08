"""
高阶函数：接收函数为参数或将函数作为结果返回的函数是高阶函数
sorted, map, filter, reduce
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(word):
	return word[::-1]

print(sorted(fruits, key=reverse))

"""
map, filter, reduce的替代品，列表推导和生成器表达式
"""
def factorial(n):
	"""return n!"""
	return 1 if n < 2 else n * factorial(n - 1)

fact = factorial
print(list(map(fact, range(6))))
print([fact(i) for i in range(6)])

print(list(map(fact, filter(lambda n: n % 2, range(6)))))
print([fact(i) for i in range(6) if i % 2])

"""
匿名函数
"""
print(sorted(fruits, key=lambda w: w[::-1]))
