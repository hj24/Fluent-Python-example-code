"""
unicode标准把字符的标识和字节表述进行了明确区分
字符的标识即码位
字符的具体表述取决于所用的编码
码位转化成字节序列的过程是编码
字节序列转换成码位的过程是解码
"""
s = 'café'
print(len(s))
b = s.encode('utf8')
print(b)
print(len(b))
print(b.decode('utf8'))

"""
字节概要
bytes或bytearray对象的各个元素介于0-255之间
对于一个序列类型，a[i]返回的是一个元素，a[i:i+1](切片)返回的是一个相同类型的序列
"""
cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[3])
print(cafe[3:4])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[0])
print(cafe_arr[-1:])

"""
二进制序列有一个str没有的类方法：fromhex
解析16进制数字对，构建二进制序列
"""
a = bytes.fromhex('31 4B CE A9 EC AB')	# 空格可写可不写
print(a)

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
ocets = bytes(numbers)
print(ocets)

"""
python自带了超过100种编解码器
1. latin1 (iso8859_1)
一种重要编码，是其它编码的基础，例如cp1252和Unicode
2. cp1252
微软的latin1超集，添加了有用的符号如欧元符号
3. gb2312
编码中文的陈旧标准
3. utf-8、utf-16
"""
# 使用三个常用编解码符编码 El Niño 得到的差异也很大
for codec in ['latin_1', 'utf_8', 'utf_16']:
	print(codec, 'El Niño'.encode(codec), sep='\t')

