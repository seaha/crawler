import re

# 纯数字的正则 \d 0-9
pattern = re.compile('\d')
one = '1234a'
result = pattern.findall(one)
print(result)

# 匹配判断的方法
# match 方法 是否匹配成功 从头开始 匹配一次
r2 = pattern.match(one)
print(r2.group())