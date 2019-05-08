"""
可调用对象
python数据模型文档列出了7种可调用对象
1. 用户定义的函数
2. 内置函数
3. 内置方法
4. 方法
5. 类
6. 类的实例
7. 生成器函数
"""
print([callable(obj) for obj in (abs, str, 13)])

"""
用户定义的可调用类型
不仅Python函数是真正的对象，任何Python对象都可以表现的像函数
只需要实现实例方法__call__
"""
import random

class BingoCage:
	def __init__(self, item):
		self._items = list(item)
		random.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))

"""
函数内省
函数对象有很多属性，使用dir函数探知
"""
def factorial(n):
	"""return n!"""
	return 1 if n < 2 else n * factorial(n - 1)

print(dir(factorial))

# 大多数属性是python对象共有的
class C: pass
def func(): pass
obj = C()
# 函数对象有而常规对象没有的属性
print(sorted(set(dir(func)) - set(dir(obj))))