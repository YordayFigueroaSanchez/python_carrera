import time

def limitador(llamadas=3, periodo=10):
    def decorador(func):
        ultimas_llamadas = []
        def envoltura(*args, **kwargs):
            ahora = time.time()
            ultimas_llamadas[:] = [t for t in ultimas_llamadas if ahora - t < periodo]
            if len(ultimas_llamadas) >= llamadas:
                raise RuntimeError("Limite de llamadas excedido, intenta mas tarde")
            ultimas_llamadas.append(ahora)
            return func(*args, **kwargs)
        return envoltura
    return decorador

@limitador(llamadas=2, periodo=5)
def obtener_datos():
    print("obteniendo datos...")

# uso
obtener_datos()
time.sleep(2)
obtener_datos()
obtener_datos()