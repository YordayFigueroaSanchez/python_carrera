#Ejemplo de iterador
my_list = [1,2,3,4]
#Obtener iterador
my_iter = iter(my_list)
#Usar el iterador
print(next(my_iter))
#Ejemplos de iterar una cadena
my_str = "Hola mundo"
iter_my_str = iter(my_str)
for char in iter_my_str:
    print(char)
#Crear un iterador para los numeros impares
limit = 10
odd_iter = iter(range(1,limit+1,2))
for num in odd_iter:
    print(num)