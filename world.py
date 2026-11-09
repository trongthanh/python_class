"""Week 11 STARTER — run main.py; fill the numbered STEP TODOs in this file.

Like Week 7's Box Pusher, the World paints everything on its OWN canvas, then
copies it to the screen. New this week: the canvas is the whole ship (1266 × 303
WORLD pixels) and the screen is only 240 × 160. The camera is a screen-sized
Rect that chooses which part of the world we copy.

    world x/y  = where something is on the ship (never changes when we scroll)
    screen x/y = where it appears in the window = world x/y - camera x/y
"""
from pathlib import Path

import pygame

from luffy import Luffy

ASSETS = Path(__file__).resolve().parent / "assets"

WIDTH = 240  # The SCREEN, in Game Boy Advance pixels.
HEIGHT = 160

# The lower deck of Alvida's ship (scene 2 of the full game). Teacher-supplied
# data, traced from the red lines in ship_2_guide.png. All numbers are WORLD pixels.
SHIP_PICTURE = "ship_2.png"  # Cropped: no see-through strips at its edges.
SKY_PICTURE = "sky.png"  # 576 × 192, far behind the ship; seen through its sky holes.
SPAWN = (45, 250)  # (center_x, feet_y)
EXIT_GATE = (1244, 120, 23, 62)  # (left, top, width, height)
# Ground segments as (left, top, width). Together they cover every world x.
FLOOR = [
    (0, 250, 240), (240, 254, 8), (248, 261, 8), (256, 267, 16),
    (272, 270, 227), (499, 265, 8), (507, 260, 8), (515, 255, 13),
    (528, 253, 209), (737, 250, 12), (749, 245, 12), (761, 239, 57),
    (818, 243, 8), (826, 248, 8), (834, 253, 13), (847, 253, 91),
    (938, 283, 111), (1049, 173, 220),
]
# One-way ledges (left, top, width): pillar tops and a plank over the pit.
LEDGES = [(242, 189, 62), (354, 155, 62), (466, 123, 62), (817, 173, 97),
          (988, 189, 62)]


