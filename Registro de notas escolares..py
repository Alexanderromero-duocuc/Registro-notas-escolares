import json
import os

ARCHIVO_JSON = "notas_estudiantes.json"

class Estudiante:
    def __init__(self, nombre_completo, matematicas, ciencias, historia):
        self.nombre_completo = nombre_completo
        self.matematicas = matematicas
        self.ciencias = ciencias
        self.historia = historia
        self.promedio = self.calcular_promedio()

    def calcular_promedio(self):
        return (self.matematicas + self.ciencias + self.historia) / 3

def main():
    estudiantes = cargar_datos()

    while True:
        mostrar_menu()

        opcion = input("Ingrese una opción: ").strip()
        print()

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            buscar_estudiante(estudiantes)
        elif opcion == "3":
            mostrar_lista_estudiantes(estudiantes)
        elif opcion == "4":
            guardar_datos(estudiantes)
            print("¡Adios!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        print()


def mostrar_menu():
    print("----- Menú -----")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante por nombre")
    print("3. Mostrar lista de estudiantes")
    print("4. Salir del programa")


def cargar_datos():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)
            estudiantes = [Estudiante(estudiante["nombre_completo"], estudiante["matematicas"],
                                      estudiante["ciencias"], estudiante["historia"]) for estudiante in datos]
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = []
    return estudiantes


def guardar_datos(estudiantes):
    datos = [{"nombre_completo": estudiante.nombre_completo,
              "matematicas": estudiante.matematicas,
              "ciencias": estudiante.ciencias,
              "historia": estudiante.historia} for estudiante in estudiantes]
    try:
        with open(ARCHIVO_JSON, "w") as archivo_json:
            json.dump(datos, archivo_json, indent=4)
    except IOError:
        print("Error al guardar los datos.")


def registrar_estudiante(estudiantes):
    print("----- Registrar estudiante -----")
    nombre_completo = input("Nombre completo del estudiante (Nombre Apellido): ").strip()
    while len(nombre_completo.split()) != 2:
        print("Ingrese correctamente el nombre y apellido.")
        nombre_completo = input("Nombre completo del estudiante (Nombre Apellido): ").strip()

    while True:
        try:
            matematicas = float(input("Nota de Matemáticas (1.0 - 7.0): ").strip())
            if not (1.0 <= matematicas <= 7.0):
                raise ValueError("La nota debe estar entre 1.0 y 7.0")
            ciencias = float(input("Nota de Ciencias (1.0 - 7.0): ").strip())
            if not (1.0 <= ciencias <= 7.0):
                raise ValueError("La nota debe estar entre 1.0 y 7.0")
            historia = float(input("Nota de Historia (1.0 - 7.0): ").strip())
            if not (1.0 <= historia <= 7.0):
                raise ValueError("La nota debe estar entre 1.0 y 7.0")
            break
        except ValueError as ve:
            print(f"Error: {ve}")

    nuevo_estudiante = Estudiante(nombre_completo, matematicas, ciencias, historia)
    estudiantes.append(nuevo_estudiante)
    print("Estudiante registrado exitosamente.")


def buscar_estudiante(estudiantes):
    print("----- Buscar estudiante por nombre -----")
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()

    encontrados = [estudiante for estudiante in estudiantes if nombre_buscar in estudiante.nombre_completo.lower()]

    if encontrados:
        print("Resultados encontrados:")
        for estudiante in encontrados:
            print(f"Nombre Completo: {estudiante.nombre_completo}, Promedio: {estudiante.promedio:.2f}")
    else:
        print("Estudiante no encontrado.")


def mostrar_lista_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print(f"Actualmente hay {len(estudiantes)} estudiantes registrados.")
        print("----- Lista de estudiantes -----")
        for idx, estudiante in enumerate(estudiantes, 1):
            print(f"{idx}. Nombre Completo: {estudiante.nombre_completo}, Promedio: {estudiante.promedio:.2f}")


if __name__ == "__main__":
    main()

