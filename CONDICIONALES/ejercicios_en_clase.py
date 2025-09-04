#EJERCICIO 1

nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
edad = int(input("INGRESE SU EDAD: "))
promedio_general = float(input("INGRESE EL PROMEDIO GENERAL: "))
ingresos_familiares = float(input("INGRESE LOS INGRESOS FAMILIARES MENSUALES: "))
validez = True
if edad <= 17 or edad >100:
    validez = False
    print('ERROR: INGRESE UNA EDAD VALIDA')
if promedio_general < 0 or promedio_general > 10:
    validez = False
    print('ERROR: INGRESE UN PROMEDIO VALIDO')
if ingresos_familiares < 0:
    validez = False
    print('ERROR: INGRESE UN PROMEDIO VALIDO')
if validez:
    if promedio_general < 6:
        beca = "BECA RECHAZADA"
    if promedio_general >= 6:
        if ingresos_familiares<=300000:
            beca = "BECA COMPLETA"
        elif ingresos_familiares >300000 and ingresos_familiares <=600000:
            beca = "MEDIA BECA"
        else:
            beca = "BECA RECHAZADA"
    print(f"NOMBRE Y APELLIDO: {nombre} {apellido}")
    print(f"PROMEDIO: {promedio_general}")
    print(f"INGRESOS: ${ingresos_familiares}")
    print(f"RESULTADO: {beca}")
    

