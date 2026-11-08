# UTN-TUPaD-MS2-TPI
Repositorio para seguimiento y entrega del Trabajo Integrador de Metodología de Sistemas II

Integrantes:

- Fulladoza, Pablo Facundo

- Lauk, Karen Yamila

- Noguera Ríos, Joana Soledad

1. Objetivo del trabajo
Evaluar la aplicación integrada de los contenidos de Metodología de Sistemas II mediante el
análisis y mejora de un sistema de software. El trabajo debe evidenciar la diferencia entre
calidad externa e interna, identificar deuda técnica, reconocer code smells, aplicar principios
SOLID y Clean Code, ejecutar refactorings seguros y realizar una revisión técnica profesional del
código producido.

### 2. Enfoque general 
- No se busca construir un sistema grande, sino analizar y mejorar profesionalmente un modulo
acotado.
- La funcionalidad visible puede ser simple; la complejidad esperada esta en el diagnostico, las
decisiones de diseño y la evidencia técnica.
- El equipo debe mostrar una versión inicial y una versión mejorada, justificando que el
comportamiento externo se mantiene o mejora sin introducir regresiones.
- La cátedra puede solicitar defensa individual para verificar autoría, comprensión y participación
real.

### 3. Caso de trabajo sugerido
**Caso sugerido:** Sistema de Gestión de Solicitudes Académicas. El sistema permite registrar
solicitudes de estudiantes, clasificarlas por tipo, prioridad y estado, asignar un responsable,
consultar solicitudes y generar un reporte simple. 
- Entidades mínimas sugeridas: Solicitud, Estudiante/Usuario, Responsable/Area y Estado.
- Casos de uso mínimos: registrar solicitud, cambiar estado, asignar responsable, buscar/filtrar
solicitudes y listar reporte básico.
- El equipo puede usar otro dominio equivalente, siempre que permita aplicar diagnostico de
calidad, refactoring y code review.
- Se puede tomar un proyecto previo, un modulo desarrollado en otra materia o un prototipo
construido por el equipo para este trabajo.

### 4. Requerimientos mínimos del sistema base 
- Debe contar con al menos 3 entidades o estructuras principales.
- Debe implementar al menos 4 operaciones funcionales verificables.
- Debe persistir o simular datos mediante archivo, base de datos, memoria estructurada o
repositorio equivalente.
- Debe tener una versión inicial con problemas reales de diseño o implementación que puedan
ser diagnosticados.
- Debe permitir demostrar que la versión final conserva el comportamiento externo esperado. 

## Instalación y ejecución

### Requisitos previos

Para ejecutar el proyecto se necesita:

- **Python 3.10 o superior.**
- **pip**, administrador de paquetes de Python.
- **Git**, en caso de descargar el proyecto mediante el repositorio.

La aplicación utiliza módulos incluidos en la biblioteca estándar de Python. Para ejecutar las pruebas automatizadas es necesario instalar adicionalmente `pytest`.

### 1. Descargar el proyecto

Clonar el repositorio de GitHub:

```bash
git clone https://github.com/Fulla1996/UTN-TUPaD-MS2-TPI.git
```

Ingresar al directorio del proyecto


### 2. Crear un entorno virtual (opcional, recomendado)

Para mantener aisladas las dependencias del proyecto, se recomienda crear un entorno virtual:

```bash
python -m venv venv
```

Activarlo según el sistema operativo:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

Instalar `pytest`, necesario para ejecutar las pruebas automatizadas:

```bash
pip install pytest
```

### 4. Ejecutar la aplicación

Desde el directorio donde se encuentra el archivo principal, ejecutar:

```bash
python main.py
```

Una vez iniciada la aplicación, se mostrará el menú principal, desde el cual se podrá acceder a las distintas funcionalidades de gestión de estudiantes, responsables y solicitudes.

### 5. Ejecutar las pruebas automatizadas

El proyecto incluye el archivo `test_main.py`, que contiene las pruebas unitarias desarrolladas utilizando `pytest`.

Para ejecutar todos los casos de prueba:

```bash
python -m pytest -v
```

El parámetro `-v` permite visualizar el resultado individual de cada prueba, indicando cuáles fueron aprobadas y cuáles presentaron errores.

Para ejecutar un archivo de pruebas específico:

```bash
python -m pytest -v test_main.py
```

### Estructura de archivos

Los archivos principales involucrados en la ejecución son:

```text
UTN-TUPaD-MS2-TPI/
│
├── main.py
├── test_main.py
├── Evidencia Pruebas/    (capturas de pantalla de las pruebas realizadas)
└── venv/                 (entorno virtual, opcional)
```

**Nota:** el archivo `main.py` representa el código fuente refactorizado y `test_main.py` contiene las pruebas automatizadas. Ambos deben encontrarse en el mismo directorio para que las importaciones de las pruebas funcionen correctamente.