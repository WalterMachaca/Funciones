#Simulador de puntos para un torneo de videojuegos
def num():
    n = int(input("Ingrese el número de jugadores: "))
    return n

def datos():
    nombre = input("Ingrese el nombre del jugador: ")
    partidas = int(input(f"Ingrese la cantidad de partidas jugadas por {nombre}: "))
    return nombre, partidas

def puntaje(partidas):
    puntos = 0
    for i in range(1, partidas+1):
        resultado = input(F"Resultado de la partida {i}: (G=Ganar, E=Empatar, P=Perder): ").upper()
        if resultado == "G":
            puntos += 3
        elif resultado == "E":
            puntos += 1
        elif resultado == "P":
            puntos += 0
        else:
            print("Error. Ingrese una de las opciones indicadas.")
    return puntos

def tabla(jugadores):
    print("\nTabla final del torneo:")
    print("{:<15} {:<18} {:<10}".format("Jugador", "Partidas jugadas", "Puntos"))
    for jugador in jugadores:
        print("{:<15} {:<18} {:<10}".format(jugador['nombre'], jugador['partidas'], jugador['puntos']))

def obtener_ganadores(jugadores):
    max_puntos = max(jugador['puntos'] for jugador in jugadores)
    ganadores = [jugador['nombre'] for jugador in jugadores if jugador['puntos'] == max_puntos]
    return ganadores, max_puntos

def main():
    jugadores = []
    n = num()
    
    for _ in range(n):
        nombre, partidas = datos()
        puntos = puntaje(partidas)
        jugadores.append({
            'nombre': nombre,
            'partidas': partidas,
            'puntos': puntos
        })
    
    tabla(jugadores)
    
    ganadores, puntos = obtener_ganadores(jugadores)
    if len(ganadores) == 1:
        print(f"\nEl ganador del torneo es {ganadores[0]} con {puntos} puntos.")
    else:
        print(f"\nHay un empate entre: {', '.join(ganadores)} con {puntos} puntos.")

main()