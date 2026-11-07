import os
import re
from datetime import date
from enum import Enum
from typing import Any


class Prioridad(Enum):
    ALTA = "Alta"
    MEDIA = "Media"
    BAJA = "Baja"

class EstadoSolicitud(Enum):
    PENDIENTE = "Pendiente"
    PROCESO = "En Proceso"
    CERRADA = "Cerrada"

class TipoEstudiante(Enum):
    INGRESANTE = "Ingrsante"
    AVANZADO = "Avanzado"
    GRADUADO = "Graduado"

class Areas(Enum):
    SISTEMAS = "Sistemas"
    ALUMNADO = "Alumnado"
    SECRETARIA = "Secretaría"
class Estudiante:
    _nombre: str
    _email: str
    tipo: TipoEstudiante

    def __init__(self, nombre: str, email: str, tipo:TipoEstudiante):
        self.email = email
        self.nombre = nombre
        self.tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre.strip()) > 0:
            self._nombre = nombre.strip()
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, email.strip()) is not None:
            self._email = email.strip().lower()
        else:
            raise ValueError("Debe ingresar un mail válido")

    def __str__(self):
        return f"Estudiante:\n\tNombre: {self.nombre}\n\tMail: {self.email}\n\tTipo: {self.tipo.value}"


class Responsable:
    _nombre: str
    area: Areas

    def __init__(self, nombre: str, area: Areas):
        self.nombre = nombre
        self.area = area

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre.strip()) > 0:
            self._nombre = nombre.strip()
        else:
            raise ValueError("El nombre no puede estar vacío")

    def __str__(self):
        return f"Responsable:\n\tNombre: {self.nombre}\n\tArea: {self.area.value}"

class Solicitud:
    estudiante: Estudiante
    responsable: Responsable
    prioridad: Prioridad
    estado: EstadoSolicitud
    fecha: date

    def __init__(
        self,
        estudiante: Estudiante,
        responsable: Responsable,
        prioridad: Prioridad,
    ):
        if estudiante and responsable and prioridad:
            self.estudiante = estudiante
            self.responsable = responsable
            self.prioridad = prioridad
            self.estado = EstadoSolicitud.PENDIENTE
            self.fecha = date.today()
        else:
            raise ValueError("Datos incompletos para cargar la solicitud: ")
    def __str__(self):
        return f"Solicitud:\n\t{self.estudiante}\n\t{self.responsable}\n\t{self.prioridad}\n\t{self.estado.value}\n\t{self.fecha}"


# Listas globales para simular base de datos
estudiantes: list[Estudiante] = []
responsables: list[Responsable] = []
solicitudes: list[Solicitud] = []


class DataManager:
    def __init__(self):
        pass


class ProcessHandler:
    def __init__(self):
        self.dm = DataManager()

    def list_options(self, lista:list | type[Enum]):
        elementos = list(lista)
        if not elementos:
            print("La lista esta vacía.")
        for i, elemento in enumerate(elementos, start=1):
            print(f"{i} - {elemento}")


    def handler_option_list(self, lista:list | type[Enum]) -> Any:
        elementos = list(lista)
        if not elementos:
            print("La lista esta vacía")
            return None

        while True:
            try:
                option = int(input(f"Elija opción (1-{len(elementos)}): "))
            except ValueError:
                print("Se debe ingresar un número")
                continue

            if not 1 <= option <= len(elementos):
                print("Ingrese un valor dentro del rango válido")
                continue

            return elementos[option - 1]

    def handler_menu_principal(self):
        while True:
            self.menu_principal()
            option = input("Elija opción (1-4): ")
            match option:
                case "1":
                    self.handler_submenu_estudiantes()
                case "2":
                    self.handler_submenu_responsables()
                case "3":
                    self.handler_submenu_solicitudes()
                case "4":
                    break
                case _:
                    print("\nOpción inválida. Ingrese un número del 1 al 4")

    def handler_submenu_estudiantes(self):
        while True:
            self.sub_menu_estudiantes()
            option = input("Elija opción (1-4)")
            match option:
                case "1":
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    self.list_options(TipoEstudiante)
                    tipo:TipoEstudiante = self.handler_option_list(TipoEstudiante)
                    try:
                        nuevo_estudiante = Estudiante(nombre, email, tipo)
                        estudiantes.append(nuevo_estudiante)
                    except ValueError as e:
                        print("Error de validación de información de estudiantes: ", e)
                case "2":
                    self.list_options(estudiantes)
                case "3":
                    nombre = input("Nombre del estudiante a buscar: ")
                    for estudiante in estudiantes:
                        if (estudiante.nombre == nombre):
                            print(estudiante)
                        else:
                            print("Estudiante no encontrado.")
                case "4":
                    break
                case _:
                    print("\nOpción inválida. Ingrese un número del 1 al 4")

    def handler_submenu_responsables(self):
        while True:
            self.sub_menu_responsables()
            option = input("Elija opción (1-3): ")
            match option:
                case "1":
                    nombre = input("Nombre del responsable: ")
                    print("Area que se desempeña: ")
                    self.list_options(Areas)
                    area = self.handler_option_list(Areas)
                    try:
                        nuevo_responsable = Responsable(nombre, area)
                        responsables.append(nuevo_responsable)
                    except ValueError as e:
                        print("Error de validación de responsable: ", e)

                case "2":
                    self.list_options(responsables)
                case "3":
                    break
                case _:
                    print("\nOpción inválida. Ingrese un número del 1 al 3")

    def handler_submenu_solicitudes(self):
        while True:
            self.sub_menu_solicitudes()
            option = input("Elija opción (1-5): ")
            match option:
                case "1":
                    if not (estudiantes and responsables):
                        print("No se encuentran estudiantes o responsables cargados")
                        continue
                    print("Estudiante que efectua la solicitud: ")
                    self.list_options(estudiantes)
                    estudiante = self.handler_option_list(estudiantes)

                    print("\nResponsable: ")
                    self.list_options(responsables)
                    responsable = self.handler_option_list(responsables)

                    print("\nPrioridad: ")
                    self.list_options(Prioridad)
                    prioridad = self.handler_option_list(Prioridad)

                    try:
                        nueva_solicitud = Solicitud(estudiante, responsable, prioridad)
                        solicitudes.append(nueva_solicitud)
                    except ValueError as e:
                        print("Error en la validación de solicitud: ", e)
                case "2":
                    print("Seleccione la solicitud a modificar: ")
                    self.list_options(solicitudes)
                    solicitud_a_editar: Solicitud = self.handler_option_list(solicitudes)

                    print("\nSeleccione un nuevo estado")
                    self.list_options(EstadoSolicitud)
                    nuevo_estado = self.handler_option_list(EstadoSolicitud)

                    try:
                        solicitud_a_editar.estado = nuevo_estado
                    except ValueError as e:
                        print("Error en la asignación del nuevo estado: ", e)

                case "3":
                    print("Seleccione la solicitud a modificar: ")
                    self.list_options(solicitudes)
                    solicitud_a_editar: Solicitud = self.handler_option_list(solicitudes)

                    print("\nSeleccione un nuevo responsable")
                    self.list_options(responsables)
                    nuevo_responsable = self.handler_option_list(responsables)

                    try:
                        solicitud_a_editar.responsable = nuevo_responsable
                    except ValueError as e:
                        print("Error en la asignación del nuevo responsable: ", e)
                case "4":
                    self.list_options(solicitudes)
                case "5":
                    break
                case _:
                    print("\nOpción inválida. Ingrese un número del 1 al 5")

    def menu_principal(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de estudiantes")
        print("2. Gestión de Responsables")
        print("3. Gestión de Solicitudes")
        print("4. Salir")
        
    def sub_menu_estudiantes(self):
        print("\n--- SUBMENÚ: ESTUDIANTES ---")
        print("1. Alta")
        print("2. Listar")
        print("3. Buscar por nombre")
        print("4. Volver al menú principal")

    def sub_menu_responsables(self):
        print("\n--- SUBMENÚ: RESPONSABLES ---")
        print("1. Alta")
        print("2. Listar")
        print("3. Volver al menú principal")

    def sub_menu_solicitudes(self):        
        print("\n--- SUBMENÚ: SOLICITUDES ---")
        print("1. Alta")
        print("2. Cambiar estado")
        print("3. Asignar responsable")
        print("4. Listar")
        print("5. Volver al menú principal")

    def run(self):
        self.handler_menu_principal()
            


if __name__ == "__main__":
    ph = ProcessHandler()
    ph.run()
