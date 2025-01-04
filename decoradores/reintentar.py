import time
import random
def reintentar(intentos=3, retraso=1, excepcion=Exception):
    def decorador(func):
        def envoltura(*args, **kwargs):
            intentos_realizados = 0
            while intentos_realizados < intentos:
                try:
                    return func(*args, **kwargs)
                except excepcion as e:
                    intentos_realizados += 1
                    print(f"Intento {intentos_realizados} fallido : {e}")
                    time.sleep(retraso)
            raise Exception("Se alcanzo el numero maximo de intentos")
        return envoltura
    return decorador

@reintentar(intentos=5, retraso=2, excepcion=ValueError)
def funcion_probablemente_falle():
    if random.random() < 0.8:
        raise ValueError("Fallo aleatorio")
    return "Exito"

# uso
print(funcion_probablemente_falle())