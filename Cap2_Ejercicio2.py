# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA CALCULAR EL PAGO POR LA ENTREGA DE LECHE
    print("PROGRAMA PARA CALCULAR EL PAGO POR LA ENTREGA DE LECHE")
    print("-----------------------------------------------")

    # Definimos la constante GALON (3.785 litros por galón)
    GALON = 3.785

    # Pedimos al usuario que ingrese los datos
    litros = float(input("Ingrese la cantidad de litros de leche: "))
    precio = float(input("Ingrese el precio por galón (Lps.): "))

    # Realizamos los cálculos
    galones = litros / GALON
    pago = galones * precio

    # Mostramos el resultado
    print(f"\nEl pago por la entrega de leche es: {pago:.2f} Lps.")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
