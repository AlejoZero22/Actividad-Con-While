#Escribe un programa que solicite al usuario dos números enteros positivos y 
#luego imprima la suma de todos los números entre ellos (inclusive) 
#utilizando un bucle while

numero_1 = int(input("introduce el primer numero entero positivo: "))
numero_2 = int(input("introduce el segundo numero entero positivo: "))

if numero_1 <= 0 or numero_2 <= 0:
    print("Por favor, introduce dos números enteros positivos.")
else:
    if numero_1 > numero_2:
        numero_1, numero_2 = numero_2, numero_1

    suma = 0
    contador = numero_1

    while contador <= numero_2:
        suma += contador
        contador += 1

    print(f"La suma de todos los números entre {numero_1} y {numero_2} (inclusive) es: {suma}")