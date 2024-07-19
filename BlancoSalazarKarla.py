import csv
import random

def menu_principal():
    while True:
        print("***************MENÚ***************")
        print("1.- Asignar sueldos aleatorios")
        print("2.- Clasificar sueldos")
        print("3.- Ver estadísticas")
        print("4.- Reporte de sueldos")
        print("5.- Salir del programa")
        print("**********************************")
        try:
            opcion = int(input("Seleccionar una opción (1-5): "))
            if opcion == 1:
                asignar_sueldos()
            elif opcion == 2:
                clasificar_sueldos()
            elif opcion == 3:
                ver_estadisticas()
            elif opcion == 4:
                reporte_sueldos()
            elif opcion == 5:
                salir_programa()
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Debes ingresar una opción numérica válida del 1 al 5")

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = {}

def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos[trabajador] = sueldo
    print("Sueldos fueron asignados de manera aleatoria")    

def clasificar_sueldos():
    menor_800mil = {}
    entre_800mily2millones = {}
    superior_2millones = {}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            menor_800mil[trabajador] = sueldo
        elif 800000 <= sueldo <= 2000000:
            entre_800mily2millones[trabajador] = sueldo
        else:
            superior_2millones[trabajador] = sueldo
    
    print("\nSueldos menores a $800.000: ")
    for trabajador, sueldo in menor_800mil.items():
        print(f"{trabajador}: ${sueldo:,}")

    print("\nSueldos entre $800.000 y $2.000.000: ")
    for trabajador, sueldo in entre_800mily2millones.items():
        print(f"{trabajador}: ${sueldo:,}")

    print("\nSueldos superiores a $2.000.000: ")
    for trabajador, sueldo in superior_2millones.items():
        print(f"{trabajador}: ${sueldo:,}")

def ver_estadisticas():
    sueldos_list = list(sueldos.values())
    if sueldos_list:
        sueldo_maximo = max(sueldos_list)
        sueldo_minimo = min(sueldos_list)
        promedio_sueldos = sum(sueldos_list) / len(sueldos_list)
        
        print("\nEstadísticas de los sueldos:")
        print(f"Sueldo más alto: ${sueldo_maximo:,}")
        print(f"Sueldo más bajo: ${sueldo_minimo:,}")
        print(f"Promedio de sueldos: ${promedio_sueldos:,.2f}")
    else:
        print("No hay sueldos asignados aún.")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            escritor.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")

def salir_programa():
    print("Finalizando el programa ...")
    print("Desarrollado por Karla Blanco RUT 25.469.330-8")