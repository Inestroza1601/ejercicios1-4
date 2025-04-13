# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()
    # PROGRAMA PARA CALCULAR EL COSTO DE ESTACIONAMIENTO
    print("PROGRAMA PARA CALCULAR EL COSTO DE ESTACIONAMIENTO")
    print("---------------------------------------------------")

    # Declarar variables
    tiempo = float(input("Ingrese el tiempo que estuvo en el estacionamiento (en horas): "))

    # Definir las tarifas
    T1 = 5  # Lempiras por las primeras 2 horas
    T2 = 4  # Lempiras por las siguientes 3 horas
    T3 = 3  # Lempiras por las siguientes 5 horas
    T4 = 2  # Lempiras por cada hora adicional después de 10 horas

    # Analizar el tiempo y calcular el costo
    if tiempo > 0 and tiempo <= 2:
        costo = tiempo * T1
        print("El costo total es de: Lps.", costo)
    elif tiempo > 2 and tiempo <= 5:
        costo = (tiempo - 2) * T2 + 10
        print("El costo total es de: Lps.", costo)
    elif tiempo > 5 and tiempo <= 10:
        costo = (tiempo - 5) * T3 + 22
        print("El costo total es de: Lps.", costo)
    elif tiempo > 10:
        costo = (tiempo - 10) * T4 + 37
        print("El costo total es de: Lps.", costo)
    else:
        print("El tiempo ingresado no es válido.")

    # Decorar la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()