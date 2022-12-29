import re
string = "salam amin emrika akbar? "
match = re.findall(r'\b[aeAE]\w*\b', string)
print(match)