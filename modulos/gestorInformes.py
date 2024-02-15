import json

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

def listar_peliculas_por_genero():
    for Pelicula in peliculas_list:
        pass
        print(f"{Pelicula['id']} - {Pelicula['Nombre']} - {Pelicula['Duracion']} - {Pelicula['Sinopsis']} - {Pelicula['Generos']} - {Pelicula['Actores']} - {Pelicula['Formatos']} ")

def listar_peliculas_por_actor():
    for Pelicula in peliculas_list:
        pass
        print(f"{Pelicula['id']} - {Pelicula['Nombre']} - {Pelicula['Duracion']} - {Pelicula['Sinopsis']} - {Pelicula['Generos']} - {Pelicula['Actores']} - {Pelicula['Formatos']} ")

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
            print("Sinopsis:", Pelicula["Sinopsis"])
            print("Actores:", Pelicula["Actores"])
            break
    else:
        print("pelicula no encontrada.")

def menu_informes():
   while True:
        print(""" 
         ____ _____ ____ _____ ___  ____        ____  _____       ___ _   _ _____ ___  ____  __  __ _____ ____  
        / ___| ____/ ___|_   _/ _ \|  _ \      |  _ \| ____|     |_ _| \ | |  ___/ _ \|  _ \|  \/  | ____/ ___| 
       | |  _|  _| \___ \ | || | | | |_) |     | | | |  _|        | ||  \| | |_ | | | | |_) | |\/| |  _| \___ \ 
       | |_| | |___ ___) || || |_| |  _ <      | |_| | |___       | || |\  |  _|| |_| |  _ <| |  | | |___ ___) |
        \____|_____|____/ |_| \___/|_| \_\     |____/|_____|     |___|_| \_|_|   \___/|_| \_\_|  |_|_____|____/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        """)
        print("1. Listar las peliculas de un genero especifico")
        print("2. Listar las peliculas donde el protagonista sea Silvester Stallone")
        print("3. Buscar pelicula y mostar la sinopsis y los actores")
        print("4. Ir a Menu Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            pass

if __name__ == "__main__":
    menu_informes()

peliculas_list = cargar_datos_desde_json("data/formatos.json") or []