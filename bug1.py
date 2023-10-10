
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
        return "This is a circle"
        
    def draw(self):
        return f'''
({self.x}, {self.y}) {self.size}
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
       ' - , _ _ _ ,  '
'''

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
    s = Square(1, 2, 3)
    print(s.shape())
    print(s.draw())

main()
