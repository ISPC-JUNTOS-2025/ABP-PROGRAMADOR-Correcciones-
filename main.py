import usuarios
import dispositivos
import automatizaciones

def menu_usuario(user):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Consultar datos personales")
        print("2. Activar automatización")
        print("3. Consultar dispositivos")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                usuarios.consultar_datos_personales(user["Email"])
            case "2":
                automatizaciones.menu_automatizaciones()
            case "3":
                dispositivos.listardispositivos()
            case "4":
                break
            case :
                print("Opción inválida")

def menu_admin():
    while True:
        print("\n--- Menú Admin ---")
        print("1. Consultar automatizaciones")
        print("2. Gestionar dispositivos")
        print("3. Cambiar rol a usuarios")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                automatizaciones.consultar_automatizaciones_activas()
            case "2":
                menu_gestion_dispositivos()
            case "3":
                nuevo_rol = input("Ingrese el nombre del usuario: ")
                usuarios.cambiar_rol_usuario(nuevorol)
            case "4":
                break
            case :
                print("Opción inválida")
