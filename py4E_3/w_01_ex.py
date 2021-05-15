import re

file = input('Enter file name:')
if len(file) < 1: file = ('regex_sum_1205090.txt')
handfile = open(file)
ls = list()

for line in handfile:
    line = line.rstrip()
    if re.search('[0-9]+', line):
        y = re.findall('[0-9]+', line)
    else:
        continue
    
    for i in y:
        ls.append(i)

num = 0
for i in ls:
    non = int(i)
    num = num + non

print(num)
