from math import hypot

class Vector:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return f'Vector({self.x}, {self.y})'

	"""
	__repr__和__str__的区别是，后者只在str(),print()函数被调用
	__repr__则可以在交互式控制台和调试程序中被使用
	__str__没有定义时，系统会调用__repr__代替
	"""
	def __repr__(self):
		return f'Object Vector({self.x}, {self.y})'

	def __abs__(self):
		return hypot(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)