class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        if not isinstance(employee_id, str):
            raise TypeError('Employee ID must be a string')
        if hourly_rate <= 0:
            raise ValueError('Hourly rate must be greater than zero')
        if hours_worked < 0 or hours_worked > 168:
            raise ValueError('Hours worked must be between 0 and 168 per week') 
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def weekly_pay(self):
        overtime_rate = self.hourly_rate * 1.5
        overtime = self.hours_worked - 40
        if self.hours_worked <= 40:
            pay = self.hours_worked * self.hourly_rate
            return pay
        enhanced_pay = overtime_rate * overtime
        normal_pay = self.hourly_rate * 40
        total_pay = enhanced_pay + normal_pay
        return total_pay

    def give_raise(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Amount must be greater than zero")
        self.hourly_rate += amount
        return f"Hourly rate increased by {amount}."

    def __str__(self):
        title = "\nEMPLOYEE INFORMATION\n"
        title += f"Name: {self.name}\nEmployee ID: {self.employee_id}\nHourly Rate: {self.hourly_rate}\nHours Worked: {self.hours_worked}\nWeekly Pay: {self.weekly_pay():.2f}"
        return title

class Manager(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked, bonus):
        super().__init__(name, employee_id, hourly_rate, hours_worked)
        if bonus < 0:
            raise ValueError("Bonus must be more than or equal to zero")
        self.bonus = bonus
        self.approved = False

    def approve_overtime(self):
        if self.hours_worked > 40:
            self.approved = True
            return True
        return False

    def weekly_pay(self):
        normal_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)

        normal_pay = normal_hours * self.hourly_rate
        overtime_pay = overtime_hours * self.hourly_rate * 1.5

        if self.approved:
            return normal_pay + overtime_pay + self.bonus

        return normal_pay + self.bonus

    def __str__(self):
        title = "\nMANAGER INFORMATION\n"
        title += f"Name: {self.name}\n"
        title += f"Employee ID: {self.employee_id}\n"
        title += f"Hourly Rate: £{self.hourly_rate}\n"
        title += f"Hours Worked: {self.hours_worked}\n"
        title += f"Bonus: £{self.bonus}\n"
        title += f"Overtime Approved: {self.approved}\n"
        title += f"Weekly Pay: £{self.weekly_pay():.2f}"

        return title

        
class EmployeeManager:
    def __init__(self):
        self.collections = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Data must be an instance of Employee class")
        self.collections.append(employee)
    
    def remove_employee(self, employee_id):
        for employee in self.collections:
            if employee_id == employee.employee_id:
                self.collections.remove(employee)
                return
        raise ValueError(f"Employee with ID{employee_id} not found")
            
    
    def find_employee(self, employee_id):
        title = "\nEMPLOYEE INFO\n"
        for employee in self.collections:
            if employee_id == employee.employee_id:
                return employee
        raise ValueError('Invalid employee ID')
            
    
    def total_payroll(self):
        total = 0
        for data in self.collections:
            total += data.weekly_pay()
        return total
    
  
    def display_employees(self):
        data = "LIST OF EMPLOYEES\n"
        for i, employee in enumerate(self.collections, start=1):
            data += f'{i} ➡ {employee.name} {employee.employee_id}\n'
        print(data)
    




manager = EmployeeManager()
while True:
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Find employee")
    print("4. Display employees")
    print("5. Show total payroll")
    print("6. Approve manager overtime")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "7":
        break
    elif choice == "6":
        employee_id = input("Enter manager ID: ")
        try:
            employee1 = manager.find_employee(employee_id)
            if isinstance(employee1, Manager):
                employee1.approve_overtime()
                print("Overtime approved.")
            else:
                print("That employee is not a manager.")
        except ValueError:
            print("Invalid employee ID")
        
    elif choice == "4":
        manager.display_employees()
    elif choice == "5":
        total = manager.total_payroll()
        print(f"Total weekly payroll: £{total:.2f}")
    elif choice == "3":
        employee_id = input("Enter employee ID: ")
        print("\nEMPLOYEE INFO\n")
        employee_found = manager.find_employee(employee_id)
        print(f"Name: {employee_found.name}\nEmployee ID: {employee_id}")
        
    elif choice == "2":
        employee_id = input("Enter employee ID: ")
        try:
            manager.remove_employee(employee_id)
        except ValueError as error:
            print("Invalid employee ID")
    elif choice == "1":
        employee_type = input("Add Employee or Manager? ").lower()
        if employee_type == "employee":
            name = input("Enter name: ")
            employee_id = input("Enter employee ID: ")
            hourly_rate = input("Enter hourly rate: ")
            hours_worked = input("Enter hours worked: ")
            employee = Employee(name, employee_id, int(hourly_rate), int(hours_worked))
            manager.add_employee(employee)
        elif employee_type == "manager":
            name = input("Enter name: ")
            employee_id = input("Enter employee ID: ")
            hourly_rate = input("Enter hourly rate: ")
            hours_worked = input("Enter hours worked: ")
            bonus = input("Enter bonus: ")
            new_manager = Manager(name, employee_id, int(hourly_rate), int(hours_worked), int(bonus))
            manager.add_employee(new_manager)
        else:
            print("Invalid choice")