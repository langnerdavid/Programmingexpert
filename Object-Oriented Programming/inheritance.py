class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")


class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary


    def say_hello(self):
        super().say_hello()
        print(f"My salaray is {self.salary}")

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


o = Owner("Tim", "Programmer", 50000)
o.say_hello()
#print(isinstance(o, Owner))



class A:
    def __init__(self):
        print("A")
  
class B:
    def __init__(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()