"""
一个简单的例子
"""

def deco(func):
	def inner():
		print('running inner()')
	return inner

@deco
def target():
	print('running target()')

target()

"""
装饰器在被装饰的函数定义之后就立即执行
"""
registry = []

def register(func):
	print(f'running register({func})')
	registry.append(func)
	return func

@register
def f1():
	print('running f1()')

@register
def f2():
	print('running f2()')

def f3():
	print('running f3()')

def f4():
	print('running f4()')

def main():
	print('running main()')
	print(f'registry -> {registry}')
	f1()
	f2()
	f3()
	f4()

if __name__ == '__main__':
	main()