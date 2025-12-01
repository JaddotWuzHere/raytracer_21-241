from geometry import *
from util import *

SKYBOX = (125, 200, 255)
GROUND = (255, 255, 255)
LIGHT_POS = create_vector(2, 2, 0)

AMBIENT = 0.25
DIFFUSE = 1.0

# render skybox
def skyGradient(ray): # ret: (r, g, b)
    dir = normalize(ray.direction)
    y = dir[1]
    t = (y + 1) / 2  # vertical blending

    s_r = int((1 - t) * GROUND[0] + t * SKYBOX[0])
    s_g = int((1 - t) * GROUND[1] + t * SKYBOX[1])
    s_b = int((1 - t) * GROUND[2] + t * SKYBOX[2])

    return (s_r, s_g, s_b)

def colorHelper(n): # ret: float
    return (n + 1) / 2

# color normals
def colorSurfNorm(ray, objList): # ret: (r, g, b)
    N = normalVec(ray, objList)
    c_r = int(colorHelper(N[0]) * 255)
    c_g = int(colorHelper(N[1]) * 255)
    c_b = int(colorHelper(N[2]) * 255)
    return (c_r, c_g, c_b)

# shadows
def lambertianShade(ray, objList): # ret: (r, g, b)
    P, obj = intersectPt(ray, objList)
    N = normalize(P - obj.center)
    L = normalize(LIGHT_POS - P)
    diff = max(0, dot(N, L))
    brightness = AMBIENT + DIFFUSE * diff

    c_r = colorSurfNorm(ray, objList)[0]
    c_g = colorSurfNorm(ray, objList)[1]
    c_b = colorSurfNorm(ray, objList)[2]
    C_r = int(c_r * brightness)
    C_g = int(c_g * brightness)
    C_b = int(c_b * brightness)

    # clamping
    if C_r > 255: C_r = 255
    elif C_r < 0: C_r = 0
    if C_g > 255: C_g = 255
    elif C_g < 0: C_g = 0
    if C_b > 255: C_b = 255
    elif C_b < 0: C_b = 0

    return (C_r, C_g, C_b)