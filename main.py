import modulos.gestorActores as gestorActores
import modulos.gestorFormatos as gestorFormatos
import modulos.gestorGeneros as gestorGeneros
import modulos.gestorInformes as gestorInformes
import modulos.gestorPeliculas as gestorPeliculas

def menu_principal():
    while True:
        print(""" 
         ____ ___ ____ _____ _____ __  __    _         ____ _____ ____ _____ ___  ____      ____  _____                          
        / ___|_ _/ ___|_   _| ____|  \/  |  / \       / ___| ____/ ___|_   _/ _ \|  _ \    |  _ \| ____|                         
        \___ \| |\___ \ | | |  _| | |\/| | / _ \     | |  _|  _| \___ \ | || | | | |_) |   | | | |  _|                           
         ___) | | ___) || | | |___| |  | |/ ___ \    | |_| | |___ ___) || || |_| |  _ <    | |_| | |___                          
        |____/___|____/ |_| |_____|_|  |_/_/   \_\    \____|_____|____/ |_| \___/|_| \_\   |____/|_____|                         
         ____  _____ _     ___ ____ _   _ _        _    ____      ____  _     ___   ____ _  ______  _   _ ____ _____ _____ ____  
        |  _ \| ____| |   |_ _/ ___| | | | |      / \  / ___|    | __ )| |   / _ \ / ___| |/ / __ )| | | / ___|_   _| ____|  _ \ 
        | |_) |  _| | |    | | |   | | | | |     / _ \ \___ \    |  _ \| |  | | | | |   | ' /|  _ \| | | \___ \ | | |  _| | |_) |
        |  __/| |___| |___ | | |___| |_| | |___ / ___ \ ___) |   | |_) | |__| |_| | |___| . \| |_) | |_| |___) || | | |___|  _ < 
        |_|   |_____|_____|___\____|\___/|_____/_/   \_\____/    |____/|_____\___/ \____|_|\_\____/ \___/|____/ |_| |_____|_| \_\
                                                                                                                                                                                                                                                                            
        """)
        print("1. Administrador de Generos")
        print("2. Administrador de Actores")
        print("3. Administrador de Formatos")
        print("4. Gestor de Peliculas")
        print("5. Gestor de Informes")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
 
        if opcion == "1":
            from modulos import gestorGeneros
            gestorGeneros.menu_generos()
        elif opcion == "2":
            from modulos import gestorActores
            gestorActores.menu_actores()
        elif opcion == "3":
            from modulos import gestorFormatos
            gestorFormatos.menu_formatos()
        elif opcion == "4":
            from modulos import gestorPeliculas
            gestorPeliculas.menu_peliculas()
        elif opcion == "5":
            from modulos import gestorPeliculas
            gestorPeliculas.menu_peliculas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
