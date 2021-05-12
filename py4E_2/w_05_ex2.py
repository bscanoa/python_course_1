# Palabra más común en un archivo, por medio de un histograma.

name = input('Enter file:')
handle = open(name)

count = dict()

# Añade las palabras a un diccionario y las va contando.

for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1

bigcount = None
bigword = None

# Determina cual es la palabra con el valor más alto.

for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print (bigword, bigcount)