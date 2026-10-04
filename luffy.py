"""Week 9 STARTER — change this file during class, then run main.py.

Make Luffy animate, turn and walk across a flat ship deck.
The background, image helper and game loop are supplied. Follow the TODOs.
"""
import pygame

from frames import LUFFY  # Luffy's OWN frame lists.
from spritesheet import SpriteSheet


class Luffy:
    SPEED = 105  # Game pixels per second.
    IDLE_FPS = 6  # Pictures per second, NOT game-loop frames per second.
    WALK_FPS = 9

    def __init__(self, surface, center_x, feet_y):
        self.surface = surface  # WHERE Luffy draws himself: given by main.py.
        self.sheet = SpriteSheet(LUFFY)  # WHAT he looks like: his own pictures.
        self.rect = pygame.FRect(0, 0, 23, 39)
        self.rect.midbottom = (center_x, feet_y)
        self.facing = 1  # 1 = right, -1 = left
        self.animation = "idle"
        self.animation_time = 0.0  # Seconds since this animation started.

    def set_animation(self, name):
        # STEP 1 — TODO: only when name is DIFFERENT from self.animation:
        # remember the new name and reset self.animation_time to 0.0.
        pass

    def update_animation(self, dt):
        # STEP 2 — TODO: add dt to self.animation_time.
        # dt is the time since the previous game-loop frame, in seconds.
        pass

    def read_direction(self, keys):
        # Supplied: holding both directions cancels them out.
        direction = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction += 1
        # STEP 4 — TODO: if direction is not zero, remember it in self.facing.
        # Releasing the keys should NOT make Luffy forget his last direction.
        return direction

    def choose_animation(self, direction):
        # STEP 3 — TODO: choose "walk" if direction is not zero;
        # otherwise choose "idle". Use self.set_animation(...).
        pass

    def move_horizontal(self, direction, width, dt):
        # STEP 5 — TODO: add direction * self.SPEED * dt to self.rect.x.
        # If the left edge goes below 0, set it to 0.
        # If the right edge passes width, set it to width.
        pass

    def draw(self):
        # Supplied: turn the clock into a picture number, then ask the sheet
        # to draw that picture with its feet on the bottom-middle of self.rect.
        speed = self.WALK_FPS
        if self.animation == "idle":
            speed = self.IDLE_FPS
        frame = int(self.animation_time * speed)  # The sheet wraps: 0, 1, 2, 3, 0, ...
        self.sheet.draw(self.surface, self.animation, frame, self.facing,
                        self.rect.centerx, self.rect.bottom)
