# draws the window thing
from geometry import *
from util import *

SKYBOX = (255, 255, 255)
LIGHT_POS = create_vector(2, 2, 0)
SHADOW_STR = 0.85 # [0, 1]

def renderGradient(camera, sphere, width, height):
    pixelBuf = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            ray = camera.genRay(j, i)
            P = intersectPt(ray, sphere)
            if P is SENTINEL:
                pixelBuf[i][j] = SKYBOX
            else:
                pixelBuf[i][j] = lambertianShade(ray, sphere)
    return pixelBuf

def colorHelper(n): # ret: float
    return (n + 1) / 2

# color normals
def colorSurfNorm(ray, sphere): # ret: (r, g, b)
    N = normalVec(ray, sphere)
    c_r = int(colorHelper(N[0]) * 255)
    c_g = int(colorHelper(N[1]) * 255)
    c_b = int(colorHelper(N[2]) * 255)
    return (c_r, c_g, c_b)

# shadows
def lambertianShade(ray, sphere): # ret: (r, g, b)
    P = intersectPt(ray, sphere)
    N = normalize(P - sphere.center)
    L = normalize(LIGHT_POS - P)
    diff = max((1 - SHADOW_STR), dot(N, L))
    c_r = int(colorSurfNorm(ray, sphere)[0] * diff)
    c_b = int(colorSurfNorm(ray, sphere)[1] * diff)
    c_g = int(colorSurfNorm(ray, sphere)[2] * diff)
    return (c_r, c_g, c_b)

# generate file
def writePPM(filename, width, height, pixels):
    with open(filename + ".ppm", "w") as f:
        f.write(f"P3\n"
                f"{width} {height}\n"
                f"255\n")
        for i in range(height):
            for j in range(width):
                r, g, b = pixels[i][j]
                f.write(f"{r} {g} {b}\n")