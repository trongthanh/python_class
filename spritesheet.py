"""Supplied helper, unchanged since Week 10 — your Week 9 crop/list methods.

frames.py supplies crop rectangles, foot pivots and the background color.
No cache, loader wrapper or validation framework.
"""
from pathlib import Path

import pygame

ASSETS = Path(__file__).resolve().parent / "assets"


class SpriteSheet:
    def __init__(self, data):
        # Supplied: the source is a solid bitmap, with no alpha transparency.
        self.image = pygame.image.load(str(ASSETS / data["image"])).convert()
        self.actions = data["actions"]
        self.background = data["background"]
        self.source_facing = data["source_facing"]

    def get_frame(self, entry):
        # Last week: crop pixels, then hide the solid background color.
        rect = pygame.Rect(entry["rect"])
        image = self.image.subsurface(rect).copy()
        image.set_colorkey(self.background)
        return image

    def load_animation(self, name):
        # Last week: build an ordered picture list, keeping each foot pivot.
        frames = []
        for entry in self.actions[name]:
            image = self.get_frame(entry)
            frames.append({"image": image, "pivot": entry["pivot"]})
        return frames
