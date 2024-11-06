import methods
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
    todolist = methods.ToDoList(load_tasks)
    # Run the application
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == 'a':
            # Create a syntex
            task = input("Enter the task: ")
            todolist.add_task(task)
        elif choice == 'b':
            task_id = input("Enter the task id: ")
            todolist.delete_task(task_id)
        elif choice == 'c':
            task_id = input("Enter completed task id: ")
        elif choice == 'd':
            todolist.view_tasks()
        elif choice == 'e':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    print("See you later!")