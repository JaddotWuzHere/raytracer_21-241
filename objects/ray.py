# r(t) = O + tD

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin # vector3d
        self.direction = direction # unit vector3d

def at(self, t): # ret: vector3d
    return self.origin + t * self.direction # vector3d

