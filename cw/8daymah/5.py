import re
text = '2014-12-27'
pattern = r'-'

text = re.split(pattern, text)
out = "-".join(text[::-1])
print(out)