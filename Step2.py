with open('output.txt', 'r', encoding="utf-8") as input_file:
    lines = input_file.readlines()


output_lines = []

i = 0
while i < len(lines):
    # remove any timestamps, which are formated in side of brackets, and add a ":" at the end of the line. Make a new line with the text after the timestamp the colon
    if lines[i].startswith('['):
        lines[i] = lines[i][lines[i].find(']')+2:-1] + ': \n'

    else:
        i += 1

with open('FinalOutput.txt', 'w', encoding="utf-8") as file:
    file.writelines(lines)
