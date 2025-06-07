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



def iniciar_sesion(email_usuario, contraseña_usuario):
    try:
        # Verifica que no estén vacíos
        if email_usuario.strip() == "" or contraseña_usuario.strip() == "":
            raise ValueError("El email y la contraseña no pueden estar vacíos.")

        # Buscar el usuario
        usuario_encontrado = next((u for u in lista_de_usuarios if u["Email"] == email_usuario), None)

        if not usuario_encontrado:
            raise ValueError("No se encontró un usuario con ese email.")

        # Encriptar la contraseña ingresada para compararla
        contraseña_encriptada = utilidades.encriptar_contraseña(contraseña_usuario)

        if usuario_encontrado["Contraseña"] != contraseña_encriptada:
            raise ValueError("La contraseña es incorrecta.")

        print(f"Inicio de sesión exitoso. Bienvenido, {usuario_encontrado['Nombre']}.")
        return usuario_encontrado

    except ValueError as error:
        print(f"Error: {error}")
        return None


#Login(Luciana) - 20 lineas

def consultar_datos_personales(email_usuario):
    try:
        for usuario in lista_de_usuarios:
            if email_usuario not in usuario["Email"]:
                raise ValueError("No se encontro un usuario con ese email")
            print("\n--- DATOS PERSONALES ---")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Email: {usuario['Email']}")
    except ValueError as error:
        print(f"Error: {error}")
