# math stuff
# vectors are 3d
import math

import numpy as np


# vector stuff
ORIGIN = np.array([0.0, 0.0, 0.0])

def create_vector(x, y, z): # ret: vector3d
    return np.array([x, y, z], dtype=float)

def copy_vector(v): # ret: vector3d
    return create_vector(v[0], v[1], v[2])

def dot(v1, v2): # ret: vector3d
    return np.dot(v1, v2)

def cross(a, b): # ret: matrix
    return np.cross(a, b)

def length(v): # ret: float
    return np.linalg.norm(v)

def normalize(v): # ret: unit vector3d
    norm = length(v)
    v_u = v / norm
    return v_u

# algebra stuff
def discriminant(a, b, c): # ret: float
    return b ** 2 - (4 * a * c)

def findRoots(a, b, c, pm): # ret: float
    discr = discriminant(a, b, c)
    if pm >= 0:
        return (-b + math.sqrt(discr)) / (2 * a)
    else:
        return (-b - math.sqrt(discr)) / (2 * a)

# matrix stuff
def translation(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype = float)

def scale(s):
    return np.array([
        [s, 0, 0, 0],
        [0, s, 0, 0],
        [0, 0, s, 0],
        [0, 0, 0, 1]
    ], dtype = float)