nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
edad = int(input("INGRESE SU EDAD: "))
promedio_general = float(input("INGRESE EL PROMEDIO GENERAL: "))
ingresos_familiares = float(input("INGRESE LOS INGRESOS FAMILIARES MENSUALES: "))
validez = True
if edad <= 0 or edad >100:
    validez = False
    print('ERROR: INGRESE UNA EDAD VALIDA')
if promedio_general < 0 or promedio_general > 10:
    validez = False
    print('ERROR: INGRESE UN PROMEDIO VALIDO')
if ingresos_familiares < 0:
    validez = False
    print('ERROR: INGRESE UN PROMEDIO VALIDO')


