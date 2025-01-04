def requerir_autenticacion(func):
    def envoltura(*args, **kwargs):
        usuario_autenticado = kwargs.get("autenticado", False)
        if not usuario_autenticado:
            raise PermissionError("Acceso denegado. Usuario no autenticado.")
        return func(*args, **kwargs)
    return envoltura

@requerir_autenticacion
def ver_datos_secretos(*args, **kwargs):
    return "Datos secretos revelados."

# uso
print(ver_datos_secretos(autenticado=False)) #Lanza un error
# print(ver_datos_secretos(autenticado=True))