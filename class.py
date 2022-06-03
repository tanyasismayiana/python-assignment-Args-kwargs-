pI=22/7 or 3.14
from cmath import pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*self.radius    
    def area(self):
        return self.radius**2*3.14 
class Square:
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side    
    def area(self):
        return self.side**2  
class Rectangle:
    def __init__(self,length,width):
        self .length=length
        self.width=width
    def perimeter(self):
        return 2*( self.length+self.width )
    def area(self):
        return self.length*self.width 
class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def surface_area(self):    
        surface_area= (4*3.14)+(4*self.radius**2)
        return surface_area
    def volume(self):
       volume =4 / 3*(3.14*self.radius)+(self.radius**3)       
       return volume