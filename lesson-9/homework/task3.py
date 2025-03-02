import json
import csv

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks back to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks in a readable format."""
    print("\nTask List:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    """Calculate and display task statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    """Convert JSON task data to a CSV file."""
    tasks = load_tasks(json_filename)
    with open(csv_filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks have been successfully saved to {csv_filename}")

def main():
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_task_stats(tasks)
    convert_json_to_csv()
    
if __name__ == "__main__":
    main()