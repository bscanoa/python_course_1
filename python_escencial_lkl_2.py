# Funciones, 
# su objetivo es acomodar el código en bloques
# para llamarlo cada que lo necesitemos. Reciclar el código y regresar el valor.

# Se define de la siguiente forma:

def saludo():
    print ("Hola")
def comer ():
    print("Gato")

saludo()
#Puedo llamar la función las veces que las necesite

## Funciones que reciben variables

def caida(nombre):
    print("¿Qué tal", nombre,"?")
nombre='Luis'
caida(nombre)

## Funciones que regresan valores

def sumar(numero1,numero2):
    resultado=numero1+numero2
    return resultado

valor=sumar(5,5)
print (valor)

## Funciones con parametros por defecto 

#Los valores siempre se colocan de derecha a izquierda.
# 'def sumar(numero1=2,numero2):' sería un error pues nnumero2 esta sin definir.

def sumar(numero1,numero2=2):
    resultado=numero1+numero2
    return resultado

valor=sumar(5,)
print (valor)

#Ejercicios

# Area de un rectangulo

def area_rectangulo(base, altura):
    area=base*altura
    print("El área es: ",area)

area_rectangulo(7,2)

# Calcular el promedio de tres números

def promedio(num1=0,num2=0,num3=0):
    resultado_p = (num1+num2+num3)/3
    return resultado_p
print("El promedio es:", promedio(9,8,10))
