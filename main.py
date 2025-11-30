from camera import Camera
from objects.sphere import Sphere
from render import *
from util import *

o = create_vector(0, 0, -3)
S = Sphere(o, 0.5)
cam = Camera(ORIGIN, DEFWIN_WIDTH, DEFWIN_HEIGHT, 1)

pixels = renderGradient(cam, S, DEFWIN_WIDTH, DEFWIN_HEIGHT)
writePPM("output", DEFWIN_WIDTH, DEFWIN_HEIGHT, pixels)