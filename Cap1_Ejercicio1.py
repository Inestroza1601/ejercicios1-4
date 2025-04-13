import os

# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()

    # PROGRAMA PARA DETERMINAR EL VOLUMEN DE UNA CAJA
    print("PROGRAMA PARA DETERMINAR EL VOLUMEN DE UNA CAJA")
    print("------------------------------------------------")

    # Definimos variables
    a = float(input("Ingrese la altura de la caja: "))
    b = float(input("Ingrese la base de la caja: "))
    c = float(input("Ingrese la profundidad de la caja: "))

    # Calculamos el volumen
    volumen = a * b * c

    # Mostramos el resultado
    print("\nEl volumen de la caja es:", volumen, "cm^3")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Asegúrate de llamar a la función main() si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
