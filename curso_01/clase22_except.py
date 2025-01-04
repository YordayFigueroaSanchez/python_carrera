try:
    divisor = int(input("Ingrese el divisor : "))
    result = 100/divisor
except ZeroDivisionError as e:
    print("No se divide por zero")
    print("Error : ", e)
except ValueError as e:
    print("Error : ", e)