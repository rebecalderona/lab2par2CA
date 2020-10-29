## Aqui importamos las Librerias a utilizar
import sys
from timeit import default_timer as timer
from collections import Counter

##Todos los calculos a realizar

####Cuenta el numero de caracteres
def NumeroCaracteres(data):
    start = timer()
    numero_caracteres = len(data)
    end = timer()
    time = end - start
    print(f'El numero de caracteres es de: {numero_caracteres} ')
    print(f'El tiempo que se tomo en calcular el numero de caracteres es de:  {time} segundos')
    return

####Cuenta el numero de palabras
def NumeroPalabras(data):
    start = timer()
    numero_palabras = len(data.split())
    end = timer()
    time = end - start
    print(f'El numero de palabras es de: {numero_palabras} ')
    print(f'El tiempo que se tomo en calcular el numero de palabras es de:  {time} segundos')
    return

####Cuenta el numero de lineas en el archivo
def NumeroLineas(data):
    start = timer()
    numero_lineas = 0
    Lista = data.split("\n")
    for i in Lista:
        if i:
            numero_lineas += 1
    end = timer()
    time = end - start
    print(f'El numero de lineas es de: {numero_lineas} ')
    print(f'El tiempo que se tomo en calcular el numero de lineas es de:  {time} segundos')
    return

####Cuenta el numero de palabras unicas 
def NumeroPalabrasUnicas(data):
    start = timer()
    numero_palabras_unicas = len(Counter(data.split()))
    end = timer()
    time = end - start
    print(f'El numero de palabras unicas es de: {numero_palabras_unicas} ')
    print(f'El tiempo que se tomo en calcular el numero de palabras unicas es de:  {time} segundos')
    return

## END Todos los calculos a realizar

##Menu con opcciones
def Menu():
    respuesta = input("""
                        Que desea hacer?
                        A- Procesar un archivo
                        Q- Salir
                        Ingrese la letra con su seleccion:
    """)
    ## Si selecciona A o a lleva a la funcion de PreguntarArchivo()
    if respuesta == "A" or respuesta =="a":
        PreguntarArchivo()
    ## Si selecciona Q o q lleva a la funcion de Salire
    elif respuesta == "Q" or respuesta =="q":
        Salir()
    ## Si la opccion no es valida regresa al menu
    else:
        print("Debe ingresar una opcion valida")
        print("Porfavor intentelo de nuevo")
        Menu()
    
    

def PreguntarArchivo():
    NombreArchivo = input('Ingrese el nombre del archivo a procesar con su respectiva extension: ')
    ## Prueba el nombre de archivo ingresado 
    try:
        #Si el nombre de archivo es correcto entonces pasa a Analizar el archivo
        with open(NombreArchivo) as Archivo:
            Analizando(Archivo)
    ## Si el nombre de archivo ingresado no es correcto o no se puede abrir 
    ### regresa al inicio de la funcion.
    except FileNotFoundError:
        print("No se pudo abrir el archivo intentelo denuevo")
        PreguntarArchivo()


def Analizando(Archivo):
    data = Archivo.read()
    ##Lleva a la seccion de todos los calculos a realizar
    NumeroCaracteres(data)
    NumeroPalabras(data)
    NumeroLineas(data)
    NumeroPalabrasUnicas(data)
    input("Se completo el analisis del archivo presione enter para continuar...")
    Menu()
    


##FUNCION PARA SALIR    
def Salir():
    sys.exit

## INICIO DEL PROGRAMA
if __name__ == "__main__":
    print("Bienvenido")
    ##Lleva a la funcion del Menu
    Menu()
