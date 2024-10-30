class Vehicle:
    def __init__(self, maker, model, year):
        self.make = maker
        self.model = model
        self.year = year

    def start(self):
        print("Starting the veacle!")

    def stop(self):
        print("Stop!!!")

    def fuel_up(self):
        print("Fuel up")

class Car(Vehicle):
    def __init__(self, maker, model, year, num_doors ):
        super().__init__(maker, model, year)
        self.num_doors = num_doors

    def honk(self):
        print("Beeeeeeeeep!")

car1 = Car("Kia", "Seed", 2020, 5)

print(car1.num_doors)
car1.start()
car1.honk()
car1.stop()

class Bicycle(Vehicle):
    def __init__(self, maker, model, year, num_gears):
        super().__init__(maker, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print("Ding Dong!")

bicycle1 = Bicycle("Cannondale", "Trail", 2024, 10)

print(bicycle1.num_gears)
bicycle1.start()
bicycle1.ring_bell()
bicycle1.stop()

class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, num_wheels):
        super().__init__(maker, model, year)
        self.num_wheels = num_wheels


motorcycle1 = Motorcycle("Yamaha", "R7", 2023, 2)

print(motorcycle1.num_wheels)
motorcycle1.start()
motorcycle1.stop()

# class Employee:
#     increase = 1.04
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} earns {self.salary} '
    
#     def increase_salary(self):
#         self.salary = int(self.salary * self.increase)


# class Developer(Employee):
#     increase = 1.10
#     def __init__(self, first_name, last_name, salary, prog_lang):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = prog_lang
    
#     def __str__(self):
#         return f'{super().__str__()} and fav prog lang is {self.prog_lang}'

# emp1 = Employee('Alice', 'Ason', 45000)
# emp2 = Employee('Bob', 'Bson', 42000)
# dev1 = Developer('Carl', 'Cson', 50000, 'Python')

# print(emp1)
# print(emp2)
# print(dev1)

# emp1.increase_salary()
# emp2.increase_salary()
# dev1.increase_salary()

# print(emp1)
# print(emp2)
# print(dev1)