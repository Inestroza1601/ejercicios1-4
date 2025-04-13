# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA CALCULAR EL ÁREA DE UNA CIRCUNFERENCIA
    print("PROGRAMA PARA CALCULAR EL AREA DE UNA CIRCUNFERENCIA")
    print("-----------------------------------------------")

    # Definimos la constante PI
    PI = 3.1416

    # Pedimos al usuario que ingrese el radio
    radio = float(input("Ingrese el radio de la circunferencia (cm): "))

    # Calculamos el área
    area = PI * (radio ** 2)

    # Mostramos el resultado
    print(f"\nEl área de la circunferencia es: {area:.2f} cm^2")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
