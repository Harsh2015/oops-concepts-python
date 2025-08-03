class Employee():
    def __init__(self,name, salary,programming_language):
        self.name = name
        self.salary = salary
        self.programming_language = programming_language
        
class Developer(Employee):
    def new(self):
        print(f'name: {self.name}')
        print(f'salary: {self.salary}')
        print(f'programming language: {self.programming_language}')
        
n = Developer('Harsh','80000','Python')
n.new()
        