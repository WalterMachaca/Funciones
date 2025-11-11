def saludar_usuario(nombre, hora_del_dia="tardes"):
    saludo=print("¡Buenas", hora_del_dia, nombre,"!")
    return saludo
print(saludar_usuario("Juan"))            # Usa "tardes" por defecto
print(saludar_usuario("Luis", "noches")) # Usa "noches"