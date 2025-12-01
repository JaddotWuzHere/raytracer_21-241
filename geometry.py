# calculations regarding 3d shapes
from util import *


def calcHit(ray, objList): # ret: (float, sphere) or (None, None)
    t_hit = None
    obj = None
    for i in objList:
        t = calcHitObj(ray, i)
        if t is not None and (t_hit is None or t < t_hit):
            t_hit = t
            obj = i

    return (t_hit, obj)

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

def intersectPt(ray, objList): # ret: (vector3d, obj) or (None, None)
    t_hit, obj = calcHit(ray, objList)
    if t_hit is None:
        return (None, None)
    O = ray.origin
    D = ray.direction
    P = O + t_hit * D

    return (P, obj)

def normalVec(ray, objList): # ret: vector3d or None
    P, obj = intersectPt(ray, objList)
    if P is None:
        return None
    C = obj.center
    N = normalize(P - C)

    return N