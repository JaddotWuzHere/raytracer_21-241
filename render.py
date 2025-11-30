# draws the window thing
from camera import *
from geometry import intersectPt
from objects.sphere import Sphere
from util import *

SKYBOX = (255, 255, 255)

def renderGradient(camera, sphere, width, height):
    pixelBuf = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            R = camera.genRay(j, i)
            P = intersectPt(R, sphere)
            if P is SENTINEL:
                pixelBuf[i][j] = SKYBOX
            else:
                pixelBuf[i][j] = (0, 0, 255)
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