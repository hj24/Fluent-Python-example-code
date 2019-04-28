s = 'bicycle'
"""
srt[a:b:c] 在位置a,b之间以c为间隔切片
[a:b] 左闭右开
"""
print(s[1:2])
print(s[::3]) 
print(s[::-1])
print(s[::-2])
"""
给切片赋值: 如果将切片放在赋值语句的左边或把它作为del操作对象，我们就可以对序列
进行嫁接，切除或就地修改操作
"""
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
"""
wrong l[2:3] = 100
如果赋值对象是个切片，那么赋值语句的右侧必须是个可迭代对象
"""
l[2:3] = [100]
print(l)
"""
对序列使用+和*
"""
l = [1,2,3]
print(l * 5)
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'x'
print(board)
"""
相当于：
board = []
for i in range(3):
	row = ['_'] * 3
	board.append(row)
"""

# 错误写法：包含3个指向同一个列表的引用
wrong_board = [['_'] * 3] * 3	
wrong_board[1][2] = 'x'
print(wrong_board)
"""
相当于：
row = ['_'] * 3
wrong_board = []
for i in range(3):
	board.append(row)
"""

"""
序列的增量赋值
+= *=背后的方法__iadd__, __imul__,
如果类实现了以上两个方法，则运行+=和*=时会调用上述方法，
否则就退一步调用__add__,__mul__
两者区别是，__iadd__是就地加法，不会产生新对象
而__add__会产生新对象，相当于 a += b == a = a + b,产生新的a+b对象赋值给a
"""
l = [1, 2, 3]
print(l, id(l))
l *= 2
print(l, id(l))
t = (1, 2, 3)
print(t, id(t))
t *= 2
print(t, id(t))
"""
一个谜题
"""
t = (1, 2, [20, 30])
t[2] += [50, 60]
print(t)





