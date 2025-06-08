

def main():
    while True:
        print("\n=== SmartHome ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                usuarios.registrar_usuario(nombre, email, contraseña)

            case "2":
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                user = usuarios.iniciar_sesion(email, contraseña)
                if user:
                    if user["Rol"] == rol_enum.Roles.ADMINISTRADOR:
                        menu_admin()
                    else:
                        menu_usuario(user)

            case "3":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            case _:
                print("Opción inválida.")

main()


        
