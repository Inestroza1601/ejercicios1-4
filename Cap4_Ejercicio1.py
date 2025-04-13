# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un ciclo mientras (while)
    print("PROGRAMA PARA OBTENER LA SUMA DE DIEZ CANTIDADES")
    print("-------------------------------------")

    suma = 0
    contador = 0

    while contador < 10:
        cantidad = int(input(f"Ingrese la cantidad[{contador+1}]: "))
        suma += cantidad
        contador += 1

    print("La suma de las cantidades es:", suma)
    print("-------------------------------------")
    print("Programa terminado")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()