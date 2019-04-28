"""
数组，内存视图与队列
如果仅仅需要的是一个全是数字的列表，那么array比list更高效
创建数组需要提供一个类型码
除了支持可变序列的所有操作外，array还支持.frombytes和.tofile等文件读写函数
"""
from array import array
from random import random, randint

# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()

# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7)
# fp.close()
# print(floats2[-1])
# print(floats2 == floats)
"""
从py 3.4起，array不在支持list.sort这种就地排序
"""
arr = array('I', (randint(0,10) for i in range(10)))
print(arr)
sorted_arr = array(arr.typecode, sorted(arr))
print(sorted_arr)
"""
内存视图
在不复制内容的情况下操作同一个数组的不同切片
memoryview.cast 会把同一快内存中的内容打包成一个全新的memoryview对象给你
"""
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(numbers)
print(len(memv))
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)

"""
双相队列和其他形式的队列
collections.deque类
"""
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3) # 就地旋转操作
print(dq)
dq.rotate(-3) # 就地旋转操作
print(dq)
# 队列满了之后追加元素会在反向端删除过期元素
# 这符合队列性质
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30])
print(dq)

