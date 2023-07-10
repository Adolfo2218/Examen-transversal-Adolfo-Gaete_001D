import os
import re

os.system('cls' if os.name == 'nt' else 'clear')

escenario = [[j + i * 10 for j in range(1, 11)] for i in range(10)]

asientos_vendidos = {}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_rut(rut):
    pattern = re.compile(r'^\d{1,8}[\dkK]{1}$')
    return pattern.match(rut) is not None
    
    
def mostrar_asientos_disponibles():
    print("Estado de los asientos:")
    for fila in escenario:
        for asiento in fila:
            if asiento in asientos_vendidos:
                print("X", end="\t")
            else:
                print(asiento, end="\t")
        print()

def comprar_asientos():
    mostrar_asientos_disponibles()
    asiento = int(input("Seleccione un asiento: "))
    if asiento in asientos_vendidos:
        print("El asiento no está disponible.")
    else:
        run = input("Ingrese el RUN de la persona que ocupará el asiento (sin puntos ni guiones): ")
        if not validar_rut(run):
            print("Run inválido.")
            return
        asientos_vendidos[asiento] = run
        print("La operación se ha realizado correctamente.")
        
def mostrar_listado_asistentes():
    if not asientos_vendidos:
        print("No se han vendido asientos aún.")
    else:
        print("*** Listado de asistentes ***")
        for asiento, run in sorted(asientos_vendidos.items(), key=lambda x: x[1]):
            print(f"--- RUN: {run} -- Asiento: {asiento} ---")
            
def mostrar_ganancias_totales():
    total = 0
    acum = 0
    acum2 = 0
    acum3 = 0
    for asiento in asientos_vendidos:
        if asiento <= 20:
            acum = acum + 1
            total += 120000
        elif asiento <= 50:
            acum2 = acum2 + 1
            total += 80000
        else:
            acum3 = acum3 + 1
            total += 50000
    print("- - - - - - - - - - - - - - -")
    print(f"Platinum - - - - - - {acum}")
    print("")
    print(f"Gold - - - - - - - - {acum2}")
    print("")
    print(f"Silver - - - - - - - {acum3}")    
    print("")
    print("- - - - - - - - - - - - - - -")    
    print(f"Ganancias totales: ${total}")
    print("- - - - - - - - - - - - - - -")


while True:
    print("------------------")
    print("-----  Menú  -----")
    print("------------------")
    print("1. Comprar Entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver Listado de Asistentes")
    print("4. Ganancias totales")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        clear_console()
        comprar_asientos()
    elif opcion == "2":
        clear_console()
        mostrar_asientos_disponibles()
    elif opcion == "3":
        clear_console()
        mostrar_listado_asistentes()
    elif opcion == "4":
        clear_console()
        mostrar_ganancias_totales()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
