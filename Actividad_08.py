def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

opciones = 0
a = False
while a == False:
    print("===Menu===")
    print("1. Calcular el factorial de un numero")
    print("2. Suma de los primeros n numeros naturales")
    print("3. Calcular el n-esimo numero de Fibonacci")
    print("4. Contar cuentas veces aparece una letra en una palabra")
    print("5. Invertir una cadena de texto")
    print("6. Calcular la potencia de un numero (base ^ exponente)")
    print("7. Salir del programa")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            numero = int(input("Ingrese un numero: "))
            if numero > 0:
                print(f"El factorial de {numero} es: {factorial(numero)}")
            else:
                print("El numero debe de ser positivo")

        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")