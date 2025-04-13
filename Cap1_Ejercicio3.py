# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR CUÁL DE DOS CANTIDADES ES LA MAYOR
    print("PROGRAMA PARA DETERMINAR CUAL DE DOS CANTIDADES ES LA MAYOR")
    print("------------------------------------------------")

    # Definimos variables
    n1 = float(input("Ingrese la primera cantidad: "))
    n2 = float(input("Ingrese la segunda cantidad: "))

    # Analizamos y mostramos el resultado
    if n1 > n2:
        print(f"\nLa cantidad {n1} es mayor que {n2}")
    elif n1 < n2:
        print(f"\nLa cantidad {n1} es menor que {n2}")
    else:
        print(f"\nAmbas cantidades son iguales: {n1} = {n2}")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
