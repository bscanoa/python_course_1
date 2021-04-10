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

hrs = input("Enter Hours: ")
rat = input("Enter Rate: ")
h = float(hrs)
r = float(rat)
p = computepay(h,r)
print("Pay",p)

#Solución correcta, uso adecuado de las variables.

def computepay(hrs,rat):
   
    hrs = input("Enter Hours: ")
    rat = input("Enter Rate: ")
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