class World:
    def __init__(self):
        # convert_alpha(): the ship picture has see-through holes where the sky is.
        self.background = pygame.image.load(str(ASSETS / SHIP_PICTURE)).convert_alpha()
        # STEP 5 — TODO: load SKY_PICTURE into self.sky, like the ship picture
        # above. Use .convert(): the sky has no see-through parts.
        # The world surface is as big as the whole ship picture. Every thing
        # draws here at its world position, like actors on a film set.
        # SRCALPHA keeps the sky holes see-through on the world surface too.
        self.surface = pygame.Surface(self.background.get_size(), pygame.SRCALPHA)
        self.platforms = []
        self.floating_platforms = []
        self.build_platforms()
        self.debug = False  # F1: collision boxes and coordinates.
        self.show_map = False  # F2: the whole world, shrunk, with the camera.
        self.font = pygame.font.Font(None, 12)
        self.big_font = pygame.font.Font(None, 28)
        self.reset()

    def build_platforms(self):
        # Supplied: Week 10's floor and ledge Rects, now made from the numbers.
        # A ground Rect reaches down to the bottom of the world.
        world_bottom = self.surface.get_height()
        for left, top, width in FLOOR:
            self.platforms.append(pygame.Rect(left, top, width, world_bottom - top))
        # Each ledge is a thin one-way top, like Week 10's brown ledge.
        for left, top, width in LEDGES:
            self.floating_platforms.append(pygame.Rect(left, top, width, 6))

    def reset(self):
        # R builds a fresh Luffy and camera; the ship itself does not change.
        x, feet = SPAWN
        self.player = Luffy(self.surface, x, feet, platforms=self.platforms,
                            floating_platforms=self.floating_platforms)
        # STEP 1 — TODO: replace None with the camera: a screen-sized Rect in
        # WORLD pixels, at the part of the world the offset shows: (0, feet - 120).
        self.camera = None  # No camera yet.
        self.done = False
        self.follow_player()

    def update(self, dt, keys=None, events=()):
        if self.done:
            return  # Scene clear: freeze until R.
        self.player.update(dt, keys, events)  # Only the player gets the events.
        self.follow_player()
        self.check_exit()

    def follow_player(self):
        # STEP 2 — TODO: set self.camera.centerx to Luffy's rect.centerx.
        # STEP 4 — TODO: set self.camera.top so Luffy's feet (rect.bottom)
        # sit 120 pixels down the screen. Write it ABOVE the Step 3 line.
        # STEP 3 — TODO: keep the camera inside the ship with clamp_ip(),
        # clamped to self.surface.get_rect(). Clamp is always LAST.
        pass

    def check_exit(self):
        # STEP 6 — TODO: make gate = pygame.Rect(EXIT_GATE). If Luffy's rect
        # collides with it, set self.done = True. Both are in WORLD pixels.
        pass

    # --- Drawing: the world on its own surface, then one camera copy ---

    def draw(self, screen):
        self.draw_sky(screen)  # Behind everything, straight on the screen.
        # Paint the world on its own surface, at WORLD positions.
        self.surface.fill((0, 0, 0, 0))  # Wipe last frame: fully see-through.
        self.surface.blit(self.background, (0, 0))
        # STEP 6 — TODO: call self.draw_exit() here, before Luffy draws.
        self.player.draw()  # Luffy draws himself on the world, as in Week 10.
        if self.debug:
            self.draw_debug()  # Supplied: collision boxes, on the world.
        # Show the WHOLE world on the screen, moved up so Luffy's spawn is in
        # view: his feet (world y SPAWN[1]) land at screen y 120.
        offset_x = 0
        offset_y = 120 - SPAWN[1]
        screen.blit(self.surface, (offset_x, offset_y))
        # STEP 1 — TODO: replace the three offset lines above with ONE camera
        # copy: blit self.surface at (0, 0), with self.camera as the area.
        # Supplied: screen things stay put while the ship scrolls behind them.
        if self.show_map:
            self.draw_map(screen)
        if self.debug:
            self.draw_coordinates(screen)
        self.draw_hud(screen)
        if self.done:
            self.draw_banner(screen)

    def draw_sky(self, screen):
        # The ship's see-through holes show this plain sky-blue fill (it also
        # wipes last frame off the screen).
        # STEP 5 — TODO: replace the fill with the sky picture: sky_x = 0,
        # sky_y = 0, then blit self.sky at (sky_x, sky_y). Run it.
        # Then parallax, like Week 2's starfield: far things move slower.
        # The camera moves 5 pixels, the sky slides 1 (minus: opposite way):
        # sky_x = -self.camera.x // 5 and sky_y = -self.camera.y // 5.
        screen.fill("skyblue")

    def draw_exit(self):
        # STEP 6 — TODO: make gate = pygame.Rect(EXIT_GATE). Draw it as a gold
        # frame on the WORLD surface: pygame.draw.rect(self.surface, "gold", gate, 2).
        # Bonus: render "EXIT" with self.font and blit it on self.surface
        # at (gate.centerx - 9, gate.top - 10).
        pass

    # --- Supplied teacher tools: read later ---

    def draw_debug(self):
        # Drawn on the WORLD surface, so the boxes scroll with the ship.
        for platform in self.platforms + self.floating_platforms:
            pygame.draw.rect(self.surface, "lime", platform, 1)
        pygame.draw.rect(self.surface, "cyan", self.player.rect, 1)
        pygame.draw.circle(self.surface, "yellow", self.player.rect.midbottom, 2)

    def draw_coordinates(self, screen):
        # F1, fixed to the screen. Screen position = world position - camera.
        world_x = int(self.player.rect.centerx)
        world_y = int(self.player.rect.bottom)
        lines = ["Luffy world: (" + str(world_x) + ", " + str(world_y) + ")"]
        if self.camera is not None:
            screen_x = world_x - self.camera.x
            screen_y = world_y - self.camera.y
            lines.append("Luffy screen: (" + str(screen_x) + ", " + str(screen_y) + ")")
            lines.append("camera: (" + str(self.camera.x) + ", " + str(self.camera.y) + ")")
        top = 4
        if self.show_map:
            top = 58  # Below the shrunken map.
        for number, line in enumerate(lines):
            screen.blit(self.font.render(line, True, "white"), (4, top + number * 10))

    def draw_map(self, screen):
        # The whole world shrunk to the screen's width; yellow = the camera.
        scale = WIDTH / self.surface.get_width()
        size = (WIDTH, round(self.surface.get_height() * scale))
        pygame.draw.rect(screen, "midnightblue", ((0, 0), size))  # Behind the sky holes.
        screen.blit(pygame.transform.scale(self.surface, size), (0, 0))
        if self.camera is not None:
            view = pygame.Rect(self.camera.x * scale, self.camera.y * scale,
                               self.camera.width * scale, self.camera.height * scale)
            pygame.draw.rect(screen, "yellow", view, 1)

    def draw_hud(self, screen):
        strip = pygame.Surface((WIDTH, 12), pygame.SRCALPHA)
        strip.fill((0, 0, 0, 170))
        screen.blit(strip, (0, HEIGHT - 12))
        hint = "A/D: move  SPACE: jump  F1: boxes  F2: map  R: reset"
        screen.blit(self.font.render(hint, True, "white"), (4, HEIGHT - 10))

    def draw_banner(self, screen):
        shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        shade.fill((0, 0, 0, 150))
        screen.blit(shade, (0, 0))
        title = self.big_font.render("SCENE CLEAR!", True, "gold")
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10)))
        hint = self.font.render("Next week: more of Alvida's ship. R: again", True, "white")
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 12)))
