consumo_comida= float(input("Introduzca el consumo total en el restaurante: "))
porc_propina= float(input("¿que porcentaje de propina desea dejar al mesero?: "))

propinatotal= porc_propina*(consumo_comida/100)

print("¡Usted deberá dejar como propina " +str(propinatotal) + " soles!")