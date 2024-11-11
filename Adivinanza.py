import getpass 
import openpyxl
from datetime import datetime
from openpyxl import load_workbook 
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
from collections import Counter 
import matplotlib.pyplot as plt 

def elegir_dificultad ():
    while True: 
        try:
            dificultad = int(input("\n\033[1;30;47mElige la dificultad\033[0m\033[1m\n1. Fácil\n2. Medio\n3. Difícil\n\033[0m"))
            if (1 <= dificultad <= 3): 
                return dificultad
            else: 
                print("\033[4mLa dificultad debe estar entre 1 y 3.\033[0m")
        except ValueError: 
            print("\033[4mPor favor, ingresa un número válido.\033[0m")

def pista (numero_introducido, numero_aleatorio):
    if (numero_introducido < numero_aleatorio):
        print(f"\033[1;3mPista: El número {numero_introducido} es menor que el número a adivinar\033[0m")
    else: 
        print(f"\033[1;3mPista: El número {numero_introducido} es mayor que el número a adivinar\033[0m")

def introducir_numero (maximo):
    while True:
        try: 
            numero_aleatorio = int(getpass.getpass(f"\n\033[1mIntroduce un número entre 1 y {maximo}: \033[0m"))
            if (numero_aleatorio > maximo or numero_aleatorio < 1):
                print("\033[4mEl número está fuera del rango\033[0m") 
            else:
                return numero_aleatorio
        except ValueError: 
            print("\033[4mPor favor, ingresa un número válido.\033[0m")

def adivinar (intentos, intentos_restantes, maximo, no_acertado, numero_aleatorio, dificultad, opcion):
    while intentos_restantes > 0: 
        try: 
            numero_introducido = int(input(f"\033[1m\nTrata de adivinarlo, tienes {intentos_restantes} intentos: \033[0m"))
        except ValueError: 
            print("\033[4mPor favor, ingresa un número válido.\033[0m")
            continue 
        if (numero_introducido < 1 or numero_introducido > maximo): 
            print(f"\033[4mEl número debe estar entre 1 y {maximo}.\033[0m")
            continue 
        if numero_introducido in no_acertado: 
            print("\033[4mEse número ya lo has probado...\033[0m")
            continue 
        if numero_introducido == numero_aleatorio: 
            print("\n\033[1;33;47m¡Enhorabuena! Has acertado el número.\033[0m")
            ganado = True
            guardar(intentos, intentos_restantes, ganado, dificultad, opcion)
            return 
        else:
            no_acertado.append(numero_introducido)
            intentos_restantes -= 1 
            print(f"\033[1;37;44m¡Que pena, no lo has adivinado!\033[0m")
            pista(numero_introducido, numero_aleatorio)
    else:
        print(f"\n\033[1;37;44m¡Has perdido! El número era {numero_aleatorio}\033[0m") 
        ganado = False
        guardar(intentos, intentos_restantes, ganado, dificultad, opcion)


def crear_excel ():
    try: 
        workbook = openpyxl.load_workbook("./Estadistica.xlsx")
    except FileNotFoundError: 
        workbook = openpyxl.Workbook()
        hoja = workbook.active 
        hoja.title="Estadísticas" 
        cabeceras = ["Fecha", "Jugador", "Resultado", "Dificultad", "Modo", "Intentos"]
        for col, cabecera in enumerate(cabeceras, start=1):
            cell = hoja.cell(row=1, column=col, value=cabecera) 
            cell.font=Font(bold=True, color="FFFFFF") 
            hoja.column_dimensions[get_column_letter(col)].width=20
            cell.fill=openpyxl.styles.PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
        hoja.auto_filter.ref = "A1:F1"
        workbook.save("./Estadistica.xlsx")

