class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary

    def display_info(self):
        return f"ID: {self.id_number}, Name: {self.name}, Salary: ${self.salary}"

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement this method")

class Manager(Employee):
    def __init__(self, name, id_number, salary, department, bonus_percentage):
        super().__init__(name, id_number, salary)
        self.department = department
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        bonus = self.salary * self.bonus_percentage
        print(f"Manager {self.name} bonus: ${bonus}")
        return bonus

    def assign_task(self, task):
        print(f"Manager {self.name} has assigned task: {task}")

class Engineer(Employee):
    def __init__(self, name, id_number, salary, specialty, project_bonus):
        super().__init__(name, id_number, salary)
        self.specialty = specialty
        self.project_bonus = project_bonus

    def calculate_bonus(self, projects_completed):
        bonus = projects_completed * self.project_bonus
        print(f"Engineer {self.name} bonus for {projects_completed} projects: ${bonus}")
        return bonus

    def work_on_project(self, project):
        print(f"Engineer {self.name} is working on project: {project}")

# Salesperson subclass
class Salesperson(Employee):
    def __init__(self, name, id_number, salary, commission_rate):
        super().__init__(name, id_number, salary)
        self.commission_rate = commission_rate

    def calculate_bonus(self, sales_made):
        bonus = sales_made * self.commission_rate
        print(f"Salesperson {self.name} bonus for {sales_made} sales: ${bonus}")
        return bonus

    def make_sale(self, sale_value):
        print(f"Salesperson {self.name} made a sale worth ${sale_value}.")

manager = Manager("Alice", "M123", 85000, department="IT", bonus_percentage=0.10)
print(manager.display_info())
manager.calculate_bonus()
manager.assign_task("Complete IT infrastructure upgrade")

engineer = Engineer("Bob", "E456", 75000, specialty="Software", project_bonus=2000)
print(engineer.display_info())
engineer.calculate_bonus(projects_completed=3)
engineer.work_on_project("New App Development")

salesperson = Salesperson("Charlie", "S789", 60000, commission_rate=500)
print(salesperson.display_info())
salesperson.calculate_bonus(sales_made=15)
salesperson.make_sale(sale_value=1200)
