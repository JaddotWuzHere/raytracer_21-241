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