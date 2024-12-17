#Escribe un programa que solicite al usuario dos números enteros 
#positivos y luego imprima 
#todos los números entre ellos (inclusive) utilizando un bucle while.

numero1 = int(input("ingrese numeros entero: "))
numero2 = int(input("ingrese el segundo numeros entero: "))

if numero1 <= 0 or numero2 <= 0:
    print("los numeros tienen que ser enteros")

else:
    inicio = min(numero1, numero2)
    fin = max(numero1, numero2)
    contador = inicio


while contador <= fin:
    print(contador)
    contador += 1
    