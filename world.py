"""Week 12 — practice punches on Week 11's lower deck; no scene transitions."""
from pathlib import Path

import pygame

from enemy import Enemy
from luffy import Luffy

ASSETS = Path(__file__).resolve().parent / "assets"
WIDTH = 240
HEIGHT = 160

# Supplied Week 11 terrain and three static pirate practice positions.
# Multi-scene data and transitions are deferred to a later lesson.
SCENE = {'title': 'LOWER DECK',
  'picture': 'ship_2.png',
  'spawn': (45, 250),
  'floor': [(0, 250, 240),
            (240, 254, 8),
            (248, 261, 8),
            (256, 267, 16),
            (272, 270, 227),
            (499, 265, 8),
            (507, 260, 8),
            (515, 255, 13),
            (528, 253, 209),
            (737, 250, 12),
            (749, 245, 12),
            (761, 239, 57),
            (818, 243, 8),
            (826, 248, 8),
            (834, 253, 13),
            (847, 253, 91),
            (938, 283, 111),
            (1049, 173, 220)],
  'ledges': [(242, 189, 62), (354, 155, 62), (466, 123, 62), (817, 173, 97), (988, 189, 62)],
  'exit': (1242, 120, 23, 62),
  'enemies': [(85, 250), (140, 250), (600, 253)]}


class World:
    def __init__(self):
        self.scene = SCENE
        self.background = pygame.image.load(str(ASSETS / self.scene["picture"])).convert_alpha()
        self.sky = pygame.image.load(str(ASSETS / "sky.png")).convert()
        self.surface = pygame.Surface(self.background.get_size(), pygame.SRCALPHA)
        self.platforms = []
        self.floating_platforms = []
        bottom = self.surface.get_height()
        for left, top, width in self.scene["floor"]:
            self.platforms.append(pygame.Rect(left, top, width, bottom - top))
        for left, top, width in self.scene["ledges"]:
            self.floating_platforms.append(pygame.Rect(left, top, width, 6))
        self.debug = False
        self.show_map = False
        self.font = pygame.font.Font(None, 12)
        self.big_font = pygame.font.Font(None, 24)
        self.reset()

    def reset(self):
        x, feet = self.scene["spawn"]
        self.player = Luffy(self.surface, x, feet, platforms=self.platforms,
                            floating_platforms=self.floating_platforms)
        self.targets = []
        for x, feet in self.scene["enemies"]:
            self.targets.append(Enemy(self.surface, x, feet))
        self.camera = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.done = False
        self.follow_player()

    def update(self, dt, keys=None, events=()):
        if self.done:
            return
        for target in self.targets:
            target.update(dt)
        self.player.update(dt, keys, events)
        self.hit_targets()
        self.follow_player()
        gate = pygame.Rect(self.scene["exit"])
        if self.player.rect.colliderect(gate):
            self.done = True

    def hit_targets(self):
        # STEP 4 — TODO: test world Rect overlap; remember each target hit this action.
        pass

    def follow_player(self):
        self.camera.centerx = self.player.rect.centerx
        self.camera.top = self.player.rect.bottom - 120
        self.camera.clamp_ip(self.surface.get_rect())

    def draw(self, screen):
        self.draw_sky(screen)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.background, (0, 0))
        self.draw_exit()
        for target in self.targets:
            target.draw()
        self.player.draw()
        if self.debug:
            self.draw_debug()
        screen.blit(self.surface, (0, 0), self.camera)
        if self.show_map:
            self.draw_map(screen)
        self.draw_hud(screen)
        if self.done:
            self.draw_banner(screen)

    def draw_sky(self, screen):
        screen.fill("skyblue")
        sky_x = -self.camera.x // 5
        sky_y = -self.camera.y // 5
        screen.blit(self.sky, (sky_x, sky_y))

    def draw_exit(self):
        gate = pygame.Rect(self.scene["exit"])
        pygame.draw.rect(self.surface, "gold", gate, 2)
        label = self.font.render("EXIT", True, "gold")
        self.surface.blit(label, (gate.left, gate.top - 10))

    def draw_debug(self):
        for platform in self.platforms + self.floating_platforms:
            pygame.draw.rect(self.surface, "lime", platform, 1)
        pygame.draw.rect(self.surface, "cyan", self.player.rect, 1)
        for target in self.targets:
            pygame.draw.rect(self.surface, "white", target.rect, 1)
        box = self.player.attack_rect()
        if box is not None:
            pygame.draw.rect(self.surface, "red", box, 1)

    def draw_map(self, screen):
        scale = WIDTH / self.surface.get_width()
        size = (WIDTH, round(self.surface.get_height() * scale))
        pygame.draw.rect(screen, "midnightblue", ((0, 0), size))
        screen.blit(pygame.transform.scale(self.surface, size), (0, 0))
        view = pygame.Rect(self.camera.x * scale, self.camera.y * scale,
                           self.camera.width * scale, self.camera.height * scale)
        pygame.draw.rect(screen, "yellow", view, 1)

    def draw_hud(self, screen):
        strip = pygame.Surface((WIDTH, 23), pygame.SRCALPHA)
        strip.fill((0, 0, 0, 190))
        screen.blit(strip, (0, HEIGHT - 23))
        lines = ["A/D: walk  SPACE: jump  J: punch  K: hold",
                 "R: reset practice  F1/F2: debug"]
        for number, line in enumerate(lines):
            screen.blit(self.font.render(line, True, "white"), (3, HEIGHT - 21 + number * 10))
        title = self.font.render(self.scene["title"], True, "white")
        screen.blit(title, (4, 3))

    def draw_banner(self, screen):
        shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        shade.fill((0, 0, 0, 150))
        screen.blit(shade, (0, 0))
        label = self.big_font.render("SCENE CLEAR!", True, "gold")
        screen.blit(label, label.get_rect(center=(WIDTH // 2, 68)))
        label = self.font.render("R: return to punch practice", True, "white")
        screen.blit(label, label.get_rect(center=(WIDTH // 2, 91)))
