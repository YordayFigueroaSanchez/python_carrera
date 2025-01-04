def convertir_a_mayusculas(func):
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper() if isinstance(resultado, str) else resultado
    return envoltura

@convertir_a_mayusculas
def saludar(nombre):
    return f"Hola, {nombre}"

# uso
print(saludar("Antonio"))