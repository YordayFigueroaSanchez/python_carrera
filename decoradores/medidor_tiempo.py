import time
def medidor_tiempo(func):
        def envoltura(*args, **kwargs):
            inicio = time.perf_counter()
            resultado = func(*args, **kwargs)
            fin = time.perf_counter()
            print(f"Tiempo de ejecucion : {fin-inicio:.4f} segundos ")
            return resultado
        return envoltura

@medidor_tiempo
def funcion_lenta():
    time.sleep(2)
    return "Terminado..."

# uso
print(funcion_lenta())