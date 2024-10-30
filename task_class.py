# class Something:
#     def __init__(self, data:dict):
#         self.__dict__ = data
    
#     def __str__(self):
#         str_rep = " ".join([f'{key} = {value} ' for key, value in self.__dict__.items()])
#         return str_rep
#         # for key, value in self.__dict__.items():
#         #     str_rep += f'{key} = {value} '
#         # return str_rep
    


# data_dict1 = {
#     'a' : 10,
#     'b' : 20,
#     'name' : 'One'
# }

# data_dict2 = {
#     'c' : 15,
#     'd' : 25,
#     'name' : 'Two'
# }

# s1 = Something(data_dict1)
# s2 = Something(data_dict2)
# print(s1)
# print(s2)

# Define a Student Class:
# Define a class named Student with the following attributes:
# name: Name of the student (string).
# age: Age of the student (int).
# grade: Grade level of the student (int).
# Add Methods:
# Add the following methods to the Student class:
# get_info( ): Method to display the student's information.
# promote ( ): Method to promote the student to the next grade level.
# Test the Class:
# Create instances of the Student class and test its methods:
# Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
# Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information.

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
#     def get_info(self):
#         return f"Student {self.name} is {self.age} yeas old, {self.grade} grade"
    
#     def promote(self, grade):
#         self.grade = grade

# student1 = Student("Anna", 15, 9)

# print(student1.get_info())
# student1.promote(10)

# print(student1.get_info())

# class A:
#     def __init__(self, value):
#         print(f'In A.__init__ and value = {value}')
#         self.value = value
    
# class B(A):
#     def __init__(self, value):
#         print(f'In B.__init__ and value = {value}')
#         super().__init__(value)
#         self.value += 10

# class C(A):
#     def __init__(self, value):
#         print(f'In C.__init__ and value = {value}')
#         super().__init__(value)
#         self.value *= 4

# class D(B, C):
#     def __init__(self, value):
#         print(f'In D.__init__ and value = {value}')
#         super().__init__(value)   

# d = D(10)
# print(d.value)

