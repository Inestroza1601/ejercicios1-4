from datetime import datetime

# Función principal que encapsula el código del ejercicio
def main():
    # Limpiar la consola al ejecutar el script
    import limpiar
    limpiar.main()
    
    # PROGRAMA PARA DETERMINAR SI UNA PERSONA PUEDE VOTAR
    print("PROGRAMA PARA DETERMINAR SI UNA PERSONA PUEDE VOTAR")
    print("------------------------------------------------")

    # Definimos las variables
    fechaNacimiento = int(input("Ingrese su año de nacimiento: "))

    # Definimos la fecha actual
    fechaActual = datetime.now().year

    # Realizamos el cálculo de la edad
    edad = fechaActual - fechaNacimiento

    # Mostramos los resultados
    if edad >= 18:
        print(f"\nUsted tiene: {edad} años y puede votar en las próximas elecciones")
    else:
        print(f"\nUsted tiene: {edad} años y no puede votar en las próximas elecciones")

    # Decoramos la salida
    print("-----------------------------------------------")
    print("PROGRAMA TERMINADO CON ÉXITO")

    # Esperamos a que el usuario presione Enter para salir
    input("\nPresione Enter para salir...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
