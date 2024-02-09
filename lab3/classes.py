#1
class String():
    def __init__(self):
        self.str = ""

    def get_String(self):
        self.str = input()

    def print_String(self):
        print(self.str.upper())

str = String()
str.get_String()
str.print_String()

#2
class Shape():
    def __init__(self):
        self._area = 0
    def area(self):
        return self._area

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        
    def calculate_area(self):
        self.area = self.length ** 2
        return self.area
    
length = int(input())
square = Square(length)
print(square.calculate_area())    

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def compute_area(self):
        self._area = self.length * self.width
        return self._area
    
length = int(input())
width = int(input())
rectangle = Rectangle(length, width)

print(rectangle.compute_area()) 

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
# Example:
x = 1  
y = 2  
x1 = 4  
y1 = 6  
point1 = Point(x, y)
point2 = Point(x1, y1)
print("Original position of point 1:", point1.show())
print("Distance between point 1 and point 2:", point1.dist(point2))
point1.move(3, 5)
print("New position of point 1:", point1.show())
print("New distance between point 1 and point 2:", point1.dist(point2))

#5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, deposit):
        self.balance += deposit
        return self.balance
    def withdrawals(self, withdrawal):
        if self.balance < withdrawal:
            return f"You have only left {self.balance}"
        else:
            self.balance -= withdrawal
            return self.balance
a1 = Account("Aray", 500)
print(a1.deposit(500))
print(a1.withdrawals(1999))
print(a1.withdrawals(2))

#6
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pn = list(filter(lambda x : x > 1 and all(x % y != 0 for y in range (2, int(x / 2) + 1)), numbers))
print(pn)  

