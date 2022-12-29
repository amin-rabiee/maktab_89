import re
words = ['amin', 'pride', 'benz', 'parima', 'parastoo', 'pari', ]
pattern = r"^p"
found = []
for item in words:
    if re.search(pattern, item) and len(found) < 2 :
        found.append(item)
for i in found:
    print(i)