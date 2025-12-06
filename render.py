# draw scene
from geometry import *
from ray import Ray
from util import *

SKYBOX = (125, 200, 255)
GROUND = (255, 255, 255)
LIGHT_POS = create_vector(5, 2, 0)

AMBIENT = 0.25
DIFFUSE = 1.0
SHINE = 20
DIFFUSE_COEF = 1.0
SPECULAR_COEF = 0.8
LIGHT_COLOR = (1.0, 1.0, 1.0)

DEPTH_MAX = 2
EPSILON = 1e-8

# for rendering the window, default sizes
DEFWIN_WIDTH = 1280
DEFWIN_HEIGHT = 720

def renderFrame(camera, scene, width, height):
    pixelBuf = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            ray = camera.genRay(j, i)
            pixelBuf[i][j] = traceRefl(ray, 0, scene, camera)
    return pixelBuf

def traceRefl(ray, depth, scene, camera):
    if depth > DEPTH_MAX:
        return skyGradient(ray)

    hit = scene.trace(ray)
    if hit is None:
        return skyGradient(ray)

    obj = hit.obj
    P = hit.point
    N = normalVec(obj, P)

    CLoc = lambertianShade(hit, camera)
    r = obj.reflectivity

    if r <= 0.0:
        return CLoc

    D = normalize(ray.direction)

    rDir = normalize(D - 2 * dot(D, N) * N)
    rOrig = P + EPSILON * rDir

    reflectRay = Ray(rOrig, rDir)

    CRefl = traceRefl(reflectRay, depth + 1, scene, camera)

    C_r = (1 - r) * CLoc[0] + r * CRefl[0]
    C_g = (1 - r) * CLoc[1] + r * CRefl[1]
    C_b = (1 - r) * CLoc[2] + r * CRefl[2]

    C_r = max(0, min(255, int(C_r)))
    C_g = max(0, min(255, int(C_g)))
    C_b = max(0, min(255, int(C_b)))

    C = (int(C_r), int(C_g), int(C_b))
    return C

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
def colorSurfNorm(N): # ret: (r, g, b)
    c_r = int(colorHelper(N[0]) * 255)
    c_g = int(colorHelper(N[1]) * 255)
    c_b = int(colorHelper(N[2]) * 255)
    return (c_r, c_g, c_b)

# shadows and specular
def lambertianShade(hit, camera):
    P = hit.point
    N = hit.normal

    L = normalize(LIGHT_POS - P)
    diff = max(0, dot(N, L))

    C = camera.pos
    V = normalize(C - P)
    H = normalize(L + V)
    specAngle = max(0.0, dot(N, H))
    spec = specAngle ** SHINE

    base_r_255, base_g_255, base_b_255 = colorSurfNorm(N)

    base_r = base_r_255 / 255.0
    base_g = base_g_255 / 255.0
    base_b = base_b_255 / 255.0

    ambient_r = AMBIENT * base_r
    ambient_g = AMBIENT * base_g
    ambient_b = AMBIENT * base_b

    diffuse_r = DIFFUSE_COEF * diff * base_r
    diffuse_g = DIFFUSE_COEF * diff * base_g
    diffuse_b = DIFFUSE_COEF * diff * base_b

    specular_r = SPECULAR_COEF * spec * LIGHT_COLOR[0]
    specular_g = SPECULAR_COEF * spec * LIGHT_COLOR[1]
    specular_b = SPECULAR_COEF * spec * LIGHT_COLOR[2]

    color_r = ambient_r + diffuse_r + specular_r
    color_g = ambient_g + diffuse_g + specular_g
    color_b = ambient_b + diffuse_b + specular_b

    color_r = max(0.0, min(1.0, color_r))
    color_g = max(0.0, min(1.0, color_g))
    color_b = max(0.0, min(1.0, color_b))

    C_r = int(color_r * 255.0)
    C_g = int(color_g * 255.0)
    C_b = int(color_b * 255.0)

    # DEPRECATED
    # c_r = colorSurfNorm(N)[0]
    # c_g = colorSurfNorm(N)[1]
    # c_b = colorSurfNorm(N)[2]
    # C_r = int(c_r * brightness)
    # C_g = int(c_g * brightness)
    # C_b = int(c_b * brightness)
    #
    # # clamping
    # if C_r > 255: C_r = 255
    # elif C_r < 0: C_r = 0
    # if C_g > 255: C_g = 255
    # elif C_g < 0: C_g = 0
    # if C_b > 255: C_b = 255
    # elif C_b < 0: C_b = 0

    return (C_r, C_g, C_b)



def writeBytes(pixels, width, height):
    byteBuf = bytearray(width * height * 3)
    k = 0
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            byteBuf[k] = r
            byteBuf[k + 1] = g
            byteBuf[k + 2] = b
            k += 3

    return byteBuf

# generate image file
def writePPM(filename, width, height, pixels):
    with open(filename + ".ppm", "w") as f:
        f.write(f"P3\n"
                f"{width} {height}\n"
                f"255\n")
        for i in range(height):
            for j in range(width):
                r, g, b = pixels[i][j]
                f.write(f"{r} {g} {b} \n")