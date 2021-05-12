# Este programa hace una lista de palabras en orden alfabetico del archivo que abra.

fname = input("Enter file name: ") #file romero.txt
fh = open(fname)
lst = list()

for line in fh:
    sps = line.split()
    for i in sps:
    	if i in lst:
        	continue
        else:
			lst.append(i)
lst.sort()
print(lst)
