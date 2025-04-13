# Función principal que encapsula el código del ejercicio
def main():
    # Importar el módulo personalizado para limpiar la pantalla
    import limpiar
    limpiar.main()  # Llamada a la función que limpia la consola

    # Título del programa
    print("PROGRAMA PARA OBTENER LA EDAD PROMEDIO DE UN GRUPO DE N ALUMNOS")
    print("------------------------------------------------------------")

    # Solicitar al usuario la cantidad de alumnos
    contador = int(input("Ingrese el número de alumnos: "))

    # Inicializar la variable que acumulará la suma de las edades
    suma = 0

    # Ciclo para pedir las edades de cada alumno
    for i in range(contador):
        edad = int(input(f"Ingrese la edad del alumno {i + 1}: "))
        suma += edad  # Sumar la edad ingresada al acumulador

    # Calcular el promedio dividiendo la suma entre la cantidad de alumnos
    promedio = suma / contador

    # Mostrar el resultado redondeado a 2 decimales
    print("La edad promedio del grupo de alumnos es:", round(promedio, 2))
    print("------------------------------------------------------------")
    print("Programa terminado con éxito")

    # Pausar el programa hasta que el usuario presione Enter
    input("Presione Enter para continuar...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
