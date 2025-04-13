# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL ÁREA DE UN RECTÁNGULO
    print("PROGRAMA PARA DETERMINAR EL AREA DE UN RECTANGULO")
    print("------------------------------------------------")

    # Definimos variables
    b = float(input("Ingrese la base del rectángulo (cm): "))
    h = float(input("Ingrese la altura del rectángulo (cm): "))

    # Calculamos el área
    area = b * h

    # Mostramos el resultado
    print("\nEl área del rectángulo es:", area, "cm^2")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
