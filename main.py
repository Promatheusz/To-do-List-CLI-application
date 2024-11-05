import methods
import file_handling

# Menu function to display the options
def print_menu():
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View tasks")
    print("4. Exit")

# Main function that runs the application
def main():
    # Initialize task class
    load_tasks = []
    todolist = methods.ToDoList(load_tasks)
    # Run the application
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todolist.add_task(task)
        elif choice == '2':
            task = input("Enter the task: ")
            todolist.delete_task(task)
        elif choice == '3':
            todolist.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    print("See you later!")