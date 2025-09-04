#EJERCICIO 6 CALIFICACION FINAL

print("CALCULADORA DE CALIFACION FINAL")
print("")
parcial = float(input("INGRESE LA NOTA DEL PRIMER PARCIAL: "))
parcial_2 = float(input("INGRESE LA NOTA DEL SEGUNDO PARCIAL: "))
parcial_3 = float(input("INGRESE LA NOTA DEL TERCER PARCIAL: "))
examen_final = float(input("INGRESE LA NOTA DEL EXAMEN FINAL: "))
trabajo_final = float(input("INGRESE LA NOTA DEL TRABAJO FINAL: "))
promedio_parciales = (parcial + parcial_2 + parcial_3) / 3 
calificacion_final = (0.55 * promedio_parciales ) + (0.30 * examen_final) + (0.15 * trabajo_final)
print(f"LA CLASIFICACION FINAL FUE CALCULADA POR LAS SIGUIENTES NOTAS: \n PARCIALES: {promedio_parciales} \n EXAMEN FINAL: {examen_final} \n TRABAJO FINAL: {trabajo_final} ")
print(f"CLASIFICACION FINAL: {calificacion_final}")
print("")
#EJERCICIO 7 
print("CAMBIO DE DOLARES A DIVISAS INTERNACIONALES")
print("")

dolares = float(input("INGRESE EL MONTO EN DOLARES (USD): "))

tasa_cop = 4016    
tasa_ars = 1360    
tasa_eur = 0.859   

pesos_colombianos = dolares * tasa_cop
pesos_argentinos = dolares * tasa_ars
euros = dolares * tasa_eur

print("EQUIVALENTE EN PESOS COLOMBIANOS (COP):", pesos_colombianos)
print("EQUIVALENTE EN PESOS ARGENTINOS (ARS):", pesos_argentinos)
print("EQUIVALENTE EN EUROS (EUR):", euros)
print("")
#EJERCICIO 8

print("CALCULADORA DE GASOLINA")
print("")

distancia = float(input("INGRESE LA DISTANCIA EN KM "))
precio_litro = float(input("INGRESE EL PRECIO DE LA GASOLINA POR LITRO "))

litros = (distancia * 8) / 100
costo = litros * precio_litro
horas = distancia / 90

print("LITROS NECESARIOS:", litros)
print("COSTO DEL VIAJE:", costo)
print("TIEMPO ESTIMADO EN HORAS: ", horas)