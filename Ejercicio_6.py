#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima la suma de los cuadrados de todos los números desde 1 hasta ese 
#número utilizando un bucle while.

numero = int(input("ingrese un numero entero positivo: "))

if numero <= 0:
    print("ingrse un numero positivo")

else:
    cuadrados = 0
    contador = 1

    while contador <= numero:
        cuadrados += contador ** 2
        contador += 1
    
    print(f"la suma de los numeros desde 1 hasta {numero} es: {cuadrados}")