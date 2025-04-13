# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()
    # PROGRAMA PARA OBTENER LA SUMA DE DIEZ CANTIDADES UTILIZANDO UN CICLO FOR
    print("PROGRAMA PARA OBTENER LA SUMA DE DIEZ CANTIDADES UTILIZANDO UN CICLO FOR")
    print("------------------------------------------------------------")

    acumulador = 0
    for i in range(10):
        cantidad = float(input(f"Ingrese la cantidad {i + 1}: "))
        acumulador += cantidad

    print("La suma de las diez cantidades es:", acumulador)
    print("------------------------------------------------------------")
    print("Fin del programa")
    input("Presione Enter para continuar...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()