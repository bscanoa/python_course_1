#Lee cada línea del archivo y extrae su correo electrónico(así se repita).

fname = input("Enter file name: ") #file mbox-short.txt
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    wds = line.split()
    # 'Guardian', para las lineas vacias.
    #if len(wds) < 3:
    #   continue
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[1])
    count = count + 1

# my solution
#    if line.startswith('From:'):
 #       ch = line.split()
 #       email = ch[1]
 #       print (email)
 #       count = count + 1

print("There were", count, "lines in the file with From as the first word")