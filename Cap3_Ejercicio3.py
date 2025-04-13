# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL REGALO IDEAL PARA EL DIA DEL AMOR Y LA AMISTAD
    print("PROGRAMA PARA DETERMINAR EL REGALO IDEAL PARA EL DIA DEL AMOR Y LA AMISTAD")
    print("------------------------------------------------")

    # Solicitamos al usuario su presupuesto
    presupuesto = float(input("Ingrese su presupuesto disponible (Lps.): "))

    # Analizamos el presupuesto y determinamos un regalo adecuado
    if 0 < presupuesto <= 10:
        print("\nEl regalo ideal para su ser querido es una tarjeta")
    elif 10 < presupuesto <= 100:
        print("\nEl regalo ideal para su ser querido es una caja de chocolates")
    elif 100 < presupuesto <= 250:
        print("\nEl regalo ideal para su ser querido es un ramo de flores")
    elif presupuesto > 250:
        print("\nEl regalo ideal para su ser querido es un anillo")
    else:
        print("\nNo se puede determinar un regalo con el presupuesto ingresado")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    input("Presione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
