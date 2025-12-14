1. Project Overview

This project implements a command-line based To-Do List Manager using Python.
The application allows users to manage tasks by adding, updating, deleting, completing, and listing tasks, with all task data persisted in a JSON file.

The project demonstrates the use of:

Object-Oriented Programming (OOP)

File handling using JSON

Modular design with classes and methods

Basic testing using assertions

Menu-driven user interaction

This project is developed as part of the Bonus (Group Project) for Assignment 3 – Introduction to Programming.

2. Features

The To-Do List Manager supports the following functionalities:

Add Task

Create a new task with a unique ID and description.

Task is initially marked as not completed.

Update Task

Modify the description of an existing task using its ID.

Delete Task

Remove a task permanently.

Automatically reassigns task IDs to maintain order.

Mark Task as Completed

Update the status of a task to completed.

List Tasks

Display all tasks with their IDs and completion status.

Completed tasks are marked with ✓, incomplete tasks with ✗.

Persistent Storage

All tasks are saved to a tasks.json file.

Data is automatically loaded when the program restarts.

3. Project Structure
Bonus_Group_Project
│
├── bonus_project.py      # Main application source code
├── tasks.json            # Stores task data persistently
└── README.md             # Project documentation

4. Code Architecture
4.1 Task Class

Represents an individual task.

Attributes:

id : Unique task identifier

description : Task description

completed : Boolean status

Methods:

to_dict() – Converts a Task object to a dictionary for JSON storage

4.2 TaskManager Class

Handles all task-related operations and file handling.

Responsibilities:

Loading tasks from JSON

Saving tasks to JSON

Adding, updating, deleting, and listing tasks

Reassigning task IDs after deletion

Key Methods:

load_tasks()

save_tasks()

add_task()

update_task()

delete_task()

mark_task_completed()

list_tasks()

4.3 Menu-Driven Interface (main())

The main() function provides a continuous loop with a menu allowing the user to interact with the application until they choose to exit.

5. Testing

A dedicated test function test_todo_list_manager() is included to validate core functionalities using assert statements, such as:

Task creation

Task updates

Task deletion

ID reassignment

File save/load consistency

This ensures correctness and reliability of the system.

6. File Storage Format (tasks.json)

Tasks are stored in JSON format as shown below:

[
    {
        "id": 1,
        "description": "a",
        "completed": false
    }
]


This format ensures:

Human readability

Easy serialization/deserialization

Persistent storage across executions

7. How to Run the Program
Requirements

Python 3.x

Steps

Navigate to the project directory:

cd Bonus_Group_Project


Run the program:

python bonus_project.py


Follow the on-screen menu options to manage tasks.

8. Limitations & Assumptions

The application is single-user and command-line based.

Input validation is minimal (assumes correct input format).

Task IDs are reassigned after deletion for simplicity.

Two additional mathematical functions are included but not invoked, serving as unused computational examples.

9. Learning Outcomes

Through this project, the following concepts were practiced:

Object-oriented design in Python

Persistent data storage using JSON

File I/O operations

Menu-based program flow

Unit-style testing using assertions

10. Bonus Assignment Declaration

This project is submitted as part of the Bonus Question (Group Project) for Assignment 3 of the Introduction to Programming course.
