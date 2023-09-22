num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nEste es el siguiente Menú para su elección:\n")
print("1. Sumar los dos números")
print("2. Restar los numeros")
print("3. Multiplicar los dos números")


eleccion = input("Elija una opción: ")

if eleccion == '1':
    resultado = num1 + num2
    print("La suma de los dos números es: " +str(resultado))
elif eleccion == '2':
    resultado = num1 - num2
    print("La resta de los numeros es: " +str(resultado))
elif eleccion == '3':
    resultado = num1 * num2
    print("La multiplicación de los números es: " +str(resultado))
else:
    print("Opciones inválida. Porfavor, elija una de las opciones")