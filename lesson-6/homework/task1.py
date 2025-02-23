def add_employee(filename='employees.txt'):
    with open(filename, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
        print("Employee record added successfully.")

if __name__ == "__main__":
    while True:
        print("\nEmployee Record System")
        print("1. Add Employee Record")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")
