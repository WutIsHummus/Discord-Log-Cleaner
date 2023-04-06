import re

filename = 'FinalOutput.txt'

with open(filename, 'r', encoding="utf-8") as f:
    text = f.read()
text = re.sub(r'\n{3,}', '\n\n', text)
with open(filename, 'w', encoding="utf-8") as f:
    f.write(text)
