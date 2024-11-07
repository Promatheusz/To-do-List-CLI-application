import object_oriented
import file_handling

# Menu function to display the options
def print_menu():
    print("a) Add a task")
    print("b) Delete a task")
    print("c) Make a task as completed")
    print("d) View tasks list")
    print("e) Exit a program")

# Main function that runs the application
def main():
    # Loading a tasks from the csv file
    load_tasks = file_handling.import_tasks("import_tasks.csv")
    # Initialize TodoList object
    todolist = object_oriented.ToDoList(load_tasks)
    # Run the application in a loop
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == 'a':
            description = input("Enter task description: ")
            date = input("Enter task deadline (yyyy-mm-dd): ")
            todolist.add_task(description, date)
        elif choice == 'b':
            task_id = input("Enter the task id: ")
            todolist.delete_task(task_id)
        elif choice == 'c':
            task_id = input("Enter completed task id: ")
            todolist.make_task_completed(task_id)
        elif choice == 'd':
            todolist.view_tasks()
        elif choice == 'e':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    print("See you later!")