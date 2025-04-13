# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL CAMBIO QUE RECIBIRÁ UNA PERSONA
    print("PROGRAMA PARA DETERMINAR EL CAMBIO QUE RECIBIRA UNA PERSONA")
    print("------------------------------------------------")

    # Definimos variables
    precio = float(input("Ingrese el precio del producto (Lps.): "))
    pago = float(input("Ingrese la cantidad de dinero con la que pagará (Lps.): "))

    # Calculamos el cambio
    cambio = pago - precio
    print("\nEl cambio que recibirá es:", cambio, "Lps.")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
