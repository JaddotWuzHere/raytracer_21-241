from camera import Camera
from objects.sphere import Sphere
from render import *
from scene import Scene
from util import *

S1 = Sphere(create_vector(0, 0, -3), 1)
S2 = Sphere(create_vector(-1, 0, -2), 1)
S3 = Sphere(create_vector(-2, 0, -1), 1)

scene = Scene([S1, S2, S3])

cam = Camera(ORIGIN, create_vector(0, 0, -1), DEFWIN_WIDTH, DEFWIN_HEIGHT, 1)

pixels = renderFrame(cam, scene, DEFWIN_WIDTH, DEFWIN_HEIGHT)
writePPM("output", DEFWIN_WIDTH, DEFWIN_HEIGHT, pixels)