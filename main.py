from geomtery import intersectPt, normalVec, calcHit
from util import *
from objects.sphere import *
from objects.ray import *

v1 = create_vector(0, 0, -1)
o1 = create_vector(0, 0, 0)
d1 = create_vector(0, 0, -1)
s1 = Sphere(v1, 0.5)
r1 = Ray(o1, d1)
t_hit1 = calcHit(r1, s1)
p1 = intersectPt(r1, s1)
n1 = normalVec(r1, s1)

print("Test 1:")
print(f"{t_hit1}")
print(f"{p1}")
print(f"{n1}")

d2 = create_vector(0, 1, 0)
r2 = Ray(o1, d2)
t_hit2 = calcHit(r2, s1)
p2 = intersectPt(r2, s1)
n2 = normalVec(r2, s1)

print("Test 2:")
print(f"{t_hit2}")
print(f"{p2}")
print(f"{n2}")