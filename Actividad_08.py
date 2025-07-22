def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n -1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1)

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
                print("El numero debe de ser mayor a 0")
        case 2:
            numero = int(input("Ingrese un numero entero: "))
            if numero > 0:
                print(f"La suma de los primeros {numero} numeros naturales es: {suma_naturales(numero)}")
            else:
                print("El numero debe de ser mayor a 0")
        case 3:
            numero = int(input("Ingrese un numero: "))
            if numero >= 0:
                print(f"El numero {numero} de la serie fibonaci es: {fibonacci(numero)}")
            else:
                print("El numero debe de ser positivo w")
        case 4:
        case 5:
        case 6:
        case 7:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")