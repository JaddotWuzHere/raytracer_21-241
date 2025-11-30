# draws the window thing
from camera import *
from geometry import intersectPt, normalVec
from objects.sphere import Sphere
from util import *

SKYBOX = (255, 255, 255)

def renderGradient(camera, sphere, width, height):
    pixelBuf = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            ray = camera.genRay(j, i)
            P = intersectPt(ray, sphere)
            if P is SENTINEL:
                pixelBuf[i][j] = SKYBOX
            else:
                pixelBuf[i][j] = colorSurfNorm(ray, sphere)
    return pixelBuf

def writePPM(filename, width, height, pixels):
    with open(filename + ".ppm", "w") as f:
        f.write(f"P3\n"
                f"{width} {height}\n"
                f"255\n")
        for i in range(height):
            for j in range(width):
                r, g, b = pixels[i][j]
                f.write(f"{r} {g} {b}\n")

def colorHelper(n):
    return (n + 1) / 2

def colorSurfNorm(ray, sphere):
    N = normalVec(ray, sphere)
    c_r = int(colorHelper(N[0]) * 255)
    c_g = int(colorHelper(N[1]) * 255)
    c_b = int(colorHelper(N[2]) * 255)
    return (c_r, c_g, c_b)