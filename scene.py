from objects.sphere import Sphere
from util import *


class Scene:
    def __init__(self, objList):
        self.objList = objList

    def trace(self, ray):
        closest = None
        for obj in self.objList:
            hit = obj.intersect(ray)
            if hit is not None and (closest is None or hit.t < closest.t):
                closest = hit

        return closest

def makeSphere(center, radius):
    S = scale(radius)
    T = translation(center[0], center[1], center[2])
    M = T @ S
    M_inv = np.linalg.inv(M)
    return Sphere(M, M_inv)

def projPt(PWrld, camera, width, height):
    V = camera.createViewMatr()
    P = camera.createProjMatr()

    PWrldMatr = np.array([PWrld[0], PWrld[1], PWrld[2], 1.0])

    PCam = V @ PWrldMatr
    PClip = P @ PCam

    #homogenous divide
    xndc = PClip[0] / PClip[3]
    yndc = PClip[1] / PClip[3]
    zndc = PClip[2] / PClip[3]

    screenX = (xndc + 1) * 0.5 * width
    screenY = (1 - yndc) * 0.5 * height

    return (screenX, screenY), zndc

