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
