"""shapes_w_args"""
import sys

class Shape():
    """Shapes are all shapey."""
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Triangle(Shape):  # Class Triangle inherits from Shape
    """Triangles have three corners"""
    def area(self):
        return self.height * self.width / 2.
    
class Rectangle(Shape):
    """Rectangles can be square if they try really hard."""
    def area(self):
        return self.height * self.width

if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print "Usage: shapes_w_args height, width"
    else:
        height = int(sys.argv[1]) # Supplies!
        width = int(sys.argv[2])
    print "Triangle area: {}".format(Triangle(height,width).area())
    print "Rectangle area: {}".format(Rectangle(height,width).area())
