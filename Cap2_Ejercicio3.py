import math

# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA CALCULAR LA DISTANCIA ENTRE DOS PUNTOS
    print("PROGRAMA PARA CALCULAR LA DISTANCIA ENTRE DOS PUNTOS")
    print("-----------------------------------------------------")

    # Definimos las variables
    x1 = float(input("Ingrese el valor de la coordenada x en el punto 1: "))
    y1 = float(input("Ingrese el valor de la coordenada y en el punto 1: "))
    x2 = float(input("Ingrese el valor de la coordenada x en el punto 2: "))
    y2 = float(input("Ingrese el valor de la coordenada y en el punto 2: "))

    # Realizamos los cálculos
    x = x2 - x1
    y = y2 - y1
    distancia = math.sqrt(x**2 + y**2)

    # Mostramos los resultados
    print(f"\nLa distancia entre los puntos es: {distancia:.2f}")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
