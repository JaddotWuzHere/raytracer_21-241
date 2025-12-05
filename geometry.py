# calculations regarding 3d shapes
from dataclasses import dataclass

import numpy as np

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

def calcHitObj(ray, sphere): # ret: float or None
    O = ray.origin
    D = ray.direction

    OMatr = np.array([O[0], O[1], O[2], 1.0])
    DMatr = np.array([D[0], D[1], D[2], 0.0])

    OLocMatr = sphere.M_inv @ OMatr
    DLocMatr = sphere.M_inv @ DMatr

    OLoc = OLocMatr[:3]
    DLoc = DLocMatr[:3]

    C = ORIGIN
    R = 1
    oc = OLoc - C

    a = dot(DLoc, DLoc)
    b = 2 * (dot(oc, DLoc))
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

def normalVec(obj, PWrld):
    PWrldMatr = np.array([PWrld[0], PWrld[1], PWrld[2], 1.0])
    PLocMatr = obj.M_inv @ PWrldMatr
    PLoc = PLocMatr[:3]

    NLoc = normalize(PLoc)
    NLocMatr = np.array([NLoc[0], NLoc[1], NLoc[2], 0.0])
    NWrldMatr = obj.M @ NLocMatr
    NWrld = normalize(NWrldMatr[:3])

    return NWrld