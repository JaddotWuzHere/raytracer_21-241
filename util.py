# basic vector math stuff
# vectors are represented with 3 components: x y and z
import numpy as np

EPSILON = 1e-8

# for rendering the window, default values
DEFWIN_WIDTH = 1280
DEFWIN_HEIGHT = 720


def create_vector(x, y, z):
    return np.array([x, y, z], dtype=float)

def copy_vector(v):
    return create_vector(v[0], v[1], v[2])

def dot(v1, v2):
    return np.dot(v1, v2)

def cross(a, b):
    return np.cross(a, b)

def length(v):
    return np.linalg.norm(v)

def normalize(v):
    norm = length(v)
    if norm <= EPSILON:
        return np.array([0, 0, 0], dtype=float)
    else:
        v_u = v / norm
        return v_u

