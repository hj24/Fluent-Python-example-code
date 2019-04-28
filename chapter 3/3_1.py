"""
字典
dict类型是python语言的基石，其性能出众的背后原因是散列表

标准库中的所有映射类型都是利用dict来实现的，因此它们都有个共同限制：
只有可散列的类型才能作为映射的键值
"""
from collections import abc

my_dict = {}
print(isinstance(my_dict, abc.Mapping))
"""
什么是可散列类型？
如果一个类型是可散列的话，那么在它的生命周期中其散列值不变
这个对象需要实现__hash__和__eq__方法，如果两个可散列对象是相等的那么它的散列值一定相同

原子不可变数据都是可散列类型，frozenset也是可散列类型
根据frozenset定义，它只能容纳可散列类型
而对于元组，只有它所包含的所有元素都是可散列的情况下它才是可散列的
"""
tt = (1, 2, (20, 40))
print(hash(tt))

# 会报错
# tl = (1, 2, [20, 40])
# print(hash(tl))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

"""
创建字典的不同方式
"""
a = dict(one=1, two=2, three=3)
print(a)
b = {'one': 1, 'two': 2, 'three': 3}
print(b)
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d)
e = dict([('one', 1), ('two', 2), ('three', 3)])
print(e)
c = dict({'one': 1, 'two': 2, 'three': 3})
print(c)
print(a == b == c == d == e)
"""
字典推导
可以把任何以键值对作为元素的可迭代对象中构建出字典
"""
DIAL_CODES = [
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

"""
常见映射方法
"""
print(a)
a.clear()
print(a)

print(b.get('one'))
print(b.items())
# 返回的元素是可迭代的
print(b.keys())
print(b.values())
b.popitem()
print(b)
# update方法，有相同的键值时会更新
h = {'mm': 123, 'one': 111}
b.update(h)
print(b)


