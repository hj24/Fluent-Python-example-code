"""
定位参数到仅限关键字参数
"""

# 用于生成HTML标签的函数
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


# 几种调用方式
print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', 'world', id=123))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag('p', 'hello', 'world', cls='sidebar', id=123))

# 仅限关键字参数是python3的新特性，若想指定仅限关键字参数，需将其放到*参数后
# 如果不想支持数量不定的参数，直接写*即可
def f(a, *, b):
	print(a)
	print(b)

f(1, b=4)