import math

class Vector:
    """ A three element vector used in 3D graphics"""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z 
    
    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def mag(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        return self/mag(self)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x*other.x, self.y*other.y, self.z*other.z)
        else:
            return Vector(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x*other.x, self.y*other.y, self.z*other.z)
        else:
            return Vector(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other): # python3 / in python2, use __div__
        if isinstance(other, Vector):
            return Vector(self.x/other.x, self.y/other.y, self.z/other.z)
        else:
            return Vector(self.x/other, self.y/other, self.z/other)
