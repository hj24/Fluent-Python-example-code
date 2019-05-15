"""
函数式编程

python并不是一门函数式编程语言
但functools和operator包的支持让它也可以轻松的进行函数式编程
"""
from functools import reduce
from operator import mul

# 使用reduce函数和一个匿名函数计算阶乘
def fact_1(n):
	return reduce(lambda a, b: a * b, range(1, n + 1))

print(fact_1(5))

# 用operator的mul改写上面的函数
def fact_2(n):
	return reduce(mul, range(1, n + 1))

print(fact_2(5))

# operator 还有一类函数能代替代替从序列中取出元素的lambda表达式：
# itemgetter, attrgetter
data = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter
for c in sorted(data, key=itemgetter(1)):
	print(c)

cc_name = itemgetter(1, 0)
for c in data:
	print(cc_name(c))

from collections import namedtuple
from inspect import signature
from operator import attrgetter

# attrgetter的作用和itemgetter类似，根据给出的名字提取对象的属性

LatLong = namedtuple('LatLong', 'lat long')
DataList = namedtuple('DataList', 'name cc pop coord')
areas = [DataList(name, cc, pop, LatLong(lat, long))
		for (name, cc, pop, (lat, long)) in data]
print(signature(DataList))
print(areas[0].coord.lat)

name_lat = attrgetter('name', 'coord.lat')
for c in sorted(areas, key=attrgetter('coord.lat')):
	print(name_lat(c))

# 在operator余下的函数中，最重要的是methodcaller
# 调用方法

from operator import methodcaller

s = 'The Time Has Come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

print(str.upper(s))

# 使用functools.partial冻结参数
# functools提供一系列高阶函数
# partial作用到一个函数上，把原函数的某些参数固定即冻结

from functools import partial
from operator import mul

# 把mul的第一个参数固定为3
triple = partial(mul,3)
print(triple(7))
print([triple(i) for i in range(11)])

# 把partial应用于之前的tag函数
def tag(name, *content, cls=None, **attrs):
	"""生成一个或多个HTML标签"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
							for attr, value
							in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
						(name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='hehe.jpg'))