def guardar (intentos, intentos_restantes, ganado, dificultad, opcion):
    nombre_jugador = str(input("\n\033[1mPor favor, escribe tu nombre: \033[0m")) 
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if ganado == True: 
        resultado = "Ganado"
    elif ganado == False:
        resultado = "Perdido"
    if opcion == 1:
        modo_juego = "Solitario"
    elif opcion == 2:
        modo_juego = "2 jugadores"
    intentos_usados = intentos - intentos_restantes
    crear_excel()
    workbook = load_workbook("./Estadistica.xlsx")
    hoja = workbook["Estadísticas"]
    siguiente_fila = hoja.max_row+1
    hoja.cell(row=siguiente_fila, column=1, value=fecha_actual)
    hoja.cell(row=siguiente_fila, column=2, value=nombre_jugador)
    hoja.cell(row=siguiente_fila, column=3, value=resultado)
    hoja.cell(row=siguiente_fila, column=4, value=dificultad)
    hoja.cell(row=siguiente_fila, column=5, value=modo_juego)
    hoja.cell(row=siguiente_fila, column=6, value=intentos_usados)
    workbook.save("./Estadistica.xlsx") 

def grafico_dificultades ():
    dificultades = []
    colores = {"Fácil":"green", "Medio":"orange", "Difícil":"red"} 
    workbook = load_workbook("./Estadistica.xlsx")
    hoja = workbook["Estadísticas"]
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        _, _, _, dificultad, _, _ = fila
        if dificultad == 1:
            dificultades.append("Fácil")
        elif dificultad == 2:
            dificultades.append("Medio")
        elif dificultad == 3:
            dificultades.append("Difícil")
    dificultad_counts = Counter(dificultades)
    plt.figure(figsize=(10,5)) 
    plt.bar(dificultad_counts.keys(), dificultad_counts.values(),
            color = [colores[dif] for dif in dificultad_counts.keys()], edgecolor="black")
    plt.title("Distribución de dificultades en el juego")
    plt.xlabel("Dificultad")  
    plt.ylabel("Número de partidas")
    plt.show()
    return

def grafico_resultados():
    resultados_modos={
        "Solitario":{"Ganado":0, "Perdido":0},
        "2 jugadores":{"Ganado":0, "Perdido":0}
    }
    workbook = load_workbook("./Estadistica.xlsx")
    hoja = workbook["Estadísticas"]
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        _, _, resultado, _, modo_juego, _ = fila
        if modo_juego in resultados_modos:
            if resultado in resultados_modos[modo_juego]:
                resultados_modos[modo_juego][resultado]+=1
    modos = list(resultados_modos.keys())
    ganados = [resultados_modos[modo]["Ganado"] for modo in modos]
    perdidos = [resultados_modos[modo]["Perdido"] for modo in modos]
    x = range(len(modos))
    plt.figure(figsize=(10, 5))
    plt.bar(x,ganados, width=0.4, label="Ganado", color="blue", align='center')
    plt.bar(x,perdidos, width=0.4, label="Perdido", color="red", align='edge')
    plt.title("Resultados de partidas por modo de juego")
    plt.xlabel("Modo de juego")
    plt.ylabel("Número de partidas")
    plt.xticks(x, modos)  
    plt.legend()
    plt.show()
    return

def grafico_intentos():
    intentos_dificultad={"Fácil": {"intentos":0, "partidas":0},
                        "Medio": {"intentos":0, "partidas":0},
                        "Difícil": {"intentos":0, "partidas":0}}
    workbook = load_workbook("./Estadistica.xlsx")
    hoja = workbook["Estadísticas"]
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        _, _, _, dificultad, _, intentos_usados = fila
        if dificultad == 1:
            intentos_dificultad["Fácil"]["intentos"]+=intentos_usados
            intentos_dificultad["Fácil"]["partidas"]+=1
        elif dificultad == 2:
            intentos_dificultad["Medio"]["intentos"]+=intentos_usados
            intentos_dificultad["Medio"]["partidas"]+=1
        elif dificultad == 3:
            intentos_dificultad["Difícil"]["intentos"]+=intentos_usados
            intentos_dificultad["Difícil"]["partidas"]+=1
    promedios = []
    etiquetas = []
    for dificultad, datos in intentos_dificultad.items():
        if datos["partidas"]>0:
            promedio_intentos = datos["intentos"]/datos["partidas"]
            promedios.append(promedio_intentos)
            etiquetas.append(f"{dificultad}({promedio_intentos:.1f}intentos)")
    plt.figure(figsize=(8,8))
    plt.pie(promedios, labels=etiquetas,  autopct="%1.1f%%", startangle=140, colors=["green","orange","red"])
    plt.title("Promedio de intentos por dificultad")
    plt.show()
    return
