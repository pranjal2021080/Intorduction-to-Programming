import json
import os

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed}

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task.description}")

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                self.save_tasks()
                print(f"Task {task_id} updated.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.reassign_ids()
        self.save_tasks()
        print(f"Task {task_id} deleted.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "✓" if task.completed else "✗"
                print(f"[{status}] Task {task.id}: {task.description}")

    def reassign_ids(self):
        for index, task in enumerate(self.tasks, start=1):
            task.id = index
def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
def test_todo_list_manager():
    # Create a Task instance
    task = Task(1, "Finish Python project", False)
    assert task.id == 1
    assert task.description == "Finish Python project"
    assert task.completed is False
    assert task.to_dict() == {"id": 1, "description": "Finish Python project", "completed": False}

    # Create TaskManager instance
    manager = TaskManager(file_name="test_tasks.json")
    assert isinstance(manager.tasks, list)
    assert len(manager.tasks) == 0

    # Test adding tasks
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    assert len(manager.tasks) == 3
    assert manager.tasks[0].description == "Task 1"
    assert manager.tasks[1].description == "Task 2"
    assert manager.tasks[2].description == "Task 3"

    # Test marking task as completed
    manager.mark_task_completed(2)
    assert manager.tasks[1].completed is True
    assert manager.tasks[0].completed is False

    # Test updating a task
    manager.update_task(1, "Updated Task 1")
    assert manager.tasks[0].description == "Updated Task 1"

    # Test deleting a task
    manager.delete_task(2)
    assert len(manager.tasks) == 2
    assert manager.tasks[0].description == "Updated Task 1"
    assert manager.tasks[1].description == "Task 3"

    # Test task ID reassignment
    assert manager.tasks[0].id == 1
    assert manager.tasks[1].id == 2

    # Test listing tasks
    assert manager.list_tasks() is None  # list_tasks prints output, returns nothing

    # Test saving and loading tasks
    manager.save_tasks()
    loaded_manager = TaskManager(file_name="test_tasks.json")
    assert len(loaded_manager.tasks) == 2
    assert loaded_manager.tasks[0].description == "Updated Task 1"
    assert loaded_manager.tasks[1].description == "Task 3"

    print("All tests passed!")  # Just for manual confirmation if this function is called.

# This function is not called anywhere in the code.
    
def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. List Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description: ")
            manager.update_task(task_id, new_description)
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            manager.mark_task_completed(task_id)
        elif choice == "5":
            manager.list_tasks()
        elif choice == "6":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
