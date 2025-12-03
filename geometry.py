# calculations regarding 3d shapes
from dataclasses import dataclass

from util import *

@dataclass
class HitRecord:
    t: float
    point: any
    normal: any
    obj: "Renderable"

class Renderable:
    def intersect(self, ray) -> HitRecord | None:
        raise NotImplementedError


# DEPRECATED
# returns both the distance and obj from which the ray was hit
# def calcHit(ray, objList): # ret: (float, sphere) or (None, None)
#     t_hit = None
#     obj = None
#     for i in objList:
#         t = calcHitObj(ray, i)
#         if t is not None and (t_hit is None or t < t_hit):
#             t_hit = t
#             obj = i
#
#     return (t_hit, obj)

# for individual obj calculation
def calcHitObj(ray, sphere): # ret: float or None
    O = ray.origin
    D = ray.direction
    C = sphere.center
    R = sphere.radius
    oc = O - C

    a = dot(D, D)
    b = 2 * (dot(oc, D))
    c = dot(oc, oc) - R ** 2
    discr = discriminant(a, b, c)
    if discr < 0:
        return None # no hit
    else:
        t1 = findRoots(a, b, c, 1)
        t2 = findRoots(a, b, c, -1)

        t_hit = None
        if t1 > 0: t_hit = t1
        if t2 > 0 and (t_hit is None or t2 < t_hit):
            t_hit = t2

        return t_hit

def intersectPt(ray, t_hit): # ret: vector3d or None
    if t_hit is None:
        return None
    O = ray.origin
    D = ray.direction
    P = O + t_hit * D

    return P

def normalVec(ray, t_hit, obj, P): # ret: vector3d or None
    if P is None:
        return None
    C = obj.center
    N = normalize(P - C)

    return N