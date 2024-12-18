#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima todos los números primos menores o iguales a ese número utilizando 
#un bucle while

numero = int(input("ingrese un numero entero positivo: "))

if numero <= 0 :
    print("el numero es positivo")
else:
    primo = 2
    print(F"numero menores o iguales a {numero}:")

    while primo <= numero:
        es_primo = True
        divisor = 2

        while divisor * divisor <= primo:
            if primo % divisor == 0:
                es_primo = False
                break
            divisor += 1
        if es_primo:
            print(primo)
        primo += 1