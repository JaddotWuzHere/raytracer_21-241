# draws the window thing
from geometry import *
from util import *

SKYBOX = (255, 255, 255)
LIGHT_POS = create_vector(2, 2, 0)

AMBIENT = 0.25
DIFFUSE = 1.0

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
    diff = max(0, dot(N, L))
    brightness = AMBIENT + DIFFUSE * diff
    c_r = colorSurfNorm(ray, sphere)[0]
    c_g = colorSurfNorm(ray, sphere)[1]
    c_b = colorSurfNorm(ray, sphere)[2]
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