# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA CALCULAR EL SUELDO SEMANAL DE UN TRABAJADOR
    print("PROGRAMA PARA CALCULAR EL SUELDO SEMANAL DE UN TRABAJADOR")
    print("---------------------------------------------------------")

    # Definimos las variables
    horas = float(input("Ingrese el número de horas trabajadas en la semana: "))
    pago = float(input("Ingrese el pago por hora que recibe (Lps.): "))

    # Realizamos los cálculos
    sueldo = horas * pago

    # Mostramos los resultados
    print(f"\nEl sueldo semanal del trabajador es: {sueldo:.2f} Lps.")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
