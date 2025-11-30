# main
from util import *
from render import *

pixels = renderGradient(DEFWIN_WIDTH, DEFWIN_HEIGHT)
writePPM("output", DEFWIN_WIDTH, DEFWIN_HEIGHT, pixels)