symbols = '$&%*'
code = []
for symbol in symbols:
	code.append(symbol)
print(code)

code = [ord(symbol) for symbol in symbols]
print(code)

# python3里不会有列表推导导致变量泄漏问题
# 这段代码在python2里会打印
# print(x) -- 'c'
# print(dummy) -- [97, 98, 99]
x = 'abc'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

colors = ['black', 'white']
sizes = ['s', 'm', 'l']
tshirt = [(color, size) for color in colors
						for size in sizes]
print(tshirt)

# 用生成器表达式初始化元组与数组
"""
	C type 				Python type
'b'	signed char			int					1	 
'B'	unsigned char		int					1	 
'u'	Py_UNICODE			Unicode character	2	(1)
'h'	signed short		int					2	 
'H'	unsigned short		int					2	 
'i'	signed int			int					2	 
'I'	unsigned int		int					2	 
'l'	signed long			int					4	 
'L'	unsigned long		int					4	 
'q'	signed long long	int					8	(2)
'Q'	unsigned long long	int					8	(2)
'f'	float				float				4	 
'd'	double				float				8	 
"""
symbols = '$&%*'
code = tuple(ord(symbol) for symbol in symbols)
print(code)
import array
array_code = array.array('I', (ord(symbol) for symbol in symbols))
print(array_code)
# 使用生成器表达式计算笛卡尔积
# 与列表推导相比，利用生成器表达式惰性计算的特性，每次for循环时才产生一个组合
# 如果这种情况用列表推导，会在内存中留下一个列表，多出很多开销
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
	print(tshirt)