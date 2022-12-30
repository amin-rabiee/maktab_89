import re

text = "jksdjkbjk90sdv8789@#jnjk8789"
pattern = r'\d+'
find = re.finditer(pattern, text)
for i in find:
    print(i.group())
