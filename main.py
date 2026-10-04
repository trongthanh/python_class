"""Week 9 — Luffy comes alive. Run this file; edit luffy.py in class."""
import pygame

from luffy import Luffy
from spritesheet import load_image

WIDTH = 240
HEIGHT = 160
SCALE = 3
LOOP_FPS = 60
FEET_Y = 126  # The top of the flat deck in assets/background.png.


def main():
    # No audio this week; these two modules are all we need to initialize.
    pygame.display.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
    pygame.display.set_caption("Week 9 - Luffy comes alive")
    # The 240 x 160 game canvas. This week the whole deck fits on it, so it is
    # also the WORLD surface that Luffy draws himself on. (Week 11: a camera.)
    screen = pygame.Surface((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 16)
    clock = pygame.time.Clock()
    background = load_image("background.png")
    # Give Luffy the surface when he is created; he keeps it for drawing.
    player = Luffy(screen, WIDTH // 2, FEET_Y)
    show_body = False

    running = True
    while running:
        dt = clock.tick(LOOP_FPS) / 1000  # Milliseconds -> seconds.
        dt = min(dt, 0.05)  # Supplied: don't skip lots of poses after a stall.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_F1:
                    show_body = not show_body

        keys = pygame.key.get_pressed()
        direction = player.read_direction(keys)
        player.move_horizontal(direction, WIDTH, dt)
        player.choose_animation(direction)
        player.update_animation(dt)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, "midnightblue", (0, 0, WIDTH, 53))
        screen.blit(font.render("Left/Right or A/D: walk", True, "white"), (8, 8))
        screen.blit(font.render("F1: body box | Esc: quit", True, "white"), (8, 23))
        label = "Pose: " + player.animation + " | facing: " + str(player.facing)
        screen.blit(font.render(label, True, "gold"), (8, 40))
        player.draw()  # No arguments: Luffy knows his surface and his pictures.
        if show_body:
            pygame.draw.line(screen, "cyan", (0, FEET_Y), (WIDTH, FEET_Y))
            pygame.draw.rect(screen, "cyan", player.rect, 1)
            pygame.draw.circle(screen, "yellow", player.rect.midbottom, 2)
        pygame.draw.rect(screen, "midnightblue", (0, 141, WIDTH, 19))
        screen.blit(font.render("Explore the deck! Jump: next week", True, "white"), (8, 144))

        # Nearest-neighbour scaling keeps the original pixel art sharp.
        pygame.transform.scale(screen, window.get_size(), window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
