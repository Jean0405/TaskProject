
# Gestor de Tareas

## 1. ¿Qué hace la aplicación?

Esta aplicación es un **gestor de tareas** que permite a los usuarios agregar, listar, marcar como completadas y eliminar tareas. Además, permite importar y exportar las tareas en formato JSON.

Las funcionalidades principales son:

- **Agregar tarea**: Permite añadir nuevas tareas con un título, descripción y estado (pendiente o completada).
- **Listar tareas**: Muestra todas las tareas almacenadas en la base de datos, con su título, descripción y estado.
- **Marcar tarea como completada**: Permite marcar tareas pendientes como completadas.
- **Eliminar tareas completadas**: Elimina todas las tareas que están marcadas como completadas.
- **Importar/Exportar tareas**: Permite importar tareas desde un archivo JSON y exportarlas a un archivo JSON.

## 2. Tecnologías usadas y cómo instalarlas

### Tecnologías

- **Streamlit**: Una herramienta de Python para crear aplicaciones web interactivas.
- **SQLAlchemy**: ORM de Python para interactuar con bases de datos relacionales.
- **SQLite**: Base de datos ligera que se utiliza para almacenar las tareas.
- **JSON**: Formato para importar y exportar datos de las tareas.

### Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Instalar las bibliotecas necesarias**:

   ```bash
   pip install streamlit sqlalchemy
   ```

2. **Configurar base de datos**: La aplicación usa SQLite para almacenar las tareas. La base de datos se crea automáticamente cuando la aplicación se ejecuta por primera vez.

## 3. Pasos para ejecutar el programa

### Ejecutar la aplicación

1. **Iniciar la aplicación Streamlit**:

   En la terminal, navega hasta el directorio donde se encuentra el archivo Python y ejecuta:

   ```bash
   python -m streamlit run main.py
   ```

   Esto abrirá la aplicación en tu navegador web.

### Interacción con la aplicación

- **Agregar tareas**: En la interfaz principal, puedes agregar nuevas tareas proporcionando un título y una descripción. Al hacer clic en "Agregar", la tarea se añadirá a la base de datos.
  
- **Listar tareas**: Puedes ver todas las tareas con su estado actual (pendiente o completada).
  
- **Marcar tareas como completadas**: Puedes seleccionar una tarea pendiente de la lista y marcarla como completada.

- **Eliminar tareas completadas**: Puedes eliminar todas las tareas que estén marcadas como completadas.

- **Importar/Exportar tareas**: Puedes importar un archivo JSON con tareas previamente exportadas o exportar tus tareas actuales a un archivo JSON.


## Video de demostración

Puedes ver el video de demostración [aquí]().

---

Si tienes alguna pregunta o necesitas asistencia adicional, no dudes en consultar la documentación de Streamlit y SQLAlchemy.
