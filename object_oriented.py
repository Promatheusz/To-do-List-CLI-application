# Class with methods for handling tasks
import time

# A class to represent the user action menu for handling tasks. (Parent class)
class UserActionMenu:
    def __init__(self, tasks):
        self.tasks = tasks
    def add_task(self, description, date):
        id_task = len(self.tasks) + 1
        temp = [id_task, description, "", "Incomplete", date]
        self.tasks.append(temp)
        self.update_date_status()
        print("Task added successfully.")
    def delete_task(self, task_id):
        try:
            task_id = int(task_id)
            for task in self.tasks:
                if task[0] == int(task_id):
                    self.tasks.remove(task)
                    print("Task deleted successfully.")
                    return # Exit the method after deleting the task
            print("Task ID not found.")
        except ValueError:
            print("Invalid task ID.")
    def make_task_completed(self, task_id):
        try:
            task_id = int(task_id)
            for task in self.tasks:
                if task[0] == int(task_id):
                    task[3] = "Completed"
                    print("Task marked as completed.")
                    return # Exit the method after marking the task as completed
            print("Task ID not found.")
        except ValueError:
            print("Invalid task ID.")
    def view_tasks(self):
        if not self.tasks:
                print("No tasks found.")
        else:
            self.update_date_status()
            for i, task in enumerate(self.tasks, start=1):
                # tasks[1:] - slice the list to remove the ID
                # ', '.join() - join the list elements with a comma into a single string
                print(f"{i}. {', '.join(task[1:])}")
#  A class to represent a to-do list, inheriting from UserActionMenu. (Child class)
class ToDoList(UserActionMenu):
    def __init__(self, tasks):
        super().__init__(tasks)
    def update_date_status(self):
        for task in self.tasks:
            if task[4] == "":
                task[2] = "Pending"
            elif time.strptime(task[4], "%Y-%m-%d") < time.localtime():
                task[2] = "Missed"
            else:
                task[2] = "Due"