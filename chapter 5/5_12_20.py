"""
提取函数参数
"""

# 在指定长度附近截取字符串的函数
def clip(text, max_len=80):
	"""在max_len前面或后面第一个空格处截断文本"""
	end = None
	if len(text) > max_len:
		space_before = text.rfind(' ', 0, max_len)
		if space_before >= 0:
			end = space_before
		else:
			space_after = text.rfind(' ', max_len)
			if space_after >= 0:
				end = space_after
	if end is None:
		end = len(text)
	return text[:end].rstrip()

# 提取函数签名
# signature对象有parameters属性，有参数的具体信息 
from inspect import signature
sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
	print(param.kind, ':', name, '=', param.default)

"""
函数注解
python3的新语法

注解存储在__annotations__属性中
python不对其做检查，强制，验证与优化，对python解释器没有任何意义
注解只是元数据，供IDE，框架，装饰器使用
"""
def clip(text: str, max_len: 'int > 0'=80) -> str:
	"""在max_len前面或后面第一个空格处截断文本"""
	end = None
	if len(text) > max_len:
		space_before = text.rfind(' ', 0, max_len)
		if space_before >= 0:
			end = space_before
		else:
			space_after = text.rfind(' ', max_len)
			if space_after >= 0:
				end = space_after
	if end is None:
		end = len(text)
	return text[:end].rstrip()

print(clip.__annotations__)

