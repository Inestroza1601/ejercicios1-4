# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA CONVERTIR METROS A PULGADAS
    print("PROGRAMA PARA CONVERTIR METROS A PULGADAS")
    print("------------------------------------------------")

    # Definimos la constante
    P = 0.0254  # 1 pulgada = 0.0254 metros

    # Definimos las variables
    metros = float(input("Ingrese la cantidad de metros que requiere: "))

    # Realizamos los cálculos
    pulgadas = metros / P

    # Mostramos los resultados
    print(f"\nLa cantidad de pulgadas que debe pedir es: {pulgadas:.2f} pulgadas")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
