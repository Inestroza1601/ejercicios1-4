# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL SUELDO SEMANAL DE UN TRABAJADOR
    print("PROGRAMA PARA DETERMINAR EL SUELDO SEMANAL DE UN TRABAJADOR")
    print("---------------------------------------------------------")

    # Definimos las variables
    horas = float(input("Ingrese la cantidad de horas trabajadas: "))
    pago = float(input("Ingrese el pago por hora: "))

    # Realizamos los cálculos
    if horas > 40:
        # Calcular horas extra
        horasExtra = horas - 40
        pagoExtra = pago * 2  # Pago doble por las horas extra
        sueldo = (40 * pago) + (horasExtra * pagoExtra)
    else:
        sueldo = horas * pago

    # Mostramos los resultados
    print(f"\nEl sueldo semanal del trabajador es: {sueldo:.2f} Lps.")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
