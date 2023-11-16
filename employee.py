class Employee:
    def __init__(self, name, base_salary, bonus_hrs, sales):
        self.name = name
        self.base_salary = base_salary
        self.bonus_hrs = bonus_hrs
        self.sales = sales

    def info(self):
       print("The employee Name is",self.name," his base salary is",self.base_salary)
       print("The number of sales is",self.sales,"he won a",self.bonus_hrs,"bonus hours")

employee1 = Employee("Ahmed", 50000, 5, 100000)  
employee2 = Employee("Adam", 60000, 8, 120000)  

# Calculating and printing the total salary for each employee
employee1.info()
employee2.info()

