import json

class Pelicula:
    def __init__(self, id, Nombre, Duracion, Sinopsis, Generos, Actores, Formatos):
        self.id = id
        self.Nombre = Nombre
        self.Duracion = Duracion
        self.Sinopsis = Sinopsis
        self.Generos = Generos
        self.Actores = Actores
        self.Formatos = Formatos

class actor:
    def __init__(self, Nro_Identificacion, Nombre, Apellidos):
        self.Nro_Identificacion = Nro_Identificacion
        self.Nombre = Nombre
        self.Apellidos = Apellidos

def agregar_pelicula():
    try:
        Pelicula = {}
        Pelicula["id"] = int(input("Ingrese el ID de la pelicula: "))
        Pelicula["Nombre"] = input("Ingrese el nombre de la pelicula: ")
        Pelicula["Duracion"] = input("Ingrese la duracion de la pelicula: ")
        Pelicula["Sinopsis"] = input("Ingrese la sinopsis de la pelicula: ")
        Pelicula["Generos"] = input("Ingrese el/los generos de la pelicula: ")
        Pelicula["Actores"] = input("Ingrese los actores de la pelicula: ")
        Pelicula["Formato"] = input("Ingrese el formato de la pelicula: ") 
        
        peliculas_list = cargar_datos_desde_json("data/peliculas.json")
        
        peliculas_list.append(Pelicula)
        
        guardar_datos_en_json("data/peliculas.json", peliculas_list)
        
        print("Peliculas registrado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el número de identificación.")
    except Exception as e:
        print(f"Error al registrar el camper: {e}")

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

def editar_pelicula(peliculas_list):
    id_pelicula = input("Ingrese el ID de la pelicula a actualizar: ")
    try:
        id_pelicula = int(id_pelicula)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for Pelicula in peliculas_list:
        if Pelicula["id"] == id_pelicula:
            print("Datos actuales de la pelicula:")
            print(Pelicula)
      
            Pelicula["id"] = int(input("Ingrese el ID de la pelicula: "))
            Pelicula["Nombre"] = input("Ingrese el nombre de la pelicula: ")
            Pelicula["Duracion"] = input("Ingrese la duracion de la pelicula: ")
            Pelicula["Sinopsis"] = input("Ingrese la sinopsis de la pelicula: ")
            Pelicula["Generos"] = input("Ingrese el/los generos de la pelicula: ")
            Pelicula["Actores"] = input("Ingrese los actores de la pelicula: ")
            Pelicula["Formato"] = input("Ingrese el formato de la pelicula: ") 
            guardar_datos_en_json("data/peliculas.json", peliculas_list)
            print("Pelicula actualizada exitosamente.")
            return
    else:
        print("Pelicula no encontrado.")

def eliminar_pelicula(peliculas_list):
    id_pelicula = input("Ingrese el ID de la pelicula a eliminar: ")
    try:
        id_pelicula = int(id_pelicula)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for Pelicula in peliculas_list:
        if Pelicula["Nro_Identificacion"] == id_pelicula:
            peliculas_list.remove(Pelicula)
            guardar_datos_en_json("data/peliculas.json", peliculas_list)
            print("Pelicula eliminadoa exitosamente.")
            return
    else:
        print("Pelicula no encontrada.")

def eliminar_actor(actores_list):
    id_actor = input("Ingrese el ID del Actor a eliminar: ")
    try:
        id_actor = int(id_actor)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for actor in actores_list:
        if actor["Nro_Identificacion"] == id_actor:
            actores_list.remove(actor)
            guardar_datos_en_json("data/actores.json", actores_list)
            print("Actor eliminado exitosamente.")
            return
    else:
        print("Actor no encontrada.")

def buscar_pelicula(peliculas_list):
    id_pelicula = input("Ingrese el ID de la pelicula: ")
    try:
        id_pelicula = int(id_pelicula)
    except ValueError:
        print("Número de identificación no válido. Intente de nuevo.")
        return

    for Pelicula in peliculas_list:
        if Pelicula["Nro_Identificacion"] == id_pelicula:
            print("Nombre:", Pelicula["Nombre"])
            print("Duracion:", Pelicula["Duracion"])
            print("Sinopsis:", Pelicula["Sinopsis"])
            print("Genero:", Pelicula["Genero"])
            print("Formato:", Pelicula["Formato"])
            print("Actores:", Pelicula["Actores"])
            break
    else:
        print("pelicula no encontrada.")

def listar_peliculas():
    for Pelicula in peliculas_list:
        print(f"{Pelicula['id']} - {Pelicula['Nombre']} - {Pelicula['Duracion']} - {Pelicula['Sinopsis']} - {Pelicula['Generos']} - {Pelicula['Actores']} - {Pelicula['Formatos']} ")

def menu_peliculas():
   while True:
        print(""" 
         ____ _____ ____ _____ ___  ____        ____  _____       ____  _____ _     ___ ____ _   _ _        _    ____  
        / ___| ____/ ___|_   _/ _ \|  _ \      |  _ \| ____|     |  _ \| ____| |   |_ _/ ___| | | | |      / \  / ___| 
       | |  _|  _| \___ \ | || | | | |_) |     | | | |  _|       | |_) |  _| | |    | | |   | | | | |     / _ \ \___ \ 
       | |_| | |___ ___) || || |_| |  _ <      | |_| | |___      |  __/| |___| |___ | | |___| |_| | |___ / ___ \ ___) |
        \____|_____|____/ |_| \___/|_| \_\     |____/|_____|     |_|   |_____|_____|___\____|\___/|_____/_/   \_\____/       
                                                                                                                                                                                                                                                                                                                                                                    
        """)
        print("1. Agregar pelicula")
        print("2. Editar pelicula")
        print("3. Eliminar pelicula")
        print("4. Eliminar Actor")
        print("5. Buscar pelicula")
        print("6. Listar todas las peliculas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            editar_pelicula()
        elif opcion == "3":
            eliminar_pelicula()
        elif opcion == "4":
            eliminar_actor()
        elif opcion == "5":
            buscar_pelicula()
        elif opcion == "6":
            listar_peliculas()
        elif opcion == "7":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_peliculas()

peliculas_list = cargar_datos_desde_json("data/formatos.json") or []