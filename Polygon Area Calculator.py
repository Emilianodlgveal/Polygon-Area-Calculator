class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        x = f'Rectangle(width={self.width}, height={self.height})'
        return x
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return self.width*2+self.height*2
    
    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big to picture.'
        else:
            return ('*'*self.width+'\n')*self.height
    
    def get_amount_inside(self, figure):
        x = str(self.width/figure.width)[0]
        y = str(self.height/figure.height)[0]
        if int(x) and int(y) > 1:
            return int(x)*int(y)
        else:
            return 0
    
class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side
    
    def __str__(self):
        x = f'Square(side={self.side})'
        return x
    
    def set_side(self, side):
        self.side = side
    
    def set_width(self, width):
        self.side = width
    
    def set_height(self, height):
        self.side = height
        
        
rec = Rectangle(64,122)
rec.set_width(7)
rec.set_height(3)
print(rec.get_picture())

sqr = Square(2)
sqr.set_side(2)
print(sqr.get_picture())
    
    
    
