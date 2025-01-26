from sys import exit
from time import time

import pygame

from ui import Text

SCREEN_SIZE = 300, 200
CENTER = SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2


def main():

    pygame.init()
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

    flags = pygame.DOUBLEBUF
    pygame.display.set_caption('Tap BPM')
    screen = pygame.display.set_mode(SCREEN_SIZE, flags, depth=8, vsync=1)

    clock = pygame.time.Clock()

    label = Text(screen, 100, pos=CENTER, center_align=True)

    last_time = time()

    running = 1

    bpm = 120

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    t = time() - last_time
                    last_time = time()
                    bpm = round(60 / t)

        screen.fill('black')

        label.update(bpm)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
