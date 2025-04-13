def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    print("PROGRAMA PARA CALCULAR CUÁNTO AHORRARÁ UNA PERSONA EN UN AÑO")
    print("--------------------------------------------------------------")

    AH = 0.0  # AH = Ahorro total en el año
    M = 1     # M = Número de mes

    # Ciclo que recorre los 12 meses del año
    while M <= 12:
        # Leer la cantidad ahorrada en el mes actual
        CA = float(input(f"Ingrese la cantidad ahorrada en el mes {M}: "))
        
        # Sumar la cantidad al ahorro total
        AH += CA

        # Mostrar cuánto lleva ahorrado hasta ese mes
        print(f"El ahorro acumulado al mes {M} es: Lps. {round(AH, 2)}\n")

        # Pasar al siguiente mes
        M += 1

    # Mostrar el ahorro final al terminar el año
    print("--------------------------------------------------------------")
    print(f"El ahorro final al terminar el año es: Lps. {round(AH, 2)}")
    print("--------------------------------------------------------------")
    print("Programa terminado con éxito.")
    input("\nPresione Enter para continuar...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()