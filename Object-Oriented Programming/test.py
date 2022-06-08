# class Employee:
    
#     number_of_employees = 0
#     average_age = 0
#     average_salary = 0
    
#     total_age = 0
#     total_salary = 0

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         Employee.number_of_employees += 1
#         Employee.total_salary += self.salary
#         Employee.total_age += self.age
#         Employee.average_age = Employee.total_age / Employee.number_of_employees
#         Employee.average_salary = Employee.total_salary / Employee.number_of_employees

class Temperature:
    
    min_temperature = 0
    max_temperature = 1000
    
    def __init__(self, kelvin):
        self._kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, temp):
        if temp > Temperature.min_temperature:
            raise Exception("Invalid temperature.")
        Temperature.min_temperature = temp

    @classmethod
    def update_max_temperature(cls, temp):
        if temp < Temperature.min_temperature:
            raise Exception("Invalid temperature.")

    
    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, kelvin):
        if kelvin < Temperature.min_temperature or kelvin > Temperature.max_temperature:
            raise Exception("Invalid temperature.")
        self._kelvin = kelvin