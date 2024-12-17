#Escribe un programa que solicite al usuario un número entero positivo 
#y luego calcule la suma de todos los números divisibles por 3 
#desde 1 hasta ese número utilizando un bucle while.


numero = int(input("ingrese numero entero positivo: "))
suma = 0

if numero <= 0:
    print(F"introduce numero entero positivo")
else:
    contador = 1
    suma = 0

while contador <= numero:
    if contador % 3 == 0:
        suma += contador
    contador +=1 

print(F"numeros divisibles por 3 desde 1 hasta {numero} es: {suma}")