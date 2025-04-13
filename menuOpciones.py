# Importa el módulo para limpiar pantalla
import limpiar
limpiar.main()

# Variable para controlar el menú principal
capitulo = 0

# Bucle principal: se ejecuta mientras el usuario no elija -1 para salir
while capitulo != -1:
    # Limpia la pantalla antes de mostrar el menú
    import limpiar
    limpiar.main()

    # Muestra el menú principal de capítulos
    print("                                                           MENU DE OPCIONES CAPITULO 1-4")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("1.- EJERCICIOS CAPITULO 1 | 2.- EJERCICIOS CAPITULO 2 | 3.- EJERCICIOS CAPITULO 3 | 4.- EJERCICIOS CAPITULO 4 | -1.- SALIR")
    print("----------------------------------------------------------------------------------------------------------------------------")

    # Solicita al usuario que seleccione una opción
    capitulo = int(input("ESCOGE UNA OPCION: "))

    # Usa estructura match para manejar la selección del capítulo
    match capitulo:
        case 1:
            # Menú de ejercicios del capítulo 1
            ejercicio = ""
            while ejercicio != "X":
                import limpiar
                limpiar.main()
                print("                                     MENU EJERCICIOS CAPITULO 1")
                print("-----------------------------------------------------------------------------------------------------")
                print("A.- EJERCICIO 1 | B.- EJERCICIO 2 | C.- EJERCICIO 3 | D.- EJERCICIO 4 | E.- EJERCICIO 5 | X.- SALIR")
                print("-----------------------------------------------------------------------------------------------------")
                ejercicio = input("ESCOGE UNA OPCION: ").upper()

                # Llama al archivo correspondiente según la opción
                match ejercicio:
                    case "A":
                        import Cap1_Ejercicio1
                        Cap1_Ejercicio1.main()
                    case "B":
                        import Cap1_Ejercicio2
                        Cap1_Ejercicio2.main()
                    case "C":
                        import Cap1_Ejercicio3
                        Cap1_Ejercicio3.main()
                    case "D":
                        import Cap1_Ejercicio4
                        Cap1_Ejercicio4.main()
                    case "E":
                        import Cap1_Ejercicio5
                        Cap1_Ejercicio5.main()
        case 2:
            # Menú de ejercicios del capítulo 2
            ejercicio = ""
            while ejercicio != "X":
                import limpiar
                limpiar.main()
                print("                                     MENU EJERCICIOS CAPITULO 2")
                print("-----------------------------------------------------------------------------------------------------")
                print("A.- EJERCICIO 1 | B.- EJERCICIO 2 | C.- EJERCICIO 3 | D.- EJERCICIO 4 | E.- EJERCICIO 5 | X.- SALIR")
                print("-----------------------------------------------------------------------------------------------------")
                ejercicio = input("ESCOGE UNA OPCION: ").upper()

                match ejercicio:
                    case "A":
                        import Cap2_Ejercicio1
                        Cap2_Ejercicio1.main()
                    case "B":
                        import Cap2_Ejercicio2
                        Cap2_Ejercicio2.main()
                    case "C":
                        import Cap2_Ejercicio3
                        Cap2_Ejercicio3.main()
                    case "D":
                        import Cap2_Ejercicio4
                        Cap2_Ejercicio4.main()
                    case "E":
                        import Cap2_Ejercicio5
                        Cap2_Ejercicio5.main()
        case 3:
            # Menú de ejercicios del capítulo 3
            ejercicio = ""
            while ejercicio != "X":
                import limpiar
                limpiar.main()
                print("                                     MENU EJERCICIOS CAPITULO 3")
                print("-----------------------------------------------------------------------------------------------------")
                print("A.- EJERCICIO 1 | B.- EJERCICIO 2 | C.- EJERCICIO 3 | D.- EJERCICIO 4 | E.- EJERCICIO 5 | X.- SALIR")
                print("-----------------------------------------------------------------------------------------------------")
                ejercicio = input("ESCOGE UNA OPCION: ").upper()

                match ejercicio:
                    case "A":
                        import Cap3_Ejercicio1
                        Cap3_Ejercicio1.main()
                    case "B":
                        import Cap3_Ejercicio2
                        Cap3_Ejercicio2.main()
                    case "C":
                        import Cap3_Ejercicio3
                        Cap3_Ejercicio3.main()
                    case "D":
                        import Cap3_Ejercicio4
                        Cap3_Ejercicio4.main()
                    case "E":
                        import Cap3_Ejercicio5
                        Cap3_Ejercicio5.main()
        case 4:
            # Menú de ejercicios del capítulo 4
            ejercicio = ""
            while ejercicio != "X":
                import limpiar
                limpiar.main()
                print("                                     MENU EJERCICIOS CAPITULO 4")
                print("-----------------------------------------------------------------------------------------------------")
                print("A.- EJERCICIO 1 | B.- EJERCICIO 2 | C.- EJERCICIO 3 | D.- EJERCICIO 4 | E.- EJERCICIO 5 | X.- SALIR")
                print("-----------------------------------------------------------------------------------------------------")
                ejercicio = input("ESCOGE UNA OPCION: ").upper()

                match ejercicio:
                    case "A":
                        import Cap4_Ejercicio1
                        Cap4_Ejercicio1.main()
                    case "B":
                        import Cap4_Ejercicio2
                        Cap4_Ejercicio2.main()
                    case "C":
                        import Cap4_Ejercicio3
                        Cap4_Ejercicio3.main()
                    case "D":
                        import Cap4_Ejercicio4
                        Cap4_Ejercicio4.main()
                    case "E":
                        import Cap4_Ejercicio5
                        Cap4_Ejercicio5.main()

# Mensaje al salir del programa
input("\nPULSA ENTER PARA SALIR DEL SISTEMA")
print("-----------------------------------------------------------")
print("\nPROGRAMA TERMINADO CON ÉXITO")