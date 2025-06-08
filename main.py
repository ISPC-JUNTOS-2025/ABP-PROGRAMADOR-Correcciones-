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


def menu_gestion_dispositivos():
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                tipo = input("Tipo de dispositivo: ")
                nombre = input("Nombre del dispositivo: ")
                dispositivos.crear_dispositivo(tipo, nombre)
            case "2":
                dispositivos.listar_dispositivos()
            case "3":
                nombre = input("Nombre a buscar: ")
                dispositivos.buscar_dispositivo_por_nombre(nombre)
            case "4":
                nombre = input("Nombre a eliminar: ")
                dispositivos.eliminar_dispositivo_pornombre(nombre)
            case "5":
                break
            case :
                print("Opción inválida.")

