edad = int(input("Ingrese su edad "))

if edad < 4:
    precio = "gratis"
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10


print(f"El precio de su entrada es: {precio}")




