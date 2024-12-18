#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima la suma de los primeros n números pares utilizando un bucle while.

numero = int(input("escriba un numero entero positivo: "))

if numero <= 0:
    print("tiene que ser potivo, porfavor")

else:
    pares = 0
    contador = 0
    actual = 2

    while contador < numero:
        pares += actual 
        actual += 2
        contador += 1

print(f"la suma de los primeros {numero} numeros pares es: {pares}")