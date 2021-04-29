##Variables
#Las variables almacenan datos que se van a manipular en memoria.
#Estos datos pueden ser de diferentes tipos,
#para el caso de python son: enteros, como la edad o números en general,
#reales y flotantes como la estatura de alguien,
#las cadenas como por ejemplo los nombre y van siempre entre comillas 
#y por último los de tipo booleano que tienen valores de falso o verdadero. 
#También soporta números complejos.

#nombre_de_la_variable=valor_asignado

##Operadores matemáticos y comentarios.

x=10
y=2
resultado=x/y
resultado_2=x%y

## Soporta operaciones aritmeticas básica suma (+) resta (-) multiplicación (*)
## división, // -> Redondea / -> Hace la división normal
## Residuo % -> Lo que sobra en una división. Si x=11 entonces x%y = 1.
## Potenciación 2**3 = 8 Es igual que dos elevado a la tres.

print(resultado)
print(resultado_2)
print (2**3)


###Condicional IF
##Condición es una regla que se verifica y si se cumple toma un camino si no tomará otro.
##Sirven para tomar una descición.
#estructura básica:
#if(condicion):
#   instrucciones si se cumple
#else:
#   instrucciones si no cumple

edad=19
pago=False
if edad>18:
    print ("Sí es mayor de edad.")
    # El igual solo es de asingnación y el doble es de verificación.
    if pago==True:
        print("Entonces eres mayor y pagaste")
    else:
        print("Eres mayor de edad y no pagaste")
else:
    print ("No es mayor de edad")

## Operadores relacionales en Python

#Se encargan de la comparar de valores.
# < menor que
# <= menor o igual
# > mayor que
# >= mayor o igual
# == para saber si son iguales
# != para saber si son diferentes

## Operadores lógicos

# and  puede unir dos condiciones y verificarlas al mismo tiempo, se deben cumplir las dos condiciones.
if edad>18 and edad<20:
    print("Tu edad es 19")
else:
    print("Tu edad no es 19")
# or solo es necesario que se cumpla una de las condiciones.
if edad>18 or edad<20 or edad==24:
    print("Tu edad es aceptada")
else:
    print("Tu edad no es aceptada")
# not, se coloca antes de la condición 
if not edad<18 :
    print("Tu edad es aceptada")
else:
    print("Tu edad no es aceptada")

##Sentencia while
#Es un bucle "mientras", mietras se cumpla una condición las intrucciones se ejecutaran
# while(este_lloviendo):
#   usar_sombrilla

numero=1

while(numero<100):
    print("El valor de número es:", numero)
    numero=numero+1

#Se ejecuta cuando sabemos lo que queremos o lo que no queremos.