with open('input.txt', 'r', encoding="utf-8") as input_file:
    lines = input_file.readlines()


output_lines = []

i = 0
while i < len(lines):
    if '{Stickers}' in lines[i]:
        lines.pop(i-2)
        lines.pop(i-1)
        lines.pop(i-1)
    elif 'Joined the server.' in lines[i]:
        lines.pop(i-1)
        lines.pop(i-1)
    elif 'http' in lines[i]:
        lines.pop(i)
    elif '{Attachments}' in lines[i]:
        lines.pop(i)
    elif '{Embed}' in lines[i]:
        lines.pop(i)
    elif '{Reactions}' in lines[i]:
        lines.pop(i)
        lines.pop(i)
    elif lines[i].startswith('[') and (i == len(lines) - 1 or not lines[i+1].strip()):
        lines.pop(i)
    elif lines[i].startswith('[') and lines[i+1].startswith('['):
        lines.pop(i)
    elif lines[i].endswith('(pinned)\n'):
        lines[i] = lines[i][:-9] + ' '
    else:
        i += 1

with open('output.txt', 'w', encoding="utf-8") as file:
    file.writelines(lines)