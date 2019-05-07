"""
处理UnicodeEncodeError (编码错误)
把errors参数传给编码方法或函数
"""
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859_1'))
# print(city.encode('cp437')) UnicodeEncodeError
print(city.encode('cp437', errors='ignore'))	# 跳过无法编码的字符
print(city.encode('cp437', errors='replace'))	# 用?代替无法编码字符
print(city.encode('cp437', errors='xmlcharrefreplace'))		# 无法编码的字符替换成xml实体

"""
处理UnicodeDecodeError (解码错误)
"""
a = b'Montr\xe9al'
print(a.decode('utf-8', errors='replace'))
print(a.decode('utf-16'))
print(a.decode('iso8859_1'))
print(a.decode('koi8_r'))
print(a.decode('cp1252'))