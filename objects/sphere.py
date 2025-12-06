# |P-C|^2 = R^2
from geometry import *


class Sphere(Renderable):
    def __init__(self, M, M_inv, reflectivity):
        self.M = M
        self.M_inv = M_inv
        self.reflectivity = reflectivity

    def intersect(self, ray):
        t = calcHitObj(ray, self)

        if t is None or t <= 0:
            return None

        P = intersectPt(ray, t)
        N = normalVec(self, P)
        return HitRecord(t, P, N, self)