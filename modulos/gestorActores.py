import json

class actor:
    def __init__(self, Nro_Identificacion, Nombre, Apellidos):
        self.Nro_Identificacion = Nro_Identificacion
        self.Nombre = Nombre
        self.Apellidos = Apellidos

def registrar_actor():
    try:
        actor = {}
        actor["Nro_Identificacion"] = int(input("Ingrese el número de identificación del actor: "))
        actor["Nombre"] = input("Ingrese el Nombre del actor: ")
        actor["Rol"] = input("Ingrese el Rol del actor: ")   
        actores_list = cargar_datos_desde_json("data/actores.json")
        actores_list.append(actor)
        guardar_datos_en_json("data/actores.json", actores_list)
        print("Actor registrado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el número de identificación.")
    except Exception as e:
        print(f"Error al registrar el actor: {e}")
        
def cargar_datos_desde_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error al cargar datos desde JSON: {e}")
        return []

def guardar_datos_en_json(nombre_archivo, data):
    try:
        with open(nombre_archivo, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Datos guardados correctamente en el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo {nombre_archivo}: {e}")

def registrar_datos_actor(actores_list):
    id_actor = input("Ingrese el número de identificación: ")
    try:
        id_actor = int(id_actor)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return
    
    nombre = input("Ingrese su nombre: ")
    nuevo_actor = actor(id_actor, nombre)
    actores_list.append(nuevo_actor.__dict__)
    guardar_datos_en_json("data/actores.json", [ruta.__dict__ for ruta in actores_list])
    print("¡Datos registrados exitosamente!")

def listar_actores():
    for actor in actores_list:
        print(f"{actor['Nro_Identificacion']} - {actor['Nombre']} - {actor['Rol']}")

def menu_actores():
   actores_list = cargar_datos_desde_json("data/actores.json")
   while True:
        print(""" 
         ____ _____ ____ _____ ___  ____        ____  _____          _    ____ _____ ___  ____  _____ ____  
        / ___| ____/ ___|_   _/ _ \|  _ \      |  _ \| ____|        / \  / ___|_   _/ _ \|  _ \| ____/ ___| 
       | |  _|  _| \___ \ | || | | | |_) |     | | | |  _|         / _ \| |     | || | | | |_) |  _| \___ \ 
       | |_| | |___ ___) || || |_| |  _ <      | |_| | |___       / ___ \ |___  | || |_| |  _ <| |___ ___) |
        \____|_____|____/ |_| \___/|_| \_\     |____/|_____|     /_/   \_\____| |_| \___/|_| \_\_____|____/                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        """)
        print("1. Crear Actor")
        print("2. Listar Actores")
        print("3. Ir a Menu Principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_actor()
        elif opcion == "2":
            listar_actores()
        elif opcion == "3":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_actores()

actores_list = cargar_datos_desde_json("data/actores.json") or []