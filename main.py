"""Run this file. Edit luffy.py (Steps 1–3, 5) and world.py (Step 4)."""
import pygame

from world import HEIGHT, WIDTH, World

SCALE = 3
LOOP_FPS = 60


def main():
    pygame.display.init()
    pygame.font.init()
    window = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
    pygame.display.set_caption("Week 12 - Two punch styles")
    screen = pygame.Surface((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    world = World()  # Keep practising on Week 11's lower deck.

    running = True
    while running:
        dt = min(clock.tick(LOOP_FPS) / 1000, 0.05)
        events = pygame.event.get()  # Collect once; forward player events below.
        player_events = []
        reset_requested = False
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
            player_events = []  # Old punches/jumps must not affect the fresh player.

        keys = pygame.key.get_pressed()
        world.update(dt, keys, player_events)
        world.draw(screen)
        pygame.transform.scale(screen, window.get_size(), window)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
