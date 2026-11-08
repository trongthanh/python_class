"""Week 10 — run this file; edit the four steps in luffy.py."""
from pathlib import Path

import pygame

from luffy import Luffy

ASSETS = Path(__file__).resolve().parent / "assets"

WIDTH = 240
HEIGHT = 160
SCALE = 3
LOOP_FPS = 60
FEET_Y = 126
START_X = 60


def main():
    pygame.display.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
    pygame.display.set_caption("Week 10 - Jump and land")
    screen = pygame.Surface((WIDTH, HEIGHT))  # Still the whole world, until Week 11.
    font = pygame.font.Font(None, 12)
    clock = pygame.time.Clock()
    background = pygame.image.load(str(ASSETS / "background.png")).convert()

    # Supplied collision geometry, NOT colors read from the picture.
    platforms = [pygame.Rect(0, FEET_Y, WIDTH, HEIGHT - FEET_Y)]
    floating_platforms = [pygame.Rect(148, 94, 64, 6)]
    player = Luffy(screen, START_X, FEET_Y,
                   platforms=platforms, floating_platforms=floating_platforms)
    show_debug = False

    running = True
    while running:
        dt = min(clock.tick(LOOP_FPS) / 1000, 0.05)
        events = pygame.event.get()  # Collect ONCE; never drain it inside Luffy.
        player_events = []
        reset_requested = False

        # Main owns window, debug and restart. Luffy owns Space.
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                show_debug = not show_debug
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_requested = True
            else:
                player_events.append(event)
        if not running:
            break
        if reset_requested:
            player = Luffy(screen, START_X, FEET_Y,
                           platforms=platforms, floating_platforms=floating_platforms)
            player_events = []  # Do not apply old-scene presses to the new player.

        keys = pygame.key.get_pressed()
        player.update(dt, keys, player_events)

        screen.blit(background, (0, 0))
        for platform in floating_platforms:
            pygame.draw.rect(screen, "saddlebrown", platform)
            pygame.draw.line(screen, "burlywood", platform.topleft,
                             platform.topright, 2)
        player.draw()

        if show_debug:
            for platform in platforms + floating_platforms:
                pygame.draw.rect(screen, "lime", platform, 1)
            pygame.draw.rect(screen, "cyan", player.rect, 1)
            pygame.draw.circle(screen, "yellow", player.rect.midbottom, 2)

            # Orange = drawn picture, cyan = body, yellow = foot anchor.
            frame = player.animations[player.animation][player.frame_index]
            foot_x, foot_y = frame["pivot"]
            if player.facing != player.sheet.source_facing:
                foot_x = frame["image"].get_width() - 1 - foot_x
            picture = pygame.Rect((player.rect.centerx - foot_x,
                                   player.rect.bottom - foot_y),
                                  frame["image"].get_size())
            pygame.draw.rect(screen, "orange", picture, 1)
            count = len(player.animations[player.animation])
            label = player.animation + " " + str(player.frame_index + 1) + "/" + str(count)
            screen.blit(font.render(label, True, "white"), (6, 4))
            label = "vy: " + str(round(player.vy)) + " | grounded: " + str(player.on_ground)
            screen.blit(font.render(label, True, "white"), (6, 15))

        pygame.draw.rect(screen, "midnightblue", (0, 141, WIDTH, 19))
        screen.blit(font.render("Arrows/A-D: move | Space: jump | F1: boxes", True, "white"), (6, 143))
        screen.blit(font.render("R: restart | Esc: quit", True, "gold"), (6, 152))
        pygame.transform.scale(screen, window.get_size(), window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
