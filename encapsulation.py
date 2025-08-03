class Student():
    def __init__(self):
        self.__marks = 0 # Private Variable
        
    def set_marks(self,m):
        if m > 0 and m <= 100:
            self.__marks = m
            print('Marks Updated...!')
            print(f'Student marks {self.__marks}')
        else:
            print('Invalid Marks')
            
    def get_marks(self):
        return self.__marks
    
new = Student()

new.set_marks(90)
print(new.get_marks())
print(new.__marks) # Accessing Private Variable Throw "AttributeError" 
        