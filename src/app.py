TASKS = []

class Task:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}: {self.description}\n"

def new_task():

    name = input("Nombre de la tarea: ").capitalize()
    description = input("Descripción de la tarea: ").capitalize()

    while True:

        if name in TASKS:

            print("Ya existe una tarea con ese nombre. ¿Quieres guardarla?")
            choice = input("Escribe 'Si' o 'No': ").capitalize()

            if choice == "No":
                print("De acuerdo. Saliendo de la opción 'Crear una nueva tarea'.")
                break
            else:
                print(f"La tarea {name} se ha guardado correctamente.")
                return Task(name, description)
        else:
            print(f"La tarea {name} se ha guardado correctamente.")
            return Task(name, description)

def task_list():

    if not TASKS:
        
        print("La lista de tareas está vacía.")
    
    else:

        print("\nLISTADO DE TAREAS:\n")

        for index, task in enumerate(TASKS):
            print(f"{index + 1}. {task.name}: {task.description}")

def edit_task():

    task_list()

    number_task = input("¿Qué tarea quieres modificar?: ")
    number_task = int(number_task)

    name = input("Nuevo nombre: ").capitalize()
    description = input("Nueva descripción: ").capitalize()
    TASKS[number_task - 1] = Task(name, description)

def delete_task():

    task_list()

    del_task = input("¿Qué tarea quieres modificar?: ")
    del_task = int(del_task)

    TASKS.pop(del_task - 1)




while True:

    print("\nTO-DO APP\n")
    print("1. Ver lista de tareas")
    print("2. Nueva tarea")
    print("3. Modificar una tarea")
    print("4. Eliminar una tarea")
    print("5. Marcar una tarea como realizada")
    print("6. Salir del programa")

    choice = input("\nSelecciona una de las opciones anteriores: ")

    match choice:
        case "1":
            task_list()
        case "2":
            TASKS.append(new_task())
        case "3":
            edit_task() #Hay que añadirle errores como que el número no esté en la lista
        case "4":
            delete_task() #Hay que añadirle errores como que el número no esté en la lista
        case "5":
            pass
        case "6":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Escriba un número del 1 al 6.")