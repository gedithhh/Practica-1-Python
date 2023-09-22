peso_pay= 112
peso_muñ= 75

num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

pesototal_paq= (num_payasos * peso_pay) + (num_muñecas * peso_muñ)

print("El peso total del paquete que será enviado es: " +str(pesototal_paq))