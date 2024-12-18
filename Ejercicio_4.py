#Escribe un programa que solicite al usuario un número entero positivo 
#y luego imprima si el número es un número de Armstrong utilizando un bucle while.

numero = int(input("ingrese un numero entero positivo: "))


if numero <= 0:
    print("introdusca el numero entero positivo")
else:
    real = numero 
    numero_digito = len(str(numero))
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma += digito ** numero_digito
        numero //= 10

    if suma == real:
        print(F"{real} es un numero armstrong.")
    else:
        print(F"{real} No es un numero armstrong.")