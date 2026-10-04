"""Supplied image helpers: load a picture once, then draw one sprite-sheet frame.

Each character makes its OWN SpriteSheet from its own frame dictionary:

    from frames import LUFFY
    self.sheet = SpriteSheet(LUFFY)

The frame dictionary, image cache and pivot maths are implementation details,
not lesson TODOs. Characters only call sheet.draw(...) and sheet.frame_count(...).
"""
from pathlib import Path

import pygame

ASSETS = Path(__file__).resolve().parent / "assets"

# File name -> loaded Surface. Ten pirates share ONE copy of pirate.png.
LOADED_IMAGES = {}


def load_image(name, transparent=False):
    """Load assets/<name> once; later calls reuse the same Surface.

    Call this after pygame.display.set_mode(): converting needs a window.
    """
    key = (name, transparent)
    if key not in LOADED_IMAGES:
        image = pygame.image.load(str(ASSETS / name))
        if transparent:
            image = image.convert_alpha()
        else:
            image = image.convert()  # Opaque backgrounds blit faster.
        LOADED_IMAGES[key] = image
    return LOADED_IMAGES[key]


class SpriteSheet:
    """One character's whole source sheet plus its frame dictionary.

    data looks like frames.LUFFY:
    {"image": "luffy.png", "background": [r, g, b], "source_facing": 1,
     "actions": {"walk": [{"rect": [x, y, w, h], "pivot": [x, y]}, ...]}}
    """

    def __init__(self, data):
        self.image = load_image(data["image"], transparent=True)
        self.actions = data["actions"]
        self.background = None
        if data.get("background") is not None:
            self.background = tuple(data["background"])
        self.source_facing = data.get("source_facing", 1)
        if self.source_facing not in (-1, 1):
            raise ValueError("source_facing must be -1 (left) or +1 (right)")
        self.cache = {}  # Reuse cropped/flipped images instead of rebuilding every frame.
        for frames in self.actions.values():
            for frame in frames:
                rect = pygame.Rect(frame["rect"])
                if rect.width <= 0 or rect.height <= 0 or not self.image.get_rect().contains(rect):
                    raise ValueError(f"Frame outside spritesheet {data['image']}: {rect}")

    def frame_count(self, action):
        return len(self.actions[action])

    def frame(self, action, index, facing=1):
        """Return (image, (foot_x, foot_y)) for one frame. Indexes wrap around."""
        frames = self.actions[action]
        number = index % len(frames)  # Wrap: 0, 1, 2, 3, 0, 1, ...
        key = (action, number, facing)
        if key not in self.cache:
            entry = frames[number]
            image = self.image.subsurface(pygame.Rect(entry["rect"]))
            if self.background is not None:
                # Each sheet keeps its original opaque background color.
                # Only the selected frame applies it as a color key.
                image = image.copy()
                image.set_colorkey(self.background)
            foot_x, foot_y = entry["pivot"]
            if facing != self.source_facing:
                image = pygame.transform.flip(image, True, False)
                foot_x = image.get_width() - 1 - foot_x
            self.cache[key] = (image, (foot_x, foot_y))
        return self.cache[key]

    def draw(self, surface, action, index, facing, x, feet_y):
        """Blit one frame so its foot pivot lands on (x, feet_y)."""
        image, (foot_x, foot_y) = self.frame(action, index, facing)
        surface.blit(image, (x - foot_x, feet_y - foot_y))
