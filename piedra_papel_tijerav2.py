# piedra_papel_tijera.py
# Juego simple contra la computadora: primera versión
import random
opciones = ["piedra", "papel", "tijera"]
print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")

ronda = 1
puntos_usuario = 0
puntos_pc = 0


while True:
    try:
        numero_de_rondas = int(input("¿Cuántas rondas querés jugar? "))
        if numero_de_rondas > 0:
            break
        else:
            print("Por favor, ingresá un número positivo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresá un número.")

while ronda <= numero_de_rondas:
    print(f"\nRonda {ronda}")
    print(f"Escribí tu jugada (piedra/papel/tijera).")
    jugada_usuario = input("Tu jugada: ").strip().lower()
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.") 
        continue
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")
    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel") 
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    ronda += 1
    if numero_de_rondas - ronda +1  < puntos_pc - puntos_usuario:
        break
    if numero_de_rondas - ronda +1 < puntos_usuario - puntos_pc:
        break

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")
if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")