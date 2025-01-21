""" tasks = {
    "ID" : 0,
    "Task" : "",
    "Description": "",
    "Status": "",
    "Created date": "",
    "Updated date": "",
} """

tasks = []

def tasks_list():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print(tasks)

def new_task():
    task = input("Tarea: ").capitalize()
    description = input("Descripción: ").capitalize()
    status = input("Eligen entre: todo, in-progress o done: ").capitalize()
    created_date = "yesterday".capitalize()
    updated_date = "today".capitalize()
    tasks.append({"Task": task, "Description": description, "Status": status, "Created date": created_date, "Update date": updated_date})

def delete_task():
    task = input("Eliminar: ").capitalize()
    for value in tasks.items():
        if value == task:
            del tasks[task]
        else:
            (f"La tarea {task} no se encuentra en la lista.")
        
def refresh_task():
    task = input("¿Qué tarea quieres actualizar?: ").capitalize()
    if task in tasks:
        del tasks[task]
        task = input("Tarea: ")
        description = input("Descripción: ")
        tasks[task.capitalize()] = description.capitalize()
        print("La tarea ha sido actualizada.")
    else:
        (f"La tarea {task} no se encuentra en la lista.")



tasks_list()
new_task()
new_task()
tasks_list()
delete_task()
tasks_list()