class Car:
  def __init__(self, model, age):
    self.model = model
    self.age = age

  def __str__(self):
    return f"{self.model}({self.age})"
  
  def myfunc(self):
    print("Car: " + self.model)

car1 = Car("volvo", 1984)

print(car1)

car1.myfunc()