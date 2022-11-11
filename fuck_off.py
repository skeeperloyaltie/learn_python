import re

words = '''
    abcdefghijkl
    Skeep
    Fuck
    fuck
    fuck_off
    
mnopqrstuvwxyz .'''

pattern = re.compile(r'[\d\d\d\d]\s',re.MULTILINE)

match = pattern.finditer(words)
# print(match)
for matches in match:
    print(matches)