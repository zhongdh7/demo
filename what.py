print("hello world")
for i in range(5):
    print(i)
if 3 > 2:
    print("3 is greater than 2")
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"My name is {self.name}."
person = Person("Bob")
print(person.introduce())
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
with open("example.txt", "w") as file:
    file.write("This is an example file.")
import math
print(math.sqrt(16))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
import os
os.system("pause")  