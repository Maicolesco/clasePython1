from datetime import date

print("Buenos dias...Para saber a que estacion del año te encuentras debes de ingresar la siguiente información:")
mes=int( input("Mes del año: "))
dia=int(input("día:  "))


año=int(2023)
fecha= date(año,mes,dia)
if date(año,  1,  1)<=fecha<=date(año,  3, 19):
    print(f"el {dia} del mes de {mes} del año {año} pertenece a invierno")
elif date(año,  3, 20)<=fecha<= date(año,  6, 20):
    print(f"el {dia} del mes de {mes} del año {año} pertenece a Primavera")
elif date(año,  6, 21)<=fecha<= date(año,  9, 22):
    print(f"el {dia} del mes de {mes} del año {año} pertenece a Verano")
elif date(año,  9, 23)<=fecha<= date(año, 12, 21):
    print(f"el {dia} del mes de {mes} del año {año} pertenece a Otoño")
elif date(año, 12, 22)<=fecha<= date(año, 12, 31):
    print(f"el {dia} del mes de {mes} del año {año} pertenece a invierno")
else:
    print(f"Verifique el dato ingresado")
