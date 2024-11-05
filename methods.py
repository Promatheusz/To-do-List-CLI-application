# Class with methods for handling tasks
class ToDoList:
    def __init__(self, task):
        self.task = task
        self.task = []
    def add_task(self, task):
        self.task.append(task)
        print("Task added successfully.")

    def delete_task(self, task):
        if task in self.task:
            self.task.remove(task)
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    def view_tasks(self):
        if len(self.task) == 0:
            print("No tasks found.")
        else:
            for i in range(len(self.task)):
                print(f"{i+1}. {self.task[i]}")

