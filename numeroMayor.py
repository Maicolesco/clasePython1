num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))

if num1 > num2:
    print(f"El numero {num1} es mayor al {num2}")
elif num2 > num1:
    print(f"El numero {num2} es mayor al {num1}")
else:
    print(f"El numero {num1} y el numero {num2} son iguales")