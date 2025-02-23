def add_employee(filename='employees.txt'):
    with open(filename, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
        print("Employee record added successfully.")

def view_employees(filename='employees.txt'):
    try:
        with open(filename, 'r') as file:
            records = file.readlines()
            if records:
                for record in records:
                    print(record.strip())
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No employee records file found.")

def search_employee(emp_id, filename='employees.txt'):
    try:
        with open(filename, 'r') as file:
            for record in file:
                if record.startswith(emp_id + ','):
                    print(record.strip())
                    return
        print("Employee not found.")
    except FileNotFoundError:
        print("No employee records file found.")

def update_employee(emp_id, filename='employees.txt'):
    try:
        with open(filename, 'r') as file:
            records = file.readlines()
        
        updated_records = []
        found = False
        for record in records:
            if record.startswith(emp_id + ','):
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(record)
        
        if found:
            with open(filename, 'w') as file:
                file.writelines(updated_records)
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records file found.")

def delete_employee(emp_id, filename='employees.txt'):
    try:
        with open(filename, 'r') as file:
            records = file.readlines()
        
        updated_records = [record for record in records if not record.startswith(emp_id + ',')]
        
        if len(updated_records) == len(records):
            print("Employee not found.")
        else:
            with open(filename, 'w') as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully.")
    except FileNotFoundError:
        print("No employee records file found.")

if __name__ == "__main__":
    while True:
        print("\nEmployee Record System")
        print("1. Add New Employee Record")
        print("2. View All Employee Records")
        print("3. Search for an Employee by Employee ID")
        print("4. Update an Employee's Information")
        print("5. Delete an Employee Record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            search_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            update_employee(emp_id)
        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(emp_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
