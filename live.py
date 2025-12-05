# live camera!!
import numpy as np
import pygame

from camera import Camera
from render import *
from scene import Scene, makeSphere, projPt
from util import *

WIDTH = 320
HEIGHT = 180

# for wireframe stuff
CUBE_VERTICES = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
]

CUBE_EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

# camera speed, def = 3.0
SPEED = 3.0
# mouse sensitivity, def = 0.003
SENS = 0.003
# mouse center
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

def camInput(camera, seconds):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        camera.moveDepth(+SPEED * seconds)
    if keys[pygame.K_s]:
        camera.moveDepth(-SPEED * seconds)

    if keys[pygame.K_d]:
        camera.moveHorizontal(+SPEED * seconds)
    if keys[pygame.K_a]:
        camera.moveHorizontal(-SPEED * seconds)

    if keys[pygame.K_SPACE]:
        camera.moveVertical(+SPEED * seconds)
    if keys[pygame.K_LSHIFT]:
        camera.moveVertical(-SPEED * seconds)

    # disable "vectoring"
    # if length(move) > 0.0:
    #     move = normalize(move)
    #     camera.pos += move * SPEED * seconds

def mouseLook(camera):
    dx, dy = pygame.mouse.get_rel()

    camera.yaw(-dx * SENS)
    camera.pitch(-dy * SENS)

    pygame.mouse.set_pos(CENTER_X, CENTER_Y)

def buildScene():
    s1 = makeSphere(create_vector(0, 0, -3), 1)
    return Scene([s1])

def buildCamera():
    return Camera(ORIGIN, create_vector(0, 0, -1), WIDTH, HEIGHT, 1)

def wireframe(screen, camera):
    center = ORIGIN
    scale = 1.0

    projected = []
    for (x, y, z) in CUBE_VERTICES:
        wx = center[0] + x * scale
        wy = center[1] + y * scale
        wz = center[2] + z * scale
        PWrld = create_vector(wx, wy, wz)

        pos2D, _ = projPt(PWrld, camera, WIDTH, HEIGHT)
        projected.append(pos2D)
    for i, j in CUBE_EDGES:
        ax, ay = projected[i]
        bx, by = projected[j]
        pygame.draw.line(screen, (255, 255, 255), (ax, ay), (bx, by))

def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    pygame.mouse.set_pos(CENTER_X, CENTER_Y)
    pygame.mouse.get_rel()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    scene = buildScene()
    camera = buildCamera()

    running = True
    while running:
        seconds = clock.tick(30) / 1000
        if seconds > 0:
            print("FPS:", 1 / seconds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        camInput(camera, seconds)
        mouseLook(camera)

        pixels = renderFrame(camera, scene, WIDTH, HEIGHT)
        byteBuf = writeBytes(pixels, WIDTH, HEIGHT)

        surf = pygame.image.frombuffer(byteBuf, (WIDTH, HEIGHT), "RGB")
        screen.blit(surf, (0, 0))

        wireframe(screen, camera)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()