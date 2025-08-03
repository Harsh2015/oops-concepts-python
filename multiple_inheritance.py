class Writer():
    def write(self):
        print('writing a poetry...')
        
class Painter():
    def paint(self):
        print('Painting a landscape')
        
class Artist(Writer,Painter):
    def both(self):
        self.write()
        self.paint()
        
new = Artist()
new.both()
        
        
        