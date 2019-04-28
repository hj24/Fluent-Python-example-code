"""
list.sort方法和内置函数sorted
list.sort方法就地排序，不会把列表复制一份，返回None
sorted则会创建一个新的排好序的列表将其返回
"""
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(fruits.sort())
print(fruits)
"""
用bisect来管理自己排序的序列
该模块主要包含两个函数。bisect和insort，都是利用二分查找来在有序的序列中查找或插入元素
常见用法：
1. bisect(haystack, needle)在haystack中搜索needle的位置index
2. 然后用haystack.insert(index, needle)插入新值

format函数：{:x<4d}	5xxx 数字补x (填充右边, 宽度为4)
"""
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def demo(bisect_fn):
	for needle in reversed(NEEDLES):
		pos = bisect_fn(HAYSTACK, needle)
		offset = pos * ' |'
		print(ROW_FMT.format(needle, pos, offset))

def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	return grades[i]

"""
用bisect.insort插入新元素
"""
import random

if __name__ == '__main__':
	# 一个更小的例子
	idx = bisect.bisect(HAYSTACK, 5)
	HAYSTACK.insert(idx, 5)
	print(HAYSTACK)
	print(idx)

	bisect_fn = bisect.bisect
	print('DEMO: ', bisect_fn.__name__)
	print('haystack->', ''.join('%2d' % n for n in HAYSTACK))
	demo(bisect_fn)

	bisect_fn = bisect.bisect_left
	print('DEMO: ', bisect_fn.__name__)
	print('haystack->', ''.join('%2d' % n for n in HAYSTACK))
	demo(bisect_fn)

	grade_list = [grade(score) for score in [33, 99, 70, 90, 100]]
	print(grade_list)

	SIZE = 7

	random.seed(1729)

	my_list = []
	for i in range(SIZE):
		new_item = random.randrange(SIZE*2)
		bisect.insort(my_list, new_item)
		print('%2d ->' % new_item, my_list)

	print(bisect.insort(my_list, 5))
	print(my_list)


