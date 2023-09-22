hora = input("Ingrese una hora en formato HH:MM: ")


horas, minutos = hora.split(":")


hora_conversion = float(horas) + float(minutos) / 60

if 7.0 <= hora_conversion <= 8.0:
    print("Es hora del desayuno.")
elif 12.0 <= hora_conversion <= 13.0:
    print("Es hora del almuerzo.")
elif 18.0 <= hora_conversion <= 19.0:
    print("Es hora de la cena.")
else:
    print("No es hora de comer.")