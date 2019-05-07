"""
为了正确比较而规范化的Unicode字符
"""
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2) # 应该相等却返回False

"""
normalize提供规范化
四个参数 NFC, NFD, NFKC, NFKD
NFC 使用最少的码位构成等价字符串
NFD 把组合字符分解成基字符和单独的组合字符
NFKC与NFKD中的K表示兼容性
"""
from unicodedata import normalize
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

"""
大小写折叠：把所有文本都变成小写
对于只包含latin1字符的字符串 s.casefold()与s.lower()效果一样

要处理多文本语言可以关注以下两种函数
"""
def nfc_equal(str1, str2):
	return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
	return (normalize('NFC', str1).casefold() == 
			normalize('NFC', str2).casefold())

s1 = 'café'
s2 = 'cafe\u0301'

print(nfc_equal(s1, s2))
print(fold_equal(s1, s2))
print(nfc_equal('A', 'a'))
print(fold_equal('A', 'a'))