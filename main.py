import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import os

# Configuración de SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///tasks.db', echo=True)
Session = sessionmaker(bind=engine)

# Modelo de datos
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(String(20), default='pendiente')

# Función para crear las tablas
def create_tables():
    Base.metadata.create_all(engine)

# CRUD
def add_task(title, description, status="pendiente"):
    session = Session()
    new_task = Task(title=title, description=description, status=status)
    session.add(new_task)
    session.commit()
    session.close()

def list_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def mark_task_completed(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.status = 'completada'
        session.commit()
    session.close()

def delete_completed_tasks():
    session = Session()
    session.query(Task).filter_by(status='completada').delete()
    session.commit()
    session.close()

# Exportar e importar
def export_tasks(file_path):
    tasks = list_tasks()
    structured_tasks = [
        {
            "title": task.title,
            "description": task.description,
            "status": task.status
        } for task in tasks
    ]
    with open(file_path, 'w') as file:
        json.dump(structured_tasks, file, indent=4)
    st.success(f"Tareas exportadas correctamente a {file_path}")

def import_tasks(file_content):
    try:
        tasks = json.loads(file_content)
        for task in tasks:
            if all(key in task for key in ["title", "description", "status"]):
                add_task(task["title"], task["description"], task["status"])
            else:
                st.warning("Formato inválido en una tarea.")
        st.success("Tareas importadas correctamente.")
    except json.JSONDecodeError:
        st.error("El archivo JSON tiene un formato incorrecto.")

# Streamlit UI
def main():
    # Asegurarse de que las tablas existen
    create_tables()

    st.set_page_config(page_title="Gestor de Tareas", layout="wide")
    
    st.title("Aplicación de Gestión de Tareas")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Menú")
        menu = ["Agregar tarea", "Listar tareas", "Marcar completada", "Eliminar completadas", "Importar/Exportar"]
        choice = st.radio("Selecciona una opción", menu)
    
    with col2:
        if choice == "Agregar tarea":
            st.subheader("Agregar nueva tarea")
            title = st.text_input("Título")
            description = st.text_area("Descripción")
            if st.button("Agregar"):
                if title:
                    add_task(title, description)
                    st.success(f"Tarea '{title}' agregada exitosamente.")
                else:
                    st.error("El título no puede estar vacío.")
        
        elif choice == "Listar tareas":
            st.subheader("Lista de tareas")
            tasks = list_tasks()
            if tasks:
                for task in tasks:
                    status = "✅" if task.status == 'completada' else "⏳"
                    st.write(f"{status} **{task.title}** - {task.description}")
            else:
                st.info("No hay tareas disponibles.")

        elif choice == "Marcar completada":
            st.subheader("Marcar tarea como completada")
            tasks = list_tasks()
            task_options = {task.title: task.id for task in tasks if task.status == 'pendiente'}
            if task_options:
                selected_task = st.selectbox("Selecciona una tarea", list(task_options.keys()))
                if st.button("Marcar como completada"):
                    mark_task_completed(task_options[selected_task])
                    st.success(f"Tarea '{selected_task}' marcada como completada.")
            else:
                st.info("No hay tareas pendientes para marcar como completadas.")

        elif choice == "Eliminar completadas":
            st.subheader("Eliminar tareas completadas")
            if st.button("Eliminar"):
                delete_completed_tasks()
                st.success("Tareas completadas eliminadas exitosamente.")

        elif choice == "Importar/Exportar":
            st.subheader("Importar o exportar tareas")
            
            export_col, import_col = st.columns(2)
            
            with export_col:
                st.write("Exportar tareas")
                export_path = st.text_input("Nombre del archivo para exportar (ej: tareas.json)")
                if st.button("Exportar"):
                    if export_path:
                        export_tasks(export_path)
                    else:
                        st.error("Especifica un nombre de archivo válido.")
            
            with import_col:
                st.write("Importar tareas")
                import_file = st.file_uploader("Importar Archivo JSON", type=["json"])
                if import_file and st.button("Importar"):
                    import_tasks(import_file.getvalue().decode("utf-8"))

if __name__ == "__main__":
    main()

