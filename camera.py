from objects.ray import Ray
from util import *

class Camera:
    def __init__(self, origin, imgWidth, imgHeight, planeDepth):
        self.origin = origin # vector3d
        self.imgWidth = imgWidth # int
        self.imgHeight = imgHeight # int
        self.planeDepth = planeDepth # float
        self.aspectRatio = imgWidth / imgHeight #float

    def genRay(self, i, j): # ret: vector3d
        # clamping [0, 1]%
        u = (i + 0.5) / self.imgWidth
        v = (j + 0.5) / self.imgHeight

        # mapping [-1, 1]
        x = (2 * u - 1) * self.aspectRatio
        y = 1 - 2 * v

        P = create_vector(x, y, -self.planeDepth)
        rawD = P - self.origin
        D = normalize(rawD)

        R = Ray(self.origin, D)
        return R