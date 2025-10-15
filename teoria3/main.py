import utilidades as ut
import math as m
import builtins as b
import random as r
contador = 0
mi_lista_numeros = [1, 5, 10, 3.14, 7]
print(f"El promedio de {mi_lista_numeros} es {ut.promedioLista(mi_lista_numeros)}")

print(f"La suma de {mi_lista_numeros} es {ut.sumaLista(mi_lista_numeros)}")

print(f"La raíz cuadrada de 16 es {m.sqrt(16)}")
print(f"La raiz cuadrada de 100, 200, 30, 80, 25, 9 es {[m.sqrt(x) for x in [100, 200, 30, 80, 25, 9]]}")
print(f"El logaritmo natural de 20 es {m.log(20)}")

def aumentador(num):
    num += 1
    return num
aumentador(contador)
aumentador(contador)
print(f"aumentador = {contador}") #### sigue siendo 0 porque la variable global se modifica dentro de la funcion pero no fuera de esta


x = 10
def aumentadorporX(num):
    x=5
    num += x
    print(f"aumentadorPorX = {x}")
    
aumentadorporX(5) # da 10 ya que usa la x local

printOriginal = b.print
def print(texto):
    printOriginal(f"*** {texto} ***")
print("Hola mundo")
print = printOriginal
print("Hola mundo")

def suma_total(*args):
    return sum(args)
print(suma_total(1, 2, 3, 4, 5))

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_info(nombre="juan", edad=30, ciudad="chascomus")

def funcion_completa(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
funcion_completa(1, 3, 4, 5, nombre="Ana", edad=25)

lista_personas = [("Ana", 25), ("Juan", 30), ("Maria", 22) , ("Pedro", 28), ("Luis", 10)]
lista_personas_ordenada = sorted(lista_personas, key=lambda u: u[1]) 
print(lista_personas_ordenada)


lista_temperaturas = [22.5, 25.0, 19.8, 30.2, 18.5]
temperaturas_fahrenheit = list(map(lambda c: (c * 9/5) + 32, lista_temperaturas))
print(temperaturas_fahrenheit)


filtrar_primos = lambda numeros: list(filter(lambda x: all(x % i != 0 for i in range(2, int(m.sqrt(x)) + 1)) and x > 1, numeros))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primos = filtrar_primos(numeros)
print(primos)


def multiplicar(factor):
    def multiplicador():
        return r.random()* factor
    return multiplicador
print(f"multiplicar 10*random = {multiplicar(10)()}")

contadorClosure = 0
def crearContador():
    contadorClosure = 0
    def contador():
        nonlocal contadorClosure
        contadorClosure += 1
        return contadorClosure
    return contador
miContador = crearContador()
print(f"miContador ahora es = {miContador()}")
print(f"miContador ahora es = {miContador()}")
def copiar_archivo(origen, destino):
    """
    Copia el contenido de un archivo de texto a otro archivo.

    Args:
        origen (str): Ruta del archivo de origen.
        destino (str): Ruta del archivo de destino.
    """
    try:
        with open(origen, 'r', encoding='utf-8') as archivo_origen:
            contenido = archivo_origen.read()
        with open(destino, 'w', encoding='utf-8') as archivo_destino:
            archivo_destino.write(contenido)
        print(f"Archivo copiado exitosamente de {origen} a {destino}.")
    except FileNotFoundError:
        print(f"Error: El archivo {origen} no existe.")
    except IOError as e:
        print(f"Error de entrada/salida: {e}")

# Prueba la función con un archivo pequeño
copiar_archivo('archivo_origen.txt', 'archivo_destino.txt')


