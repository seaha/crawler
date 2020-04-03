import re

pattern = re.compile('^\d+$')
one='123a'
result = pattern.match(one)
print(result.group())