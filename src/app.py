TASKS = []

class Task:

    def __init__(self, name: str, description: str, status):
        self.name = name
        self.description = description
        self.status = status
        
    def __repr__(self):
        return f"{self.name}: {self.description}\n"
    
    display = True
    
def task_list():

    if not TASKS:
        print("La lista de tareas está vacía.")
    
    else:
        print("\nLISTADO DE TAREAS:\n")

        for index, task in enumerate(TASKS):
            print(f"{index + 1}. {task.name}: {task.description} - {task.status}")

def task_list_2():

    if not TASKS:
        print("La lista de tareas está vacía.")
    else:
        print("\nTAREAS PENDIENTES:")
        for index, task in enumerate(TASKS):
            if task.status == "To-Do":
                print(f"{index + 1}: {task.name}: {task.description}")
        print("\nTAREAS HECHAS:")
        for index, task in enumerate(TASKS):
            if task.status == "Done":
                print(f"{index + 1}: {task.name}: {task.description}")
    
def mark_as_done():

    if not TASKS:
        print("La lista de tareas está vacía.")
    else:

        task_list()

        try:
            done_task = int(input("¿Qué tarea has realizado?: "))
        except ValueError:
            print("Error: debes de introducir un número.")
            return

        TASKS[done_task - 1].status = "Done"
        print(f"La tarea {TASKS[done_task - 1].name} ha sido realizada.")

def new_task():

    name = input("Nombre de la tarea: ").capitalize()

    while True:

        for task in TASKS:

            if task.name == name:
                print("Ya existe una tarea con ese nombre. ¿Quieres guardarla?")
                choice = input("Escribe 'Si' o 'No': ").capitalize()
                if choice == "No":
                    print("De acuerdo. Saliendo de la opción 'Crear una nueva tarea'.")
                    return None
                
        description = input("Descripción de la tarea: ").capitalize()
        status = "To-Do"
            
        print(f"La tarea {name} se ha guardado correctamente.")
        return Task(name, description, status)

def edit_task():

    task_list()

    try:
        number_task = int(input("¿Qué tarea quieres modificar?: "))
    except ValueError:
        print("Error: debes de introducir un número.")
        return

    if number_task < 1 or number_task > len(TASKS):
        print("Error: Selecciona un número de tarea válido.")
        return

    name = input("Nuevo nombre: ").capitalize()
    description = input("Nueva descripción: ").capitalize()
    
    TASKS[number_task - 1].name = name
    TASKS[number_task - 1].description = description
    print(f"La tarea {name} ha sido actualizada correctamente.")

def delete_task():

    task_list()

    try:
        del_task = int(input("¿Qué tarea quieres modificar?: "))
    except ValueError:
        print("Error: debes de introducir un número.")
        return

    if del_task < 1 or del_task > len(TASKS):
        print("Error: Selecciona un número de tarea válido.")
        return
    
    print(f"La tarea {TASKS[del_task - 1].name} ha sido eliminada.")
    TASKS.pop(del_task - 1)

def settings() -> bool:

        choice = input("\n¿Quieres cambiar la vista?: ").capitalize()
        
        while True:

            if choice == "Si":
                if Task.display == False:
                    Task.display = True
                    print("Vista cambiada.")
                    return
                if Task.display == True:
                    Task.display = False
                    print("Vista cambiada.")
                    return
            else:
                break



while True:

    print("\nTO-DO APP")
    print("1. Ver lista de tareas")
    print("2. Marcar una tarea como realizada")
    print("3. Nueva tarea")
    print("4. Modificar una tarea")
    print("5. Eliminar una tarea")
    print("6. Configuración de vista de listado")
    print("7. Salir del programa")

    choice = input("\nSelecciona una de las opciones anteriores: ")

    match choice:
        case "1":
            if Task.display == False:
                task_list_2()
            else:
                task_list()
        case "2":
            mark_as_done()
        case "3":
            task = new_task()
            if task:
                TASKS.append(task)
        case "4":
            edit_task()
        case "5":
            delete_task()
        case "6":
            settings()
        case "7":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Escriba un número del 1 al 7.")
