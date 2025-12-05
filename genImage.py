from camera import Camera
from objects.sphere import Sphere
from render import *
from scene import Scene, makeSphere
from util import *


def buildScene():
    s1 = makeSphere(create_vector(0, 0, -3), 1)
    return Scene([s1])

def buildCamera():
    return Camera(ORIGIN, create_vector(0, 0, -1), DEFWIN_WIDTH, DEFWIN_HEIGHT, 1)

def main():
    camera = buildCamera()
    scene = buildScene()
    pixels = renderFrame(camera, scene, DEFWIN_WIDTH, DEFWIN_HEIGHT)

    writePPM("output", DEFWIN_WIDTH, DEFWIN_HEIGHT, pixels)

if __name__ == "__main__":
    main()