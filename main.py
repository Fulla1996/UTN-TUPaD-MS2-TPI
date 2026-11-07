import os
import re
from datetime import date
from enum import Enum


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
    _mail: str
    tipo: TipoEstudiante

    def __init__(self, nombre: str, mail: str, tipo:TipoEstudiante):
        self.mail = mail
        self.nombre = nombre
        self.tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre.trim()) > 0:
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron, mail.trim()) is not None:
            self._mail = mail.trim().lower()
        else:
            raise ValueError("Debe ingresar un mail válido")


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
        if len(nombre.trim()) > 0:
            self._nombre = nombre.trim()
        else:
            raise ValueError("El nombre no puede estar vacío")


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
        estado: EstadoSolicitud
    ):
        if estudiante and responsable and prioridad and estado:
            self.estudiante = estudiante
            self.responsable = responsable
            self.prioridad = prioridad
            self.estado = estado
            self.fecha = date.today()


# Listas globales para simular base de datos
estudiantes: list[Estudiante] = []
responsables: list[Responsable] = []
solicitudes: list[Solicitud] = []


class DataManager:
    def __init__(self):
        pass

    def guardar_solicitud(self, n, e, t, p, s, r, f):
        # 1. Obsesión por primitivos & 3. Lista larga de parámetros & 4. Nombres poco descriptivos
        # 2. Anidamiento excesivo (Arrow anti-pattern)
        if n != "":
            if e != "":
                if t != "":
                    if p != "":
                        if s != "":
                            if r != "":
                                # 5. Cadenas hardcodeadas y comparaciones redundantes
                                if (
                                    (p == "Alta") == True
                                    or (p == "Media") == True
                                    or (p == "Baja") == True
                                ):
                                    # 7. Persistencia frágil mediante cadenas planas
                                    linea = (
                                        n
                                        + ","
                                        + e
                                        + ","
                                        + t
                                        + ","
                                        + p
                                        + ","
                                        + s
                                        + ","
                                        + r
                                        + ","
                                        + f
                                        + "\n"
                                    )
                                    sol.append(linea)
                                    print("Guardado correctamente")
                                else:
                                    pass  # 8. Validación silenciosa sin feedback
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

    # 4. Nombres poco descriptivos
    def actualizarProceso(self, n_busca):
        for i in range(len(sol)):
            parts = sol[i].strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Proceso"  # Cambio de estado hardcodeado
                sol[i] = ",".join(parts)

    # 4. Nombres poco descriptivos
    def actualizarCerrada(self, n_busca):
        for i in range(len(sol)):
            parts = sol[i].strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Cerrada"  # Cambio de estado hardcodeado
                sol[i] = ",".join(parts)

    # 4. Nombres poco descriptivos
    def actualizarPendiente(self, n_busca):
        for i in range(len(sol)):
            parts = sol[i].strip().split(",")
            # 5. Cadenas hardcodeadas y comparación redundante
            if (parts[0] == n_busca) == True:
                parts[4] = "Pendiente"  # Cambio de estado hardcodeado
                sol[i] = ",".join(parts)


class ProcessHandler:
    def __init__(self):
        self.dm = DataManager()

    def run(self):
        # 2. Anidamiento excesivo
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Gestión de estudiantes")
            print("2. Gestión de Responsables")
            print("3. Gestión de Solicitudes")
            print("4. Salir")

            op = input("Elija opción (1-4): ")

            if op == "1":
                while True:
                    print("\n--- SUBMENÚ: ESTUDIANTES ---")
                    print("1. Alta")
                    print("2. Listar")
                    print("3. Buscar por nombre")
                    print("4. Volver al menú principal")
                    sub_op = input("Elija opción (1-4): ")

                    if sub_op == "1":
                        # 4. Nombres poco descriptivos
                        # 6. Acoplamiento de I/O con lógica de negocio
                        n = input("Nombre: ")
                        e = input("Email: ")
                        # 7. Persistencia frágil mediante cadenas planas
                        est.append(n + "," + e)
                    elif sub_op == "2":
                        for e in est:
                            print(e)
                    elif sub_op == "3":
                        nom = input("Ingrese nombre a buscar: ")

                        for e in est:
                            if nom == e.split(",")[0]:
                                print(e)
                    elif sub_op == "4":
                        break
                    else:
                        print("Opción inválida")

            elif op == "2":
                while True:
                    print("\n--- SUBMENÚ: RESPONSABLES ---")
                    print("1. Alta")
                    print("2. Listar")
                    print("3. Volver al menú principal")
                    sub_op = input("Elija opción (1-3): ")

                    if sub_op == "1":
                        # 4. Nombres poco descriptivos
                        # 6. Acoplamiento de I/O con lógica de negocio
                        r_nom = input("Nombre del responsable: ")
                        r_area = input("Área: ")
                        ## 7. Persistencia frágil mediante cadenas planas
                        res.append(r_nom + "," + r_area)
                    elif sub_op == "2":
                        for r in res:
                            print(r)
                    elif sub_op == "3":
                        break
                    else:
                        print("Opción inválida")

            elif op == "3":
                while True:
                    print("\n--- SUBMENÚ: SOLICITUDES ---")
                    print("1. Alta")
                    print("2. Cambiar estado")
                    print("3. Asignar responsable")
                    print("4. Listar")
                    print("5. Volver al menú principal")
                    sub_op = input("Elija opción (1-5): ")

                    if sub_op == "1":
                        # 1. Obsesión por primitivos
                        # 3. Lista larga de parámetros
                        # 4. Nombres poco descriptivos

                        n = input("Nombre del estudiante: ")
                        e = input("Email: ")
                        t = input("Tipo: ")
                        p = input("Prioridad (Alta/Media/Baja): ")
                        s = input("Estado inicial: ")
                        r = input("Responsable: ")
                        f = input("Fecha: ")
                        self.dm.guardar_solicitud(n, e, t, p, s, r, f)
                    elif sub_op == "2":
                        # 4. Nombres poco descriptivos
                        nom = input("Nombre del estudiante de la solicitud: ")
                        nuevo_s = input("Nuevo estado (Pendiente/Proceso/Cerrada): ")
                        if nuevo_s == "Pendiente":
                            self.dm.actualizarPendiente(nom)
                        elif nuevo_s == "Proceso":
                            self.dm.actualizarProceso(nom)
                        elif nuevo_s == "Cerrada":
                            self.dm.actualizarCerrada(nom)
                    elif sub_op == "3":
                        # 4. Nombres poco descriptivos
                        nom = input("Nombre del estudiante de la solicitud: ")
                        nuevo_r = input("Nuevo responsable: ")
                        for i in range(len(sol)):
                            if nom == sol[i].split(",")[0]:
                                parts = sol[i].split(",")
                                parts[5] = nuevo_r
                                sol[i] = ",".join(parts)
                    elif sub_op == "4":
                        for s in sol:
                            print(s)
                    elif sub_op == "5":
                        break
                    else:
                        print("Opción inválida")

            elif op == "4":
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpción inválida. Ingrese un número del 1 al 4.")


if __name__ == "__main__":
    ph = ProcessHandler()
    ph.run()
