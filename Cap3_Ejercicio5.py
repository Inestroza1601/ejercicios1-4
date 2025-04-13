# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()
    
    # PROGRAMA PARA CALCULAR EL COSTO DE UN ARTICULO
    print("PROGRAMA PARA CALCULAR EL COSTO DE UN ARTICULO")
    print("---------------------------------------------------")

    # Declarar variables
    precio = float(input("Ingrese el precio del artículo: "))

    # Analizar el precio y calcular el descuento y costo
    if precio >= 200:
        descuento = precio * 0.15
        costo = precio - descuento
        print("El costo total es de: Lps.", costo)
        print("El descuento aplicado es de: Lps.", descuento)
    elif precio > 100 and precio < 200:
        descuento = precio * 0.12
        costo = precio - descuento
        print("El costo total es de: Lps.", costo)
        print("El descuento aplicado es de: Lps.", descuento)
    elif precio < 100 and precio > 0:
        descuento = precio * 0.10
        costo = precio - descuento
        print("El costo total es de: Lps.", costo)
        print("El descuento aplicado es de: Lps.", descuento)
    else:
        print("El precio ingresado no es válido.")

    # Decorar la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
