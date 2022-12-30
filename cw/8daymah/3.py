import re
text = 'Python exercises,_PHP exercises, C# exercises'
pattern = r''


text = re.sub(r' ', '1', text)
text = re.sub(r'_', ' ', text)
text = re.sub(r'1', '_', text)

print(text)