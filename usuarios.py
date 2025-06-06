from datetime import datetime
import utilidades 
import rol_enum 

lista_de_usuarios = []

id_usuario = 1

def registrar_usuario(nombre_de_usuario,email_usuario,contraseña_de_usuario):
    global id_usuario
    
    try:
        if nombre_de_usuario == " " or nombre_de_usuario == "":
            raise ValueError("El nombre no puede estar vacio")
        if contraseña_de_usuario == " " or contraseña_de_usuario == "":
            raise ValueError("La contraseña no puede estar vacia")
        utilidades.verificar_email(email_usuario)
        contraseña_encriptada = utilidades.encriptar_contraseña(contraseña_de_usuario)
        usuario = {
            "id usuario" : id_usuario,
            "Nombre" : nombre_de_usuario,
            "Email" : email_usuario,
            "Contraseña" : contraseña_encriptada,
            "Rol" : rol_enum.Roles.USUARIO,
            "Fecha de creacion" :  datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        lista_de_usuarios.append(usuario)
        id_usuario += 1
        return print(usuario)
    except ValueError as error:
        print(f"Error: {error}")
#-------------------------------------------------------------

#Login(giuliano) - 20 lineas



















#------------------------------------------------------------

#Datos Usuario(lu) - 20 Lineas



















#-------------------------------------------------------------------

#Asignacion de roles(JuanX) - 20 Lineas