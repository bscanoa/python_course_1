big = max("Hello world")
print (big)

# La función min busca el cáracter más pequeño o número.
# A modo contrario la función max el más grande.
# big y tiny son variables.

tiny = min("Hello Wolrd")
print (tiny)

#--------------------------------------------------------

def greet (lang) :
    if lang == 'es':
        print ('Hola')
    elif lang == 'fr' :
        print ('Bonjour')
    else:
        print ('Hello')

greet('es')
greet('en')
greet('fr')

#Assignment

def computepay(h,r):
    if h>40:
        hr=40*10.50 #También se debe usar r (la variable)
        ex=h-40
        p=hr+(ex*(10.50*1.5)) #Igual se debe usar r (la varible)
    else:
    	p=h*10.50 #En este caso no se usa el 10.50, se usa r pues es la variable.     
    return p 

#Ver la solucion correcta esta abajo.

#hrs = input("Enter Hours: ")
#rat = input("Enter Rate: ")
# h = float(hrs)
# r = float(rat)
# p = computepay(h,r)
# print("Pay",p)

#Solución correcta, uso adecuado de las variables.

def computepay(hrs,rat):
   
    # hrs = input("Enter Hours: ")
    # rat = input("Enter Rate: ")
    h = float(hrs)
    r = float(rat)
    
    if h>40:
        hr=40*r
        ex=h-40
        t=hr+(ex*(r*1.5))
    else:
    	t=h*r      
    return t


p = computepay(10,20)
print("Pay",p)


# Lasgest Value

largest_so_far = 0
print ('Before', largest_so_far)
list1 =  [9,41,12,3,74,15]
for the_num in list1:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ('After', largest_so_far)

# Counting
zork = 0
print('Before', zork)
for thing in list1 :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing in a loop
zork = 0
print('Before', zork)
for thing in list1 :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Finding the Average
count = 0 
sum = 0

print('Before', count, sum)
for value in list1:
    count = count + 1
    sum = sum + value
print('After', count, sum, int(sum/count))

# Filtering in a Loop

print('Before')
for value in list1:
    if value>20:
        print('Large number', value)
print('After')

# Search Using a Boolean Variable

found = False
print('Before', found)
for value in list1:
    if value==3:
        found = True 
        break
    print (found, value)
print('After', found)

# Smallest
smallest_so_far = None
for value in list1:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print (smallest_so_far, value)
print ('After', smallest_so_far)
