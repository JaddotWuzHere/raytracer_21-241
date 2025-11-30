# calculations regarding 3d shapes
from util import *


def calcHit(ray, sphere): # ret: float or SENTINEL
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
        return SENTINEL # no hit
    else:
        t1 = findRoots(a, b, c, 1)
        t2 = findRoots(a, b, c, -1)

        t_hit = SENTINEL
        if t1 > 0: t_hit = t1
        if t2 > 0 and (t_hit is SENTINEL or t2 < t_hit):
            t_hit = t2

        return t_hit

def intersectPt(ray, sphere): # ret: vector3d or SENTINEL
    t_hit = calcHit(ray, sphere)
    if t_hit is SENTINEL:
        return SENTINEL # no point
    O = ray.origin
    D = ray.direction

    P = O + t_hit * D
    return P

def normalVec(ray, sphere): # ret: vector3d or SENTINEL
    P = intersectPt(ray, sphere)
    if P is SENTINEL:
        return SENTINEL # no vector
    assert P is not SENTINEL
    C = sphere.center

    N = normalize(P - C)
    return N