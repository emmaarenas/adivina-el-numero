import random 
import Adivinanza as A 
from openpyxl import load_workbook 

def menu():
    while True: 
        print("\n\033[1;30;47mMenú:\033[0m")
        try: 
            opcion = int(input("\033[1m1. Partida modo solitario\n2. Partida 2 jugadores\n3. Estadística\n4. Salir\n\033[0m"))
            if opcion == 1: 
                solitario(opcion) 
            elif opcion == 2: 
                multijugador(opcion) 
            elif opcion == 3: 
                estadistica()
            elif opcion== 4:
                print("\n\033[1;33;47m¡Gracias por jugar! Hasta luego.\033[0m")
                exit()
            else:
                print("\033[4mEsa opción no es válida.\033[0m")
        except ValueError:
            print("\033[4mPor favor, ingresa un número válido.\033[0m")

def solitario(opcion):
    print("\n\033[1;33;47m¡Has escogido el modo Solitario!\033[0m")
    dificultad = A.elegir_dificultad()
    intentos = {1:20, 2:12, 3:5}[dificultad]
    maximo = {1:1000, 2:2000, 3:3000}[dificultad]            
    numero_aleatorio = random.randint(1, maximo)
    no_acertado = [] 
    intentos_restantes = intentos 
    print(f"\n\033[1;3mPista: El número a adivinar se encuentra entre 1 y {maximo}\033[0m") 
    A.adivinar(intentos, intentos_restantes, maximo, no_acertado, numero_aleatorio, dificultad, opcion)

def multijugador(opcion):
    print("\n\033[1;33;47m¡Has escogido el modo 2 Jugadores!\033[0m")
    dificultad = A.elegir_dificultad() 
    intentos = {1:20, 2:12, 3:5}[dificultad] 
    maximo = {1:1000, 2:2000, 3:3000}[dificultad]
    no_acertado = []
    intentos_restantes = intentos
    print("\n\033[1;37;42mJugador 1: Es tu turno.\033[0m")
    numero_aleatorio = A.introducir_numero(maximo)
    print("\n\033[1;37;42mJugador 2: Es tu turno.\033[0m")
    print(f"\n\033[1;3mPista: El número a adivinar se encuentra entre 1 y {maximo}\033[0m")    
    A.adivinar(intentos, intentos_restantes, maximo, no_acertado, numero_aleatorio, dificultad, opcion)

def estadistica():
    try:
        workbook = load_workbook("./Estadistica.xlsx")
        hoja = workbook["Estadísticas"]
        if hoja.max_row > 1: 
            print("\n\033[1;33;47mEstadísticas del Juego\033[0m\n") 
            cabeceras = ["Fecha", "Jugador", "Resultado", "Dificultad", "Modo", "Intentos"]
            print(f"{cabeceras[0]:<20}{cabeceras[1]:<12}{cabeceras[2]:<10}{cabeceras[3]:<12}{cabeceras[4]:<15}{cabeceras[5]:<10}")
            print("-" * 82) 
            for fila in hoja.iter_rows(min_row = 2, values_only = True):
                fecha, jugador, resultado, dificultad, modo_juego, intentos_usados = fila
                if dificultad == 1:
                    dificultad_str = "Fácil" 
                elif dificultad == 2:
                    dificultad_str = "Medio"
                else:
                    dificultad_str = "Difícil"
                print(f"{fecha:<20}{jugador:<12}{resultado:<10}{dificultad_str:<12}{modo_juego:<15}{intentos_usados:<10}")
            while True: 
                print("\n\033[1;30;47m¿Deseas visualizar algún gráfico?\033[0m")
                try: 
                    grafico=int(input("\033[1m1. Dificultades por partidas\n2. Resultados por modo\n3. Intentos por dificultad\n4. Volver al menú principal\n\033[0m"))
                    if grafico == 1: 
                        A.grafico_dificultades()
                    elif grafico == 2: 
                        A.grafico_resultados() 
                    elif grafico == 3: 
                        A.grafico_intentos() 
                    elif grafico == 4:
                        return 
                    else: 
                        print("\033[4mEsa opción no es válida.\033[0m")
                except ValueError: 
                    print("\033[4mPor favor, ingresa un número válido.\033[0m")
        else:
            print("\033[4mNo existen datos guardados actualmente.\033[0m")
    except FileNotFoundError: 
        print("\033[4mNo existen datos guardados actualmente.\033[0m")
        return 
    
print("\n\033[1;33;47m¡Bienvenido a Adivina el Número!\033[0m")
menu()
