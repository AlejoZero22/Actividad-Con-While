#Escribe un programa que solicite al usuario un número entero positivo y 
#luego imprima los primeros n números impares utilizando un bucle while.


numero = int(input("escriba un numero entero positivo: "))

if numero <= 0:
    print("es un numero entero")

else:
    contador = 0
    actual = 1
    print(f"los primeros {numero} numeros impares son: ")

    while contador < numero:
        print(actual)
        actual += 2
        contador += 1