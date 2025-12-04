# live camera!!
import pygame

from camera import Camera
from objects.sphere import Sphere
from render import *
from scene import Scene
from util import *


# camera speed, def = 3.0
SPEED = 3.0
# mouse sensitivity, def = 0.003
SENS = 0.003
# mouse center
CENTER_X, CENTER_Y = DEFWIN_WIDTH // 2, DEFWIN_HEIGHT // 2

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
    s1 = Sphere(create_vector(-2, 0, -1), 1)
    s2 = Sphere(create_vector(-1, 0, -2), 1)
    return Scene([s1, s2])

def buildCamera():
    return Camera(ORIGIN, create_vector(0, 0, -1), DEFWIN_WIDTH, DEFWIN_HEIGHT, 1)

def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    pygame.mouse.set_pos(CENTER_X, CENTER_Y)
    pygame.mouse.get_rel()

    screen = pygame.display.set_mode((DEFWIN_WIDTH, DEFWIN_HEIGHT))
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

        pixels = renderFrame(camera, scene, DEFWIN_WIDTH, DEFWIN_HEIGHT)
        byteBuf = writeBytes(pixels, DEFWIN_WIDTH, DEFWIN_HEIGHT)

        surf = pygame.image.frombuffer(byteBuf, (DEFWIN_WIDTH, DEFWIN_HEIGHT), "RGB")
        screen.blit(surf, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()