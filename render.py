# draw scene
from scene import *

# for rendering the window, default sizes
DEFWIN_WIDTH = 1280
DEFWIN_HEIGHT = 720

def renderGradient(camera, objList, width, height): # ret: pixel array
    pixelBuf = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            ray = camera.genRay(j, i)

            C = skyGradient(ray)

            P, obj = intersectPt(ray, objList)
            if P is None:
                pixelBuf[i][j] = C
            else:
                pixelBuf[i][j] = lambertianShade(ray, objList)
    return pixelBuf

# generate file
def writePPM(filename, width, height, pixels):
    with open(filename + ".ppm", "w") as f:
        f.write(f"P3\n"
                f"{width} {height}\n"
                f"255\n")
        for i in range(height):
            for j in range(width):
                r, g, b = pixels[i][j]
                f.write(f"{r} {g} {b} \n")