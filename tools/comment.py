from icecream import ic

# para borrar los comentarios
ic.disable()

datos_usuarios = {
    'linea01':{
        'edad':20,
        'hob': ['leer','escribir','pintar']
    },
    'linea02':{
        'edad':28,
        'hob': ['saltar','nadar','correr']
    }
}

# print(datos_usuarios)
ic(datos_usuarios)