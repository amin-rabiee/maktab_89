import re
text = 'http://www.newspaper12345678.com/12345678edition/20141227.html'
pattern = r'/(\d{8})\.'

text = re.findall(pattern, text)
print(text)