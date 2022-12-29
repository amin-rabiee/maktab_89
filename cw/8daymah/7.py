import re

text = "jksdjkbjk90sdv8789@#jnjk8789"
pattern = r'\d+'
find = re.findall(pattern, text)
print(find)
