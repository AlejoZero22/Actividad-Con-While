#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima todos los números entre 1 y ese número en orden inverso 
#utilizando un bucle while

numero = int(input("Introduce un número entero positivo: "))


if numero <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Los números desde {numero} hasta 1 en orden inverso son:")

    
    contador = numero

    while contador >= 1:
        print(contador)
        contador -= 1 
