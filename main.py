"""Week 11 — run this file. This week's TODOs are in world.py.

main.py only runs the loop. The World owns the ship, Luffy and the camera.
"""
import pygame

from world import HEIGHT, WIDTH, World

SCALE = 3
LOOP_FPS = 60


def main():
    pygame.display.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE), vsync=True)
    pygame.display.set_caption("Week 11 - The first ship scene scrolls")
    screen = pygame.Surface((WIDTH, HEIGHT))  # Only the SCREEN now, not the world.
    clock = pygame.time.Clock()
    world = World()  # Loads the ship, builds its floor, creates Luffy and the camera.

    running = True
    while running:
        dt = min(clock.tick(LOOP_FPS) / 1000, 0.05)
        events = pygame.event.get()  # Collect ONCE; never drain it inside Luffy.
        player_events = []
        reset_requested = False

        # Main owns window, debug views and restart. Luffy owns Space.
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                world.debug = not world.debug
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                world.show_map = not world.show_map
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_requested = True
            else:
                player_events.append(event)
        if not running:
            break
        if reset_requested:
            world.reset()
            player_events = []  # Do not apply old presses to the new Luffy.

        keys = pygame.key.get_pressed()
        world.update(dt, keys, player_events)
        world.draw(screen)
        pygame.transform.scale(screen, window.get_size(), window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
