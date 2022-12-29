import re

string = "Python exercises, PHP exercises, C# exercises "
pattern = r'exercises'
matches = re.finditer(pattern, string)
for match in matches:
    print(match.group())

