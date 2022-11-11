import re
def to_camel_case(text):
    text = ""
    pattern = re.compile(r'(a-z_-)')
    match = pattern.finditer(text, re.MULTILINE)
    for mat in match :
        return match

text = "the-stealth-warrior"

to_camel_case(text)