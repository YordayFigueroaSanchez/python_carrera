import time
def retraso(segundos):
    def descorador(func):
        def envoltura(*args, **kwargs):
            print(f"Esperando {segundos} segundos antes de ejecutar {func.__name__}")
            time.sleep(segundos)
            return func(*args, **kwargs)
        return envoltura
    return descorador

@retraso(3)
def decir_hola():
    print("Holaa...")

# uso
decir_hola()