tasks = {}

def tasks_list():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print(tasks)

def new_task():
    task = input("Tarea: ")
    description = input("Descripción: ")
    tasks[task.capitalize()] = description.capitalize()
    print(f"La tarea {task} ha sido creada.")

def delete_task():
    task = input("Eliminar: ").capitalize()
    if task in tasks:
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



new_task()
new_task()
tasks_list()
delete_task()
tasks_list()
refresh_task()
tasks_list()