# 元组不仅仅是不可变的列表，也可以是对一个没有名字的字段的记录
# 拆包可以让元组完美的当做记录来用
x_y = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tolyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
	print('%s / %s' % passport)

for country, _ in traveler_ids:
	print(country)

# 拆包
latitude, longitude = x_y
print(latitude)
print(longitude)

# * 运算符可以把一个可迭代对象拆开作为函数参数
t = (20, 8)
q, r = divmod(*t)
print(q, r)

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *body, b = range(5)
print(a, body, b)

# 嵌套结构中的拆包
metro_areas = [
	('Toyko', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))

# 具名元组
# 接收两个参数，一个是类名一个是类的各个字段的名字
# 后者可以是有数个字符串组成的可迭代对象也可以是用空格分开的字段名组成的字符串
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Toyko', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo[1])

# 具名元组的关键属性_fields, _make, _asdict
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi)
print(delhi._asdict())
for k, v in delhi._asdict().items():
	print(k, v)






















