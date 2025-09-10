# 🔧 Ejercicios (Strings)
#1. Pedir una palabra y mostrarla en mayúsculas, minúsculas y *title case*.
#2. Pedir una frase y contar cuántas veces aparece cada vocal.
#3. Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando *slicing*.
#4. Verificar si una palabra **contiene** la letra `'r'`. (Tip: `in`)
palabra = input("Ingrese una palabra: ")
print("Mayúsculas:", palabra.upper())
print("Minúsculas:", palabra.lower())
print("Title Case:", palabra.title())
frase = input("Ingrese una frase: ").lower()
vocales = 'aeiou'
for vocal in vocales:
    print(f"La vocal '{vocal}' aparece {frase.count(vocal)} veces.")
frase = input("Ingrese una frase: ")
print(frase[:3], frase[-3:])
palabra = input("Ingrese una palabra: ").lower()
if 'r' in palabra:
    print("La palabra contiene la letra 'r'.")

