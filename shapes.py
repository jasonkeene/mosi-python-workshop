# shapes.py
class Shape():
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Triangle(Shape):  # Class Triangle inherits from Shape
   def area(self):
        return self.height * self.width / 2.
    
class Rectangle(Shape):
    def area(self):
        return self.height * self.width

        
if __name__ == "__main__":
    r = Rectangle(3,4)  # the arguments go to the parent class's init
    t = Triangle(3,4)
    print r.area(), t.area() # both objects have area methods.