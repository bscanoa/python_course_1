
#Loops and Iteration

#Sentencia while
n = 5
while n > 0:
    print (n)
    n = n-1
# Siempre hay que terminar el loop o se volverá infinito.
print ('Blastoff!')
print (n)

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break #Para salir del loop.
    print(line)
print('Done!')


# Sentencia for

# Loop con enteros.
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

# Loop con strings
friends = ['Migue', 'Nataly', 'Fernando']
for friend in friends:
    print('Happy new year', friend)
print ('Done!')
