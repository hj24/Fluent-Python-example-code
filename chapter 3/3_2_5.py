"""
处理不到键的情况
get, setdefault, defalutdict
get(key, [default]) 
在没有key对应的值时直接返回default，所以需要d[key] = defalut这一步骤

setdefault(key, [default])
有key返回key的值，没有则另d[key] = default 然后返回default
"""

from collections import defaultdict

hash = {}
# print(hash[0]) 报错keyerror

# get
hash[0] = hash.get(0, [])
hash[0].extend([1, 2])
print(hash[0])

# setdefault
hash.setdefault(0, []).extend([3, 4])
# 等价于
# hash[0] = hash.get(0, [])
# hash[0].extend([3, 4])
print(hash[0])

# defaultdict
from collections import defaultdict
hash = defaultdict(list)
print(hash[0])
hash[0].append(1)
print(hash[0])
