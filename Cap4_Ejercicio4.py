# Se requiere un algoritmo para obtener la estatura promedio de un gru
# po de personas, cuyo número de miembros se desconoce, el ciclo debe 
# efectuarse siempre y cuando se tenga una estatura registrada.
# Función principal que encapsula el código del ejercicio
def main():
    # Limpieza de pantalla (si tenés el módulo limpiar, descomentá esta línea)
    import limpiar
    limpiar.main()

    print("PROGRAMA PARA CALCULAR LA ESTATURA PROMEDIO DE UN GRUPO DE PERSONAS")
    print("--------------------------------------------------------------------")

    # Inicializar variables
    SU = 0.0   # Suma de las estaturas
    C = 0      # Contador de personas

    # Leer la primera estatura
    ES = float(input("Ingrese una estatura en metros (0 para finalizar): "))

    # Mientras la estatura sea mayor que 0
    while ES > 0:
        SU += ES          # Acumular la estatura
        C += 1            # Incrementar el contador
        ES = float(input("Ingrese otra estatura en metros (0 para finalizar): "))

    # Evaluar si se ingresaron estaturas
    if C == 0:
        print("\nNo hay estaturas registradas.")
    else:
        PR = SU / C       # Calcular promedio
        print(f"\nLa estatura promedio del grupo es: {round(PR, 2)} metros")

    print("--------------------------------------------------------------------")
    print("Programa terminado con éxito.")
    input("\nPresione Enter para continuar...")

# Llamamos a la función main para ejecutar el programa
if __name__ == "__main__":
    main()
