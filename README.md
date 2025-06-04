# My ToDo App ✅📝

Aplicación backend desarrollada en Python que permite gestionar tareas (crear, listar, actualizar y eliminar), almacenándolas en un archivo local en formato JSON. Ideal como proyecto introductorio para entender la estructura de una API simple y persistencia de datos sin base de datos externa.

## 🧠 Descripción

Esta API permite llevar el control de tareas a través de un sistema sencillo que utiliza un archivo `.json` para el almacenamiento de la información. Ofrece una base sólida para ser extendida a aplicaciones web con interfaz de usuario o integración con bases de datos reales.

## ⚙️ Funcionalidad

- Crear nuevas tareas con nombre, descripción y estado.
- Leer la lista completa de tareas almacenadas.
- Actualizar tareas por su ID.
- Eliminar tareas específicas.
- Persistencia de datos en un archivo JSON (`TaskList.json`).

## 🛠️ Tecnologías usadas

- **Python 3.10+**
- **FastAPI** para creación de endpoints.
- **JSON** para el almacenamiento local de datos.

## 📁 Estructura del proyecto

```
My_ToDo_app/
│
├── data/
│   └── TaskList.json       # Archivo donde se almacenan las tareas
│
└── src/
    └── app.py              # Código principal con los endpoints y lógica de la API
```

## 🚀 Instalación y puesta en marcha

1. Clona el repositorio:
   ```
   git clone https://github.com/davidrguez98/My_ToDo_app.git
   cd My_ToDo_app
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias necesarias:
   ```
   pip install fastapi uvicorn
   ```

4. Inicia el servidor:
   ```
   uvicorn src.app:app --reload
   ```

   La API estará disponible en `http://127.0.0.1:8000`.

5. Puedes explorar la documentación automática de la API en:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - Redoc: `http://127.0.0.1:8000/redoc`

## 🤝 Contacto

Si quieres ponerte en contacto conmigo:

- [LinkedIn](https://www.linkedin.com/in/davidrguez98/)
- Correo: ropeda98@gmail.com
