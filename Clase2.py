# # 🔧 Ejercicios (Strings)
# #1. Pedir una palabra y mostrarla en mayúsculas, minúsculas y *title case*.
# #2. Pedir una frase y contar cuántas veces aparece cada vocal.
# #3. Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando *slicing*.
# #4. Verificar si una palabra **contiene** la letra `'r'`. (Tip: `in`)

# palabra = input("Ingrese una palabra: ")
# print("Mayúsculas:", palabra.upper())
# print("Minúsculas:", palabra.lower())
# print("Title Case:", palabra.title())



# frase = input("Ingrese una frase: ").lower()
# vocales = 'aeiou'
# for vocal in vocales:
#     print(f"La vocal '{vocal}' aparece {frase.count(vocal)} veces.")



# frase = input("Ingrese una frase: ")
# print(frase[:3], frase[-3:])
# palabra = input("Ingrese una palabra: ").lower()
# if 'r' in palabra:
#     print("La palabra contiene la letra 'r'.")

### 🔧 Ejercicios (Recorridos)
# 5. Pedir una palabra y contar cuántas vocales tiene.
# 6. Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'.
# 7. Ingresar palabras hasta escribir `FIN`; imprimir las que **empiecen y terminen** con la misma letra.

# palabra = input("Ingrese una palabra: ").lower()
# vocales = 'aeiou'
# contador = 0
# for vocal in vocales:
#     contador += palabra.count(vocal)



# print(f"La palabra '{palabra}' tiene {contador} vocales.")
# for _ in range(4):
#     palabra_2 = input("Ingrese una palabra: ").lower()
#     if 'r' in palabra_2:
#         print(palabra_2)



# palabras = []
# while True:
#     palabra = input("Ingrese una palabra (o 'FIN' para terminar): ").lower()
#     if palabra == 'fin':
#         break
#     palabras.append(palabra)
# for palabra in palabras:
#     if palabra[0] == palabra[-1]:
#         print(palabra)

# ### 🔧 Ejercicios (Funciones)
# 8. Escribir `es_palindromo(cadena)` que devuelva `True` si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).
# 9. Escribir `contar_vocales(cadena)` que retorne un diccionario con la cuenta de cada vocal.
# 10. Escribir `normalizar_palabras(frase)` que retorne una **lista** de palabras sin signos de puntuación y en minúsculas.

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "")
    return cadena.lower() == cadena[::-1].lower()
print(es_palindromo("Analana"))
print(es_palindromo("Ana"))



def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = 'aeiou'
    conteo = {vocal: 0 for vocal in vocales}
    for char in cadena:
        if char in conteo:
            conteo[char] += 1
    return conteo
print(contar_vocales("Ana"))



