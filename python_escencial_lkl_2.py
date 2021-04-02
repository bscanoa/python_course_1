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


##Tuplas 
# Las tuplas, nos permiten almacenar elementos de difertentes tipos
# Las tuplas son inmutables.
tupla=(25,1.73,"Pedro")

# La lógica con la tupla trabaja es desde 0 hacia la izquirda. 
print(tupla[2])

indice=0

#Para imprimir todos los elementos de una tupla.
while indice<len(tupla):
    print(tupla[indice])
    indice=indice+1

#Recorriendo una tupla con for
tupla_1=(12,65,23,5,87)

for numeros in tupla_1:
    print (numeros)

#Porciones de las tuplas
tupla_2=(12,34,532,23,5,43,12,312,31)

#Imprime los valores del 0 al 5 de la tupla anterior
tupla_3=tupla_2[0:5] #Colocar el rango entre corchetes.

print(tupla_3)

# Manejo de cadenas en Python

nombre_1="Un Gato Muy Robusto"

print (nombre_1[:7])


#Listas en Python
# Tipos de datos similares a las tuplas. Pero en este caso si es posible cambiar los valores.

lista=["Sara", "Pedro", 98, 76]
lista_2=["Juan", "Castro", 89, 56]

# Contando el número de elementos de una lista.
print(len(lista))

# Recorriendo listas con for.
for item in lista:
    print(item)

# Concatenar listas.
listaf=lista+lista_2
print(listaf)

# Verificación o busqueda de un elemento en una lista.
if "Sora" in lista:
    print("Nice")
else:
    print("NoNice")

# Manejo de lista por porciones

print(listaf[1:6])

# Índices negativos en tuplas y diccionarios
# Al poner un indice negativo recorrerá la lista de atras para adelante.

print(listaf[-1])

# Diccionario en Python

diccionario={'José': 27, 'Rafael':90,'Sara':30, 'Luis':40}

print(diccionario['Rafael'])
print(len(diccionario))

# Funciones proporcionadas por Python
# Funciones dentro del lengaje que permiten la ejecución algo en especifico.

tupla_4=(2,3,4,65,6,4)

# Nos da información de qué podemos hacer con las tuplas...
# help(tupla_4)

# Función Type

x_1=True 

# type nos dice el tipo de dato 
print(type(x_1))

# str
# transforma los datos en cadenas

numero_3=10
num_2=20

print(str(numero_3)+str(num_2))

# dir
# Metodos disponibles para una determinada variable.

print (dir(tupla_4))
