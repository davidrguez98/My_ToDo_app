# My ToDo App ✅📝

Aplicación de consola en Python que permite crear, listar, modificar, marcar como completadas y eliminar tareas. Las tareas se almacenan de forma persistente en un archivo JSON local. Es un proyecto ideal para practicar estructuras de control, manejo de archivos, clases y persistencia de datos sin base de datos.

## 🧠 Descripción

El usuario interactúa con el programa desde el terminal mediante un menú numérico. Cada tarea contiene un nombre, una descripción y un estado (`To-Do` o `Done`). Las tareas se guardan en `data/TaskList.json`, lo que permite mantener la información entre sesiones.

## ⚙️ Funcionalidad

- Crear nuevas tareas con nombre y descripción.
- Listar todas las tareas o clasificarlas por estado.
- Marcar tareas como realizadas.
- Editar nombre y descripción de tareas existentes.
- Eliminar tareas por su número de índice.
- Cambiar el modo de visualización (lista completa o dividida en pendientes/hechas).
- Guardado y carga automática desde archivo JSON.

## 🛠️ Tecnologías usadas

- **Python 3.10+**
- **json** para guardar tareas en disco
- Aplicación desarrollada completamente en consola (sin interfaces gráficas ni web)

## 📁 Estructura del proyecto

```
My_ToDo_app/
│
├── data/
│   └── TaskList.json       # Archivo donde se almacenan las tareas
│
└── src/
    └── app.py              # Código principal con toda la lógica y el menú interactivo
```

## 🚀 Instalación y ejecución

1. Clona el repositorio:
   ```
   git clone https://github.com/davidrguez98/My_ToDo_app.git
   cd My_ToDo_app/src
   ```

2. Ejecuta el programa:
   ```
   python app.py
   ```

   Asegúrate de tener Python 3.10 o superior instalado.

3. Interactúa con el menú que aparecerá en pantalla para gestionar tus tareas.

## 📝 Estructura de una tarea

Cada tarea se guarda en el archivo `TaskList.json` con esta estructura:

```json
{
    "name": "Lengua",
    "description": "Si",
    "status": "To-Do"
}
```

## 🤝 Contacto

Si quieres ponerte en contacto conmigo:

- [LinkedIn](https://www.linkedin.com/in/davidrguez98/)
- Correo: ropeda98@gmail.com
