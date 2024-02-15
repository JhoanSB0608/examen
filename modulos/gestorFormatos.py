import json
class Formato:
    def __init__(self, id, Nombre, Nro_Copias, ValorPrestamo):
        self.id = id
        self.Nombre = Nombre
        self.Nro_Copias = Nro_Copias
        self.ValorPrestamo = ValorPrestamo

def crear_formato():
    try:
        Formato = {}
        Formato["id"] = int(input("Ingrese el ID del Formato: "))
        Formato["Nombre"] = input("Ingrese el Nombre del Formato: ")
        Formato["Nro_Copias"] = input("Ingrese el Nro de Copias: ")
        Formato["ValorPrestamo"] = input("Ingrese el Valor del Prestamo: ")
        formato_list = cargar_datos_desde_json("data/formatos.json")
        formato_list.append(Formato)
        guardar_datos_en_json("data/formatos.json", formato_list)
        print("Formato registrado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el ID.")
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

def listar_formatos():
    for Formato in formato_list:
        print(f"{Formato['id']} - {Formato['Nombre']} - {Formato['Nro_Copias']} - {Formato['ValorPrestamo']}")

def menu_formatos():
   formato_list = cargar_datos_desde_json("data/formatos.json")
   while True:
        print(""" 
         ____ _____ ____ _____ ___  ____        ____  _____       _____ ___  ____  __  __    _  _____ ___  ____  
        / ___| ____/ ___|_   _/ _ \|  _ \      |  _ \| ____|     |  ___/ _ \|  _ \|  \/  |  / \|_   _/ _ \/ ___| 
       | |  _|  _| \___ \ | || | | | |_) |     | | | |  _|       | |_ | | | | |_) | |\/| | / _ \ | || | | \___ \ 
       | |_| | |___ ___) || || |_| |  _ <      | |_| | |___      |  _|| |_| |  _ <| |  | |/ ___ \| || |_| |___) |
        \____|_____|____/ |_| \___/|_| \_\     |____/|_____|     |_|   \___/|_| \_\_|  |_/_/   \_\_| \___/|____/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        """)
        print("1. Crear formatos")
        print("2. Listar formatos")
        print("3. Ir a Menu Principal")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_formato()
        elif opcion == "2":
            listar_formatos()
        elif opcion == "3":
            print("¡Hasta luego!")
            pass

if __name__ == "__main__":
    menu_formatos()

formato_list = cargar_datos_desde_json("data/formatos.json") or []