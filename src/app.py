class Task:

    def __init__(self, task, description):
        self.task = task
        self.description = description

class ToDo:

    def __init__(self):
        self.tasks = []

    def show_TasksList(self):
        if not self.tasks:
            print("No hay tareas en la lista.")
        else:
            print("Lista de tareas:")
            for task in self.tasks:
                print(f"    - {task["Task"]}: {task["Description"]}")
        
    def new_task(self):
        task = str(input("Nombre de la tarea: "))
        description = str(input("Descripción de la tarea: "))
        new_task = {"Task": task.capitalize(), "Description": description.capitalize()}
        self.tasks.append(new_task)
        print(f"La tarea {task} ha sido creada correctamente.")

    def delete_task(self):
        
        self.show_TasksList()
        
        a = str(input("¿Qué tarea quieres eliminar?: "))
        for task in self.tasks:
            if self.tasks["Task"] == a.capitalize(): #No me hace bien la comparación.
                self.tasks.remove(task)
                print(f"La tarea {a} ha sido eliminada correctamente.")
                return
        print(f"La tarea {a} no se encuentra en la lista")


todo = ToDo()

todo.show_TasksList()
todo.new_task()
todo.new_task()
todo.new_task()
todo.delete_task()
todo.show_TasksList()
