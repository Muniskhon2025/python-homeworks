import json

class EmployeeManager:
    def __init__(self, filename='employees.json'):
        self.filename = filename
        self.load_records()

    def load_records(self):
        try:
            with open(self.filename, 'r') as file:
                self.records = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.records = []

    def save_records(self):
        with open(self.filename, 'w') as file:
            json.dump(self.records, file, indent=4)

    def add_employee(self, emp_id, name, age, department):
        employee = {'ID': emp_id, 'Name': name, 'Age': age, 'Department': department}
        self.records.append(employee)
        self.save_records()
        print("Employee added successfully.")

    def view_employees(self):
        if not self.records:
            print("No employee records found.")
            return
        for emp in self.records:
            print(emp)

    def delete_employee(self, emp_id):
        self.records = [emp for emp in self.records if emp['ID'] != emp_id]
        self.save_records()
        print("Employee deleted successfully.")

if __name__ == "__main__":
    manager = EmployeeManager()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            manager.add_employee(emp_id, name, age, department)
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
