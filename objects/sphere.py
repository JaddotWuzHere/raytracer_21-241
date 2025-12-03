# |P-C|^2 = R^2
from geometry import *


class Sphere(Renderable):
    def __init__(self, center, radius):
        self.center = center # vector3d
        self.radius = radius # float

    def intersect(self, ray):
        t = calcHitObj(ray, self)

        if t is None or t <= 0:
            return None

        P = intersectPt(ray, t)
        N = normalVec(ray, t, self, P)
        return HitRecord(t, P, N, self)