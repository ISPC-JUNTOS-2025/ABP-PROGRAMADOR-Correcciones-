#Registro(axel) - 20 Lineas


















#-------------------------------------------------------------

#Login(giuliano) - 20 lineas



















#------------------------------------------------------------

#Datos Usuario(lu) - 20 Lineas



















#-------------------------------------------------------------------

#Asignacion de roles(JuanX) - 20 Lineas

def modificar_rol_usuario(usuarios, nombre_usuario, nuevo_rol):
    if nombre_usuario in usuarios:
        if nuevo_rol in ['admin', 'estandar']:
            usuarios[nombre_usuario]['rol'] = nuevo_rol
            print(f"Rol de {nombre_usuario} actualizado a {nuevo_rol}.")
        else:
            print("Rol inválido. Use 'admin' o 'estandar'.")
    else:
        print("Usuario no encontrado.")

usuarios = {
    'administrador': {'rol': 'admin'},
    'invitado1': {'rol': 'estandar'},
    'invitado2': {'rol': 'estandar'}
}

modificar_rol_usuario(usuarios, 'invitado1', 'admin')
modificar_rol_usuario(usuarios, 'administrador', 'estandar')
