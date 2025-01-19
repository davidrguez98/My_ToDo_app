while True:

    tasks = []

    def new_task():
        task = str(input("¿Qué tarea quieres añadir?: "))  
        if task in tasks:
            qt = str(input(f"La tarea {task} ya se encuentra en la lista de tareas. ¿Desea añadirla?: "))
            if qt.lower() == "si":
                print(f"La tarea {task} ha sido añadida correctamente.")
                tasks.append(task)
            else:
                print(f"La tarea {task} no ha sido añadida.")                   
        if task not in tasks:
            print(f"La tarea {task} ha sido añadida correctamente")
            tasks.append(task)
            print(tasks)
        

    print("")
    print("1. Ver lista de tareas.")
    print("2. Añadir una tarea.")
    print("3. Actualizar una tarea de la lista de tareas.")
    print("4. Eliminar una tarea de la lista de tareas.")
    print("5. Salir del programa.")
    index = str(input("\nEscribe la opción que deseas realizar: "))

    match index:
        case "1":
            print(tasks)
        case "2":
            new_task()
        case "3":
            def update_task():
                print(tasks)
                task = str(input("¿Qué tarea quieres actualizar?"))
                if task in tasks:
                    del tasks[task]
                    new_task()
                    print(f"La tarea {task} ha sido actualizada.")
                else:
                    print(f"La tarea {task} no se encuentra en la lista de tareas.")
        case "4":
            def delete_task():
                print(tasks)
                task = str(input("¿Qué tarea quieres eliminar?: "))
                if task.capitalize() in tasks:
                    print(f"La tarea {task} ha sido eliminada")
                    del tasks[task]
                else:
                    print(f"La tarea {task} no se encuentra en la lista de tareas.")
        case "5":
            break
        case "6":
            print("\nLa opción marcada no es correcta. Selecciona un número del 1 al 5.")
