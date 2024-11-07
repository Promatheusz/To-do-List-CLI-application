# File to save, import, export csv files
import csv

# Csv file structure : ID(number), Description(string), Date_status(string), Task_status(string), Date(date)
# ID = unique number for tasks
# Description = description of task to be done
# Date_status = status of task determine by date (Pending, Due, Missed)
# Task_status = status of task added by user (Incomplete, Completed)
# Date = deadline for task (empty if no deadline)

# Function to import tasks from the csv file
def import_tasks(file_name):
    imported_tasks = []
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
               imported_tasks.append(row)
    except FileNotFoundError:
        print("File not found.")
    return imported_tasks

# Function to export tasks to the csv file
def export_tasks(exported_tasks):
    try:
        with open('export_tasks.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(exported_tasks)
    except IOError as e:
        print(f"Error writing to file: {e}")

# Function to append task list with new tasks from the imported tasks
def add_tasks_to_list(imported_tasks, task):
    task_id = len(task) + 1
    # Change the ID of the imported tasks
    for i in range(len(imported_tasks)):
        imported_tasks[i][0] = task_id
        task_id += 1
        task.append(imported_tasks[i])
    return task