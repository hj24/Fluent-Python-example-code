"""
集合论
"""
needles = {1, 2, 3}
haystack = {1, 2, 3, 3, 4, 5, 6, 1}	# 去重
print(needles)
print(haystack)

# 交集运算，统计needles的元素在haystack中的出现次数，仅限集合类型
found = len(needles & haystack)
found_set = needles & haystack
print(found, found_set)

# 可以用于任何可迭代类型, 速度比上面慢
found = 0
for n in needles:
	if n in haystack:
		found += 1
print(found)

needles1 = [1, 2, 3]
haystack1 = [1, 2, 3, 3, 4, 5, 6, 1]	# 去重
# 改进后的集合交集运算，可用于任何可迭代类型
found = len(set(needles1) & set(haystack1))
print(found)

"""
创建集合的方式
空集必须用set
"""
s = set()
# s = {} 创建空字典
# s = {1} 创建包含1的集合
print(type(s))

# {1, 2, 3} 这种创建方式比 set([1, 2, 3])更快
# 后者需要先从set这个名字查询构造方法，然后新建一个列表再把列表传入到构造方法
# 前者则是利用一个专门的BUILD_SET的字节码来创建集合
# 用dis.dis(反汇编函数) 查看这两个方式的字节码
from dis import dis
print(dis('{1}'))
print(dis('set([1])'))

# python里没有针对frozenset的特殊字面量句法，只能采用构造方法
fs = frozenset(range(10))
print(fs)
print(type(fs))

"""
集合推导
"""

# 新建一个Latin-1字符集合，该集合的每个字符的Unicode名字里都有SIGN
from unicodedata import name
s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)

"""
常用集合操作
"""
print(needles & haystack)	# 交集
print(needles | haystack)	# 并集
print(haystack - needles)	# 差集
print(needles ^ haystack)	# 对称差集
print(5 in haystack)
print(needles <= haystack)	# 是否为子集
print(needles < haystack)	# 是否为真子集

needles.add(9)
print(needles)

needles.discard(10)	# 如有元素10则将它删除，否则无影响
print(needles)
# remove删除元素，但如果不存在，则KeyError
# needles.remove(10)

print(needles.pop())
print(needles)

"""
dict和set背后的哈希表
"""
# 键的顺序取决于添加顺序, 但如果只是次序不同，键值相同，那字典仍是相等的
DIAL_CODES = [
	(86, 'China'),
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
	(55, 'Brazil'),
	(92, 'Pakistan'),
	(7, 'Russia'),
]
d1 = dict(DIAL_CODES)
print('d1: ', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2: ', d2.keys())
# 按照国家名字首字母决定排序顺序
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3: ', d3.keys())
assert d1 == d2 and d2 == d3







