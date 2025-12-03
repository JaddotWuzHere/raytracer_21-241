from ray import Ray
from util import *

WORLD_UP = create_vector(0, 1, 0)

def rotateAroundAxis(v, axis, angle):
    ax = normalize(axis)
    vParallel = ax * dot(ax, v)
    vPerp = v - vParallel

    vRot = vPerp * math.cos(angle) + cross(ax, vPerp) * math.sin(angle)
    return vParallel + vRot

class Camera:
    def __init__(self, pos, lookAt, imgWidth, imgHeight, focalLength):
        self.pos = pos # vector3d
        self.imgWidth = imgWidth # int
        self.imgHeight = imgHeight # int
        self.focalLength = focalLength # float
        self.aspectRatio = imgWidth / imgHeight #float

        self.forward = normalize(lookAt - pos)
        self.right = normalize(cross(self.forward, WORLD_UP))
        self.up = normalize(cross(self.right, self.forward))

    def genRay(self, i, j): # ret: vector3d
        # clamping [0, 1]%
        u = (i + 0.5) / self.imgWidth
        v = (j + 0.5) / self.imgHeight

        # mapping [-1, 1]
        x = (2 * u - 1) * self.aspectRatio
        y = 1 - 2 * v

        forwardComponent = self.forward * self.focalLength
        rightComponent = self.right * x
        upComponent = self.up * y
        direction = forwardComponent + rightComponent + upComponent
        D = normalize(direction)

        R = Ray(self.pos, D)
        return R

    def moveDepth(self, amt):
        self.pos += self.forward * amt

    def moveHorizontal(self, amt):
        self.pos += self.right * amt

    def moveVertical(self, amt):
        self.pos += self.up * amt

    def yaw(self, angle):
        axis = WORLD_UP
        newForward = rotateAroundAxis(self.forward, axis, angle)
        newRight = rotateAroundAxis(self.right, axis, angle)
        self.forward = normalize(newForward)
        self.right = normalize(newRight)
        self.up = normalize(cross(newRight, newForward))

    def pitch(self, angle):
        axis = self.right
        newForward = rotateAroundAxis(self.forward, axis, angle)
        newUp = rotateAroundAxis(self.up, axis, angle)
        self.forward = normalize(newForward)
        self.right = normalize(cross(newForward, newUp))
        self.up = normalize(cross(self.right, newForward))
