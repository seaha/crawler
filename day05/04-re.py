import re

# 贪婪模式 从开头匹配到结尾
one = 'mdjjjjjjn1234456n'
pattern = re.compile('m(.*)n')
result = pattern.findall(one)
print(result) # ['djjjjjjn1234456']

# 非贪婪模式， 只匹配一次
one = 'mdjjjjjjn1234456n'
pattern = re.compile('m(.*?)n')
result = pattern.findall(one)
print(result) # ['djjjjjj']

# two
two = '2.5'
pattern = re.compile('2(\.)5')
result = pattern.findall(two)
print(result)