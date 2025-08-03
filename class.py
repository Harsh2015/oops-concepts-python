class Book():
    def __init__(self,author,title):
        self.author = author
        self.title = title

    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author:{self.author}')
        
new = Book('Atomic Habit','James Clear')
new.display_info()

        
        
        
        
        

                