class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
    def shape(self):
        pass

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        return f"This is a circle\n{self.draw()}"
        
    def draw(self):
        return f'''
({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '''  

class Square(Base):
    def shape(self):
        return "Square"
        
    def draw(self):
        return f'''
({self.x}, {self.y}) {self.size}
+{'-' * self.size}+
|{' ' * self.size}|
+{'-' * self.size}+
'''

def main():
    c = Circle(2, 2, 1)
    print(c.shape())

main()
