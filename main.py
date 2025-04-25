import os

def crear_archivo(nombre, contenido=""):

    with open(nombre, "w") as archivo:
        archivo.write(contenido)
    print(f"Archivo '{nombre}' creado con éxito.")

def leer_archivo(nombre):
    
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
        print(f"Contenido del archivo '{nombre}':")
        print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre}' no existe.")

def agregar_contenido(nombre, contenido):

    try:
        with open(nombre, "a") as archivo:
            archivo.write(contenido)
        print(f"Contenido agregado al archivo '{nombre}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre}' no existe.")

def eliminar_archivo(nombre):
    try:
        os.remove(nombre)
        print(f"Archivo '{nombre}' eliminado con éxito.")
    except FileNotFoundError:
        print(f"El archivo '{nombre}' no existe.")
    except PermissionError:
        print(f"No tienes permiso para eliminar el archivo '{nombre}'.")

def menu():

    while True:
        print("\nGestión de Archivos")
        print("1. Crear archivo")
        print("2. Leer archivo")
        print("3. Agregar contenido a un archivo")
        print("4. Eliminar archivo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del archivo (con extensión): ")
            contenido = input("Ingrese el contenido del archivo: ")
            crear_archivo(nombre, contenido)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del archivo a leer: ")
            leer_archivo(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Ingrese el contenido a agregar: ")
            agregar_contenido(nombre, contenido)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


menu()
