add = lambda a, b: a + b

print(add(12,56))

multiply = lambda a,b:a*b
print(multiply(3,7))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x:x**2, numbers))
print(squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)