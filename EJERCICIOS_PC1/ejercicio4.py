N = int(input("Ingrese un entero positivo: "))
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
   
    suma = (N * (N + 1)) // 2

    print("La suma desde 1 hasta {N} es: " + str(suma))