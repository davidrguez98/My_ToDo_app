import json
import os

if not os.path.exists("data"):
    os.makedirs("data")

json_file = "data/TaskList.json"

def task_list():

    with open(json_file, "r") as json_data:
        print(json_data.read())

def new_task():
    task = input("Tarea: ").capitalize()
    description = input("Descripción: ").capitalize()
    status = input("Eligen entre: todo, in-progress o done: ").capitalize()
    created_date = "yesterday".capitalize()
    updated_date = "today".capitalize()
    data = {
        "Task": task, 
        "Description": description, 
        "Status": status, 
        "Created date": created_date, 
        "Update date": updated_date
        }

    with open(json_file, "a") as json_data:
        json.dump(data, json_data)

def update_task():
    update_task = input("¿Qué tarea quieres actualizar?: ").capitalize()
    
    with open(json_file, "r") as json_data: #No consigo entrar el json para leer los value de los dict de dentro ya que mi diccionario está en otro archivo
        json_dict = json.load(json_data)

        

""" def refresh_task():

    update_task = input("Tarea que quieres actualizar: ").capitalize()

    with open(json_file, "r") as json_data:
        data_dict = json.load(data)
        for value in data["name"].items():
            if value == update_task:
                new_task() 


    with open(json_file, "r") as json_data:
        json_dict = json.load(json_data)
        if json_dict["name"] == update_task:
            print("true")

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
        (f"La tarea {task} no se encuentra en la lista.") """




new_task()
task_list()
