"""
Pruebas unitarias para main.py con pytest y patrón AAA.
Ubicar este archivo junto a main.py y ejecutar:
    python -m pytest -v
"""

from datetime import date
import pytest

from main import (
    Areas, DataManager, EstadoSolicitud, Estudiante, Prioridad,
    ProcessHandler, Responsable, Solicitud, TipoEstudiante
)


# Auxiliares para preparar datos de prueba

def crear_estudiante():
    return Estudiante("Ana Pérez", "ana.perez@example.com", TipoEstudiante.INGRESANTE)


def crear_responsable():
    return Responsable("Juan Gómez", Areas.SISTEMAS)


def crear_solicitud():
    return Solicitud(crear_estudiante(), crear_responsable(), Prioridad.MEDIA)


# ============================== ESTUDIANTE ==============================

def test_estudiante_se_crea_con_datos_validos():
    # Arrange
    nombre = "Ana Pérez"
    email = "ana@example.com"
    tipo = TipoEstudiante.INGRESANTE

    # Act
    estudiante = Estudiante(nombre, email, tipo)

    # Assert
    assert estudiante.nombre == nombre
    assert estudiante.email == email
    assert estudiante.tipo == tipo


def test_estudiante_normaliza_nombre():
    # Arrange
    nombre = "  Ana Pérez  "

    # Act
    estudiante = Estudiante(nombre, "ana@example.com", TipoEstudiante.AVANZADO)

    # Assert
    assert estudiante.nombre == "Ana Pérez"


def test_estudiante_rechaza_nombre_vacio():
    # Arrange
    nombre = "   "

    # Act / Assert
    with pytest.raises(ValueError, match="nombre no puede estar vacío"):
        Estudiante(nombre, "ana@example.com", TipoEstudiante.INGRESANTE)


def test_estudiante_normaliza_email():
    # Arrange
    email = " ANA@EXAMPLE.COM "

    # Act
    estudiante = Estudiante("Ana", email, TipoEstudiante.INGRESANTE)

    # Assert
    assert estudiante.email == "ana@example.com"


@pytest.mark.parametrize("email", ["", " ", "ana", "ana@", "@example.com", "ana@example"])
def test_estudiante_rechaza_email_invalido(email):
    # Arrange
    nombre = "Ana"

    # Act / Assert
    with pytest.raises(ValueError, match="mail válido"):
        Estudiante(nombre, email, TipoEstudiante.INGRESANTE)


def test_estudiante_str():
    # Arrange
    estudiante = crear_estudiante()

    # Act
    resultado = str(estudiante)

    # Assert
    assert "Ana Pérez" in resultado
    assert "ana.perez@example.com" in resultado
    assert "Ingresante" in resultado


# ============================== RESPONSABLE ==============================

def test_responsable_se_crea_con_datos_validos():
    # Arrange
    nombre = "Juan Gómez"
    area = Areas.SISTEMAS

    # Act
    responsable = Responsable(nombre, area)

    # Assert
    assert responsable.nombre == nombre
    assert responsable.area == area


def test_responsable_normaliza_nombre():
    # Arrange
    nombre = "  Juan Gómez  "

    # Act
    responsable = Responsable(nombre, Areas.ALUMNADO)

    # Assert
    assert responsable.nombre == "Juan Gómez"


def test_responsable_rechaza_nombre_vacio():
    # Arrange
    nombre = " "

    # Act / Assert
    with pytest.raises(ValueError, match="nombre no puede estar vacío"):
        Responsable(nombre, Areas.SISTEMAS)


def test_responsable_str():
    # Arrange
    responsable = crear_responsable()

    # Act
    resultado = str(responsable)

    # Assert
    assert "Juan Gómez" in resultado
    assert "Sistemas" in resultado


# ============================== SOLICITUD ==============================

def test_solicitud_se_crea_con_datos_validos():
    # Arrange
    estudiante = crear_estudiante()
    responsable = crear_responsable()
    prioridad = Prioridad.ALTA

    # Act
    solicitud = Solicitud(estudiante, responsable, prioridad)

    # Assert
    assert solicitud.estudiante is estudiante
    assert solicitud.responsable is responsable
    assert solicitud.prioridad == prioridad


def test_solicitud_inicia_pendiente():
    # Arrange
    estudiante = crear_estudiante()
    responsable = crear_responsable()

    # Act
    solicitud = Solicitud(estudiante, responsable, Prioridad.MEDIA)

    # Assert
    assert solicitud.estado == EstadoSolicitud.PENDIENTE


def test_solicitud_asigna_fecha_actual():
    # Arrange
    estudiante = crear_estudiante()
    responsable = crear_responsable()

    # Act
    solicitud = Solicitud(estudiante, responsable, Prioridad.MEDIA)

    # Assert
    assert solicitud.fecha == date.today()


@pytest.mark.parametrize(
    "estudiante,responsable,prioridad",
    [
        (None, crear_responsable(), Prioridad.ALTA),
        (crear_estudiante(), None, Prioridad.ALTA),
        (crear_estudiante(), crear_responsable(), None),
    ],
)
def test_solicitud_rechaza_datos_incompletos(estudiante, responsable, prioridad):
    # Arrange
    datos = (estudiante, responsable, prioridad)

    # Act / Assert
    with pytest.raises(ValueError, match="Datos incompletos"):
        Solicitud(*datos)


def test_solicitud_str():
    # Arrange
    solicitud = crear_solicitud()

    # Act
    resultado = str(solicitud)

    # Assert
    assert "Ana Pérez" in resultado
    assert "Juan Gómez" in resultado
    assert "Media" in resultado
    assert "Pendiente" in resultado
    assert str(date.today()) in resultado


# ============================== DATA MANAGER ==============================

def test_data_manager_inicia_con_listas_vacias():
    # Arrange
    dm = DataManager()

    # Act
    estudiantes = dm.obtener_todo(Estudiante)
    responsables = dm.obtener_todo(Responsable)
    solicitudes = dm.obtener_todo(Solicitud)

    # Assert
    assert estudiantes == []
    assert responsables == []
    assert solicitudes == []


@pytest.mark.parametrize(
    "objeto,clase",
    [
        (crear_estudiante(), Estudiante),
        (crear_responsable(), Responsable),
        (crear_solicitud(), Solicitud),
    ],
)
def test_data_manager_guarda_objeto(objeto, clase):
    # Arrange
    dm = DataManager()

    # Act
    dm.guardar(objeto)

    # Assert
    assert dm.obtener_todo(clase) == [objeto]


def test_data_manager_guarda_clase_no_registrada():
    # Arrange
    dm = DataManager()
    objeto = "dato"

    # Act
    dm.guardar(objeto)

    # Assert
    assert dm.obtener_todo(str) == [objeto]


def test_data_manager_busca_estudiante():
    # Arrange
    dm = DataManager()
    estudiante = crear_estudiante()
    dm.guardar(estudiante)

    # Act
    resultado = dm.buscar_estudiante_por_nombre("Ana Pérez")

    # Assert
    assert resultado is estudiante

def test_data_manager_busca_solicitud_por_nombre():
    # Arrange
    dm = DataManager()
    solicitud = crear_solicitud()
    dm.guardar(solicitud)

    # Act
    resultado = dm.buscar_solicitud_por_nombre_estudiante("Ana Pérez")

    assert resultado is solicitud

def test_data_manager_devuelve_none_si_no_encuentra_solicitud():
    # Arrange
    dm = DataManager()
    dm.guardar(crear_solicitud())

    # Act
    resultado = dm.buscar_solicitud_por_nombre_estudiante("Carlos")

    # Assert
    assert resultado is None

def test_data_manager_devuelve_none_si_no_hay_solicitudes(capsys):
    # Arrange
    dm = DataManager()

    # Act
    resultado = dm.buscar_solicitud_por_nombre_estudiante("Ana Pérez")
    salida = capsys.readouterr().out

    # Assert
    assert resultado is None
    assert "Lista de solicitudes vacía" in salida

def test_data_manager_busqueda_ignora_mayusculas_y_espacios():
    # Arrange
    dm = DataManager()
    estudiante = crear_estudiante()
    dm.guardar(estudiante)

    # Act
    resultado = dm.buscar_estudiante_por_nombre("  ANA PÉREZ ")

    # Assert
    assert resultado is estudiante


def test_data_manager_devuelve_none_si_no_encuentra():
    # Arrange
    dm = DataManager()
    dm.guardar(crear_estudiante())

    # Act
    resultado = dm.buscar_estudiante_por_nombre("Carlos")

    # Assert
    assert resultado is None


def test_data_manager_devuelve_none_si_lista_vacia(capsys):
    # Arrange
    dm = DataManager()

    # Act
    resultado = dm.buscar_estudiante_por_nombre("Ana")
    salida = capsys.readouterr().out

    # Assert
    assert resultado is None
    assert "Lista de estudiantes vacía" in salida


def test_data_manager_clase_desconocida_devuelve_lista_vacia():
    # Arrange
    dm = DataManager()

    # Act
    resultado = dm.obtener_todo(dict)

    # Assert
    assert resultado == []


# ============================== PROCESS HANDLER ==============================

def test_process_handler_inicializa_data_manager():
    # Arrange / Act
    handler = ProcessHandler()

    # Assert
    assert isinstance(handler.dm, DataManager)


@pytest.mark.parametrize(
    "metodo,texto",
    [
        ("menu_principal", "MENÚ PRINCIPAL"),
        ("sub_menu_estudiantes", "ESTUDIANTES"),
        ("sub_menu_responsables", "RESPONSABLES"),
        ("sub_menu_solicitudes", "SOLICITUDES"),
    ],
)
def test_process_handler_muestra_menus(metodo, texto, capsys):
    # Arrange
    handler = ProcessHandler()

    # Act
    getattr(handler, metodo)()
    salida = capsys.readouterr().out

    # Assert
    assert texto in salida


def test_list_options_muestra_elementos(capsys):
    # Arrange
    handler = ProcessHandler()
    opciones = [Prioridad.ALTA, Prioridad.MEDIA]

    # Act
    handler.list_options(opciones)
    salida = capsys.readouterr().out

    # Assert
    assert "1 -" in salida
    assert "2 -" in salida
    assert "Prioridad.ALTA" in salida
    assert "Prioridad.MEDIA" in salida


def test_list_options_informa_lista_vacia(capsys):
    # Arrange
    handler = ProcessHandler()

    # Act
    handler.list_options([])
    salida = capsys.readouterr().out

    # Assert
    assert "lista esta vacía" in salida


def test_handler_option_list_devuelve_seleccion(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    monkeypatch.setattr("builtins.input", lambda _: "2")

    # Act
    resultado = handler.handler_option_list([Prioridad.ALTA, Prioridad.MEDIA])

    # Assert
    assert resultado == Prioridad.MEDIA


def test_handler_option_list_reintenta_entrada_no_numerica(monkeypatch, capsys):
    # Arrange
    handler = ProcessHandler()
    entradas = iter(["texto", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    resultado = handler.handler_option_list([Prioridad.ALTA, Prioridad.MEDIA])
    salida = capsys.readouterr().out

    # Assert
    assert resultado == Prioridad.ALTA
    assert "Se debe ingresar un número" in salida


def test_handler_option_list_reintenta_valor_fuera_de_rango(monkeypatch, capsys):
    # Arrange
    handler = ProcessHandler()
    entradas = iter(["8", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    resultado = handler.handler_option_list([Prioridad.ALTA, Prioridad.MEDIA])
    salida = capsys.readouterr().out

    # Assert
    assert resultado == Prioridad.MEDIA
    assert "rango válido" in salida


def test_handler_option_list_lista_vacia_devuelve_none(capsys):
    # Arrange
    handler = ProcessHandler()

    # Act
    resultado = handler.handler_option_list([])
    salida = capsys.readouterr().out

    # Assert
    assert resultado is None
    assert "lista esta vacía" in salida


def test_handler_menu_principal_opcion_salir(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    monkeypatch.setattr("builtins.input", lambda _: "4")

    # Act
    handler.handler_menu_principal()

    # Assert
    assert True  # La función terminó sin error.


def test_handler_menu_principal_deriva_a_estudiantes(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    llamadas = []
    entradas = iter(["1", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(
        handler, "handler_submenu_estudiantes",
        lambda: llamadas.append("estudiantes")
    )

    # Act
    handler.handler_menu_principal()

    # Assert
    assert llamadas == ["estudiantes"]


def test_submenu_estudiantes_opcion_volver(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    monkeypatch.setattr("builtins.input", lambda _: "4")

    # Act
    handler.handler_submenu_estudiantes()

    # Assert
    assert True


def test_submenu_responsables_opcion_volver(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    monkeypatch.setattr("builtins.input", lambda _: "3")

    # Act
    handler.handler_submenu_responsables()

    # Assert
    assert True


def test_submenu_solicitudes_opcion_volver(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    monkeypatch.setattr("builtins.input", lambda _: "6")

    # Act
    handler.handler_submenu_solicitudes()

    # Assert
    assert True


def test_submenu_estudiantes_registra_estudiante(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    entradas = iter(["1", "Ana Pérez", "ana@example.com", "1", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    handler.handler_submenu_estudiantes()
    estudiantes = handler.dm.obtener_todo(Estudiante)

    # Assert
    assert len(estudiantes) == 1
    assert estudiantes[0].nombre == "Ana Pérez"
    assert estudiantes[0].email == "ana@example.com"
    assert estudiantes[0].tipo == TipoEstudiante.INGRESANTE


def test_submenu_responsables_registra_responsable(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    entradas = iter(["1", "Juan Gómez", "1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    handler.handler_submenu_responsables()
    responsables = handler.dm.obtener_todo(Responsable)

    # Assert
    assert len(responsables) == 1
    assert responsables[0].nombre == "Juan Gómez"
    assert responsables[0].area == Areas.SISTEMAS


def test_submenu_solicitudes_informa_si_faltan_datos(monkeypatch, capsys):
    # Arrange
    handler = ProcessHandler()
    entradas = iter(["1", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    handler.handler_submenu_solicitudes()
    salida = capsys.readouterr().out

    # Assert
    assert "No se encuentran estudiantes o responsables cargados" in salida
    assert handler.dm.obtener_todo(Solicitud) == []


def test_run_invoca_handler_menu_principal(monkeypatch):
    # Arrange
    handler = ProcessHandler()
    llamadas = []
    monkeypatch.setattr(
        handler, "handler_menu_principal",
        lambda: llamadas.append("invocado")
    )

    # Act
    handler.run()

    # Assert
    assert llamadas == ["invocado"]
