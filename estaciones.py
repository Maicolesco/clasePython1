from datetime import date

print("Buenos dias...Para saber a que estacion del año te encueañoras debes de ingresar la siguiente información:")
mes=int( input("Mes del año: "))
dia=int(input("día:  "))


año=int(2023)
fecha= date(año,mes,dia)
estaciones = [('invierno', date(año,  1,  1),  date(año,  3, 19)),
              ('primavera', date(año,  3, 20),  date(año,  6, 20)),
              ('verano', date(año,  6, 21),  date(año,  9, 22)),
              ('otoño', date(año,  9, 23),  date(año, 12, 21)),
              ('invierno', date(año, 12, 22),  date(año, 12, 31))]

for estacion,inicio,fin in estaciones:
    if inicio<=fecha<=fin:
        print(f"el {dia} del mes de {mes} del año {año} pertenece a la {estacion}")

