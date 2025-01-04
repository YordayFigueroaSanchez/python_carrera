numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)
print(numbers[2])
information = {"nombre":"Yo",
               "apellido":"Si",
               "altura":1.60,
               "edad":40}
print(information)
del(information["edad"])
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {
    "primero":{"apellido":"Si","altura":1.60,"edad":40},
    "segundo":{"apellido":"No","altura":1.40,"edad":30}
}
print(contacts)
print(contacts['primero'])
