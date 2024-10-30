class Employee :
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    def increace_salary(self, percent):
        self.salary += self.salary * percent / 100
    
    def __str__(self):
        return f"Employee {self.name} is a {self.position} with a salary {self.salary}"
    
    def __repr__(self):
        return (
            f"Employee( "
            f"{repr(self.name)}, {repr(self.age)}, " 
            f"{repr(self.position)}, {repr(self.salary)})"
            )
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 100:
            raise ValueError("Minimun wage is 100")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary == None:
            self._annual_salary = self.salary * 12
        return self._annual_salary


employee1 = Employee("John", 32, "developer", 120)
employee2 = Employee("Anna", 23, "tester", 100)

print(employee1.annual_salary)
employee1.salary = 200

print(employee1.annual_salary)

