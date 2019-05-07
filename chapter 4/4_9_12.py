"""
处理文本文件最佳实践
尽早把输入的字节序列解码成字符串
程序业务逻辑中只处理文本文件
输出时尽量晚的把字符串编码成字节序列
"""
fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp.write('café'))
fp.close()
re = open('cafe.txt', encoding='utf_8')
print(re.read())
re.close()

# 文本模式，返回io.TextIOWrapper
fp2 = open('cafe.txt', 'r', encoding='utf_8')
print(fp2)
fp2.close()

import os
print(os.stat('cafe.txt').st_size)

# 读字节返回 io.BufferedReader
fp3 = open('cafe.txt', 'rb')
print(fp3)
print(fp3.read())
