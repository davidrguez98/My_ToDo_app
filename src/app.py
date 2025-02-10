import json
import os

if not os.path.exists("data"):
    os.makedirs("data")

json_file = "data/TaskList.json"

count_id = 0
tasks = []
descriptions = []

def new_task():

    global count_id
    count_id += 1
    task = input("\nNombre de la tarea: ").capitalize()
    description = input("Descripción de la tarea: ").capitalize()

    tasks.append(task)
    descriptions.append(description)

    print(f"\nLa tarea {task} se ha guardado correctamente.")


    #No consigo dividir el json en dos listas independientes.
"""     with open(json_file, "w") as json_data:
        json.dump(tasks, json_data)

    with open(json_file, "a") as json_data:
        json.dump(descriptions, json_data) """

def list_task():

    if count_id > 0:
        print("\nListado de tareas:\n")
        for i in range(count_id):
            print(f"{i + 1}. {tasks[i]}: {descriptions[i]}")
        
    else:
        print("\nNo hay tareas registradas.")

def mark_as_done():

    list_task()
    
    mark_as_done = input("\nEscribe el número de la tarea que quieres marcar como realizada: ")

    global count_id

    if mark_as_done.isdigit():
        mark_as_done = int(mark_as_done)
        print(f"\nLa tarea {tasks[mark_as_done - 1]} se ha realizado con éxito.")
        tasks.pop(mark_as_done - 1)
        descriptions.pop(mark_as_done - 1)
        count_id -= 1
    else:
        print("\nDebes escribir un número.")

def delete_task():

    list_task()
    
    delete_task = input("\nEscribe el número de la tarea que quieres eliminar: ")

    global count_id

    if delete_task.isdigit():
        delete_task = int(delete_task)
        print(f"\nLa tarea {tasks[delete_task - 1]} se ha eliminado correctamente.")
        tasks.pop(delete_task - 1)
        descriptions.pop(delete_task - 1)
        count_id -= 1
    else:
        print("\nDebes escribir un número.")

def edit_task():

    list_task()
    
    edit_task = input("\nEscribe el número de la tarea que editar: ")

    global count_id

    if edit_task.isdigit():
        edit_task = int(edit_task)
        name_choice = input("¿Quieres cambiarle el nombre a la tarea?: ").lower()
        if name_choice == "si":
            new_name = input("Nuevo nombre de la tarea: ")
            tasks[edit_task - 1] = new_name
        else:
            pass
        description_choice = input("¿Quieres cambiarle la descripción a la tarea?: ").lower()
        if description_choice == "si":
            new_description = input("Nueva descripción de la tarea: ")
            descriptions[edit_task - 1] = new_description
        else:
            pass
    else:
        print("\nDebes escribir un número.")

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
            list_task()
        case "2":
            new_task()
        case "3":
            edit_task()
        case "4":
            delete_task()
        case "5":
            mark_as_done()
        case "6":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Escriba un número del 1 al 6.")