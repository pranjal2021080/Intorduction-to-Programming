# Group Project (Bonus – Assignment 3)

## To-Do List Manager (Python)

---

## Project Overview

This project is a **command-line based To-Do List Manager** developed in **Python** as part of the **Bonus (Group Project)** for **Assignment 3 – Introduction to Programming**.

The application allows users to manage daily tasks by **adding, updating, deleting, completing, and listing tasks**. All task data is stored persistently in a **JSON file**, ensuring that data is retained across program executions.

---

## Features

The application supports the following operations:

* Add a new task with a unique ID
* Update an existing task description
* Delete a task and reassign task IDs
* Mark tasks as completed
* Display all tasks with completion status
* Automatically save and load tasks using a JSON file

---

## Project Structure

```
Bonus_Group_Project
│
├── bonus_project.py      # Main Python source code
├── tasks.json            # Persistent task storage
└── README.md             # Project documentation
```

---

## Code Design

### Task Class

Represents an individual task with:

* Task ID
* Task description
* Completion status

Includes a method to convert task objects into dictionary format for JSON storage.

---

### TaskManager Class

Responsible for:

* Loading and saving tasks from/to a JSON file
* Adding, updating, deleting, and completing tasks
* Reassigning task IDs after deletion
* Displaying tasks in a readable format

---

### Menu-Driven Interface

The `main()` function provides a continuous menu-based interface that allows users to interact with the task manager until they choose to exit.

---

## File Storage Format

Tasks are stored in `tasks.json` using the following format:

```json
[
    {
        "id": 1,
        "description": "a",
        "completed": false
    }
]
```

This ensures easy readability and efficient data persistence.

---

## Testing

A test function using **assert statements** is included to verify:

* Task creation
* Task updates
* Task deletion
* ID reassignment
* Data saving and loading

This helps ensure correctness and reliability of the application.

---

## How to Run the Program

### Requirements

* Python 3.x

### Steps

1. Open a terminal and navigate to the project folder.
2. Run the following command:

   ```
   python bonus_project.py
   ```
3. Use the on-screen menu to manage tasks.

---

## Assumptions and Limitations

* The application is designed for **single-user usage**.
* Minimal input validation is performed.
* Task IDs are reassigned after deletions for simplicity.
* Additional computational functions exist in the code but are not invoked.

---

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming concepts in Python
* File handling and JSON-based persistence
* Menu-driven program design
* Basic testing using assertions

---

## Bonus Assignment Declaration

This project is submitted as the **Bonus Question (Group Project)** for **Assignment 3** under the **Introduction to Programming** course.

---
