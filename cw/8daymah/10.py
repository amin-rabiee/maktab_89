import re

text = 'simple jomle Road and another Road'
pattern = r'Road'

text = re.sub(pattern, 'RD', text)
print(text)