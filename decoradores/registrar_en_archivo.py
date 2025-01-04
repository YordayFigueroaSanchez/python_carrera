def registrar_en_archivo(ruta_archivo):
    def descorador(func):
        def envoltura(*args, **kwargs):
            resultado = func(*args, **kwargs)
            with open(ruta_archivo, "a") as archivo:
                archivo.write(f"Llamada a {func.__name__} con argumentos {args} y {kwargs} \n")
            return resultado
        return envoltura
    return descorador

@registrar_en_archivo("decoradores/registrar_en_archivo.txt")
def multiplicar(a, b):
    return a * b

# uso
print(multiplicar(4,8))