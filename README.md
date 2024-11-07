# To-do-List-CLI-application

## Description
This project is a simple command-line interface (CLI) application for managing a to-do list using Python

## Features

- Add a task with a description and deadline.
- Delete a task by its ID.
- Mark a task as completed.
- View the list of tasks with their statuses.
- Import tasks from a CSV file.
- Export tasks to a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Promatheusz/To-do-List-CLI-application.git
    ```
2. Make sure you have Python installed on your system.
3. Make sure you have data in import_tasks.csv file.

## How to run the application ?

1. Run the application:
    ```sh
    python3 main.py
    ```
2. Follow the on-screen menu to interact with the application:
    - `a) Add a task`
    - `b) Delete a task`
    - `c) Make a task as completed`
    - `d) View tasks list`
    - `e) Exit a program`

## File Structure
- `main.py`: Main entry point of the application.
- `object_oriented.py`: Contains the classes and methods for handling tasks.
- `file_handling.py`: Functions for importing and exporting tasks to/from CSV files.

## CSV File Format
- ID(number)
- Description(string) 
- Date_status(string) 
- Task_status(string)
- Date(date)
