"""Week 12 practice enemy: one static pirate picture and a body hitbox.

No AI, HP, movement, contact damage or blocking yet. Week 13 extends this class.
"""
import pygame

from frames import PIRATE
from spritesheet import SpriteSheet


class Enemy:
    def __init__(self, surface, center_x, feet_y):
        self.surface = surface
        self.frame = SpriteSheet(PIRATE).load_animation("idle")[0]
        self.rect = pygame.Rect(0, 0, 23, 39)
        self.rect.midbottom = (center_x, feet_y)
        self.hits = 0
        self.flash_time = 0.0
        self.font = pygame.font.Font(None, 12)

    def take_hit(self):
        self.hits += 1
        self.flash_time = 0.18

    def update(self, dt, keys=None):
        # Same dt-first shape as Luffy, but this static enemy ignores input.
        self.flash_time = max(0.0, self.flash_time - dt)

    def draw(self):
        image = self.frame["image"]
        foot_x, foot_y = self.frame["pivot"]
        self.surface.blit(image, (self.rect.centerx - foot_x,
                                  self.rect.bottom - foot_y))
        if self.flash_time > 0:
            pygame.draw.rect(self.surface, "gold", self.rect, 2)
        label = self.font.render(str(self.hits), True, "white")
        label_box = label.get_rect(midbottom=(self.rect.centerx, self.rect.top - 3))
        pygame.draw.rect(self.surface, "black", label_box.inflate(4, 2))
        self.surface.blit(label, label_box)
