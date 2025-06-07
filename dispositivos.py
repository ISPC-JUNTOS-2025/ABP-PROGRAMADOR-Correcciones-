from datetime import datetime

lista_de_dispositivos = []

lista_de_automatizaciones = []

id_dispositivo = 1


def crear_dispositivo(tipo_dispositivo, nombre_dispositivo):
    global id_dispositivo

    nuevo_dispositivo = {
        "Id": id_dispositivo,
        "Tipo Dispositivo": tipo_dispositivo,
        "Nombre Dispositivo": nombre_dispositivo,
        "Estado Dispositivo": False, 
        "Fecha de Creacion": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    lista_de_dispositivos.append(nuevo_dispositivo)
    id_dispositivo += 1

    return nuevo_dispositivo


def buscar_dispositivo_por_nombre(nombre_dispositivo):
    for dispositivo in lista_de_dispositivos:
        if dispositivo["Nombre Dispositivo"].lower() == nombre_dispositivo.lower():
            print("Tipo Dispositivo:", dispositivo["Tipo Dispositivo"])
            print("Nombre Dispositivo:", dispositivo["Nombre Dispositivo"])
            print("Estado:", "Encendido" if dispositivo["Estado Dispositivo"] else "Apagado")
            print("-" * 40)

    print(f"No se encontró el dispositivo: {nombre_dispositivo}")


def listar_dispositivos():
    if not lista_de_dispositivos:
       return print("No se ha encontrado ningún dispositivo")
        
    for dispositivo in lista_de_dispositivos:
        print("Tipo Dispositivo:", dispositivo["Tipo Dispositivo"])
        print("Nombre Dispositivo:", dispositivo["Nombre Dispositivo"])
        print("Estado:", "Encendido" if dispositivo["Estado"] else "Apagado")
        print("-" * 40)  


def eliminar_dispositivo_por_nombre(nombre_dispositivo):
    for dispositivo in lista_de_dispositivos:
        if dispositivo["Nombre Dispositivo"] == nombre_dispositivo:
            lista_de_dispositivos.remove(dispositivo)
            return print(f"El dispositivo: {dispositivo["Nombre Dispositivo"]}, ha sido eliminado")

    return print(f"No se encontro el dispositivo: {nombre_dispositivo}")


def automatizacion_encender_luces():
    print("movimiento detectado en entrada principal")

    for dispositivo in lista_de_dispositivos:
        if dispositivo["Nombre Dispositivo"] == "luces".lower() and dispositivo["Estado Dispositivo"] == False:
            dispositivo["Estado Dispositivo"] = True
            return print("luces entrada principal encendidas")
            

    return print("No se han detectado luces a encender")    


