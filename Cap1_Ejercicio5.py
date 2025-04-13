# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL CAMBIO QUE RECIBIRÁ UNA PERSONA CON CONDICIÓN
    print("PROGRAMA PARA DETERMINAR EL CAMBIO QUE RECIBIRA UNA PERSONA CON CONDICION")
    print("------------------------------------------------")

    # Definimos variables
    precio = float(input("Ingrese el precio del producto (Lps.): "))
    pago = float(input("Ingrese la cantidad de dinero con la que pagará (Lps.): "))

    # Analizamos y mostramos los resultados
    if pago < precio:
        faltante = precio - pago
        print(f"\nEl dinero que ingresó es insuficiente para pagar el producto. Le faltan: {faltante:.2f} Lps.")
    else:
        cambio = pago - precio
        print(f"\nEl cambio que recibirá es: {cambio:.2f} Lps.")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
