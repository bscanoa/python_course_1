##Variables
#Las variables almacenan datos que se van a manipular en memoria.
#Estos datos pueden ser de diferentes tipos,
#para el caso de python son: enteros, como la edad o números en general,
#reales y flotantes como la estatura de alguien,
#las cadenas como por ejemplo los nombre y van siempre entre comillas 
#y por último los de tipo booleano que tienen valores de falso o verdadero. 
#También soporta números complejos.



##Operdores matemáticos y comentarios.
#x=10
#y=2
#resultado=x/y
#resultado2=x%y

## Soporta operaciones aritmeticas básica suma (+) resta (-) multiplicación (*)
## división, // -> Redondea / -> Hace la división normal
## Residuo % -> Lo que sobra en una división. Si x=11 entonces x%y = 1.
## Potenciación 2**3 = 8 Es igual que dos elevado a la tres.

#print (2**3)


###Condicional IF
##Condición es una regla que se verifica y si se cumple toma un camino si no tomará otro.
##Sirven para tomar una descición.
#estructura básica if(condicion)

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

