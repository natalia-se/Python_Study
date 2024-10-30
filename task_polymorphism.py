import math

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        return "Now we are calculating Aria "

    def perimeter(self):
        return "Now we are calculating Perimeter "


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(name = "circle", color = color)
        self.radius = radius

    def area(self):
        area = round(math.pi * self.radius ** 2, 2)
        print(f"Circle area: {area}")

    def perimeter(self):
        perimeter = round(2 * math.pi * self.radius, 2)
        print(f"Circle perimeter: {perimeter}")


circle1 = Circle(4, color="red")


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(name = "rectangle", color = color)
        self.width = width
        self.height = height

    def area(self):
        area =  self.height * self.width
        print(f"Rectangle area: {area}")

    def perimeter(self):
        perimeter =  2 * (self.height + self.width)
        print(f"Rectangle perimeter: {perimeter}")
    
rectangle1 = Rectangle(2, 4, "yellow")



class Triangle(Shape):
    def __init__(self, a, b, c, color="green"):
        super().__init__(name = "triangle", color = color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2  # Semi-perimeter
        aria = round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), 2)
        print(f"Triangle area: {aria}")
    
    def perimeter(self):
        perimeter = self.a + self.b + self.c
        print(f"Triangle perimeter: {perimeter}")
    
triangle1 = Triangle(2, 3, 4)


for s in (circle1, rectangle1, triangle1):
    s.area()
    s.perimeter()