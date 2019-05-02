"""
所有映射类型在处理找不到的键的时候都会涉及__missing__方法
__missing__方法只对__getitem__调用，对其他如get和__contains__无用
"""
class StrKeyDict0(dict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError
		return self[str(key)]

	def get(self, key, default=None):
		try:
			return self[key]
		except KeyError:
			return default

	def __contains__(self, key):
		return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d[2])
print(d['2'])
print(d.get(1, 'N/A'))

"""
字典的变种
其中一种：collections.Counter
给键值准备一个整数计数器
"""
from collections import Counter

ct = Counter('aabbbbccdd')
print(ct)
ct.update('aaaaazzz')
print(ct)
# most_common(n)会按次序返回映射里最常见的n个键和它的计数
print(ct.most_common())
print(ct.most_common(2))

"""
子类化UserDict
一般来说倾向于继承UserDict而不是dict的原因是后者会在实现上走一点捷径
"""
from collections import UserDict

class StrKeyDict(UserDict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError
		return self[str(key)]

	def __contains__(self, key):
		return str(key) in self.data

	def __setitem__(self, key, item):
		self.data[str(key)] = item

d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d[2])
print(d['2'])
print(d.get(1, 'N/A'))

"""
不可变映射类型 MappingProxyType
给这个类一个映射，它会返回一个只读的视图，如对原映射做出改动，通过这个视图可以观察到
但无法通过这个视图对原映射做出修改
"""
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# 报错：
# d_proxy[2] = 'x'
# print(d_proxy)
d[2] = 'B'
print(d)
print(d_proxy)