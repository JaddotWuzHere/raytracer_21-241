from objects.sphere import Sphere
from util import *


class Scene:
    def __init__(self, objList):
        self.objList = objList

    def trace(self, ray):
        closest = None
        for obj in self.objList:
            hit = obj.intersect(ray)
            if hit is not None and (closest is None or hit.t < closest.t):
                closest = hit

        return closest

def makeSphere(center, radius):
    S = scale(radius)
    T = translation(center[0], center[1], center[2])
    M = T @ S
    M_inv = np.linalg.inv(M)
    return Sphere(M, M_inv)