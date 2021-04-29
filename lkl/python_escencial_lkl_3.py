#Manipulación de archivos, lectura escritura y "append"

def crearArchivo ():
    archivo = open("datos.txt",'w')
    archivo.close()

def escribirArchivo():
    archivo = open('datos.txt', 'a')
    archivo.write('José Pancho\n')
    archivo.write('1234564\n')
    archivo_1 = str(archivo)
    print(archivo_1)
    archivo.close

def leerArchivo():
    archivo = open('datos.txt','r')
    linea = archivo.readline()

    while linea!="":
        print(linea)
        linea = archivo.readline()
    archivo.close

leerArchivo()
