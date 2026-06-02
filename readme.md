# Sistema Académico - Gestión de Estudiantes, Profesores, Materias y Calificaciones

## Autor

BRAHYAN FERNANDEZ MUNERA

---

## Descripción del Proyecto

Este proyecto es un Sistema Académico desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite administrar estudiantes, profesores, materias y calificaciones mediante un menú interactivo en consola.

La información se almacena en archivos JSON, permitiendo que los datos permanezcan guardados incluso después de cerrar la aplicación.

---

## Funcionalidades

* Gestión de estudiantes.
* Gestión de profesores.
* Gestión de materias.
* Gestión de calificaciones.
* Búsqueda de registros.
* Eliminación de registros.
* Estadísticas básicas del sistema.
* Persistencia de datos mediante archivos JSON.

---

## Requisitos

* Python 3.10 o superior.
* PyCharm, Visual Studio Code o cualquier editor compatible con Python.

---

## Instalación

1. Descargar o clonar el proyecto.
2. Abrir la carpeta del proyecto en PyCharm o Visual Studio Code.
3. Verificar que Python esté instalado correctamente.

Comprobar versión:

```bash
python --version
```

---

## Ejecución del Proyecto

Ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

El sistema mostrará el menú principal desde donde se podrá acceder a los diferentes módulos.

---

## Estructura del Proyecto

```text
SistemaEst/
│
├── main.py
│
├── README.md
│
├── data/
│   ├── students.json
│   ├── teachers.json
│   ├── subjects.json
│   └── grades.json
│
└── src/
    │
    ├── models/
    │   ├── student.py
    │   ├── teacher.py
    │   ├── subject.py
    │   └── grade.py
    │
    ├── services/
    │   ├── student_service.py
    │   ├── teacher_service.py
    │   ├── subject_service.py
    │   └── grade_service.py
    │
    ├── storage/
    │   └── json_storage.py
    │
    └── ui/
        ├── menu.py
        ├── teacher_menu.py
        ├── subject_menu.py
        └── grade_menu.py
```

---

## Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos (POO)
* Archivos JSON
* PyCharm / Visual Studio Code

---

## Conclusión

Este proyecto permitió aplicar conceptos fundamentales de Programación Orientada a Objetos, como clases, objetos, encapsulamiento y modularización. Además, se implementó persistencia de datos mediante archivos JSON y una arquitectura organizada en modelos, servicios, almacenamiento e interfaces de usuario.
