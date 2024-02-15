import json

class Genero:
    def __init__(self, id, Nombre):
        self.id = id
        self.Nombre = Nombre

def crear_genero():
    try:
        Formato = {}
        Formato["id"] = int(input("Ingrese el ID del Genero: "))
        Formato["Nombre"] = input("Ingrese el Nombre del Genero: ")
        genero_list = cargar_datos_desde_json("data/generos.json")
        genero_list.append(Genero)
        guardar_datos_en_json("data/generos.json", genero_list)
        print("Genero registrado exitosamente.")
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

def listar_generos():
    for Formato in genero_list:
        print(f"{Formato['id']} - {Formato['Nombre']}")

def menu_generos():
   while True:
        print(""" 
         ____ _____ ____ _____ ___  ____        ____  _____        ____ _____ _   _ _____ ____   ___  ____  
        / ___| ____/ ___|_   _/ _ \|  _ \      |  _ \| ____|      / ___| ____| \ | | ____|  _ \ / _ \/ ___| 
       | |  _|  _| \___ \ | || | | | |_) |     | | | |  _|       | |  _|  _| |  \| |  _| | |_) | | | \___ \ 
       | |_| | |___ ___) || || |_| |  _ <      | |_| | |___      | |_| | |___| |\  | |___|  _ <| |_| |___) |
        \____|_____|____/ |_| \___/|_| \_\     |____/|_____|      \____|_____|_| \_|_____|_| \_\\___/|____/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        """)
        print("1. Crear genero")
        print("2. Listar generos")
        print("3. Ir a Menu Principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_genero()
        elif opcion == "2":
            listar_generos()
        elif opcion == "3":
            print("¡Hasta luego!")
            pass
        
if __name__ == "__main__":
    menu_generos()

genero_list = cargar_datos_desde_json("data/formatos.json") or []