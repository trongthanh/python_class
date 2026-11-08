"""Week 10 STARTER — run main.py; fill four physics TODOs in this file.

Starts with your working Week 9 walking scene. No gravity or jump yet.
Keep spritesheet.py and frames.py as supplied catch-up code.
"""
import pygame

from frames import LUFFY
from spritesheet import SpriteSheet


class Luffy:
    SPEED = 105  # Keep your Week 9 movement tuning.
    GRAVITY = 850  # Pixels per second added to vertical speed each second.
    JUMP = -350  # Negative goes up. About a 70-pixel jump with this gravity.
    MAX_FALL_SPEED = 650

    def __init__(self, surface, center_x, feet_y, platforms=(), floating_platforms=()):
        self.surface = surface
        self.platforms = list(platforms)
        self.floating_platforms = list(floating_platforms)
        self.sheet = SpriteSheet(LUFFY)
        self.animations = {
            "idle": self.sheet.load_animation("idle"),
            "walk": self.sheet.load_animation("walk"),
            "jump": self.sheet.load_animation("jump"),
        }
        self.rect = pygame.FRect(0, 0, 23, 39)
        self.rect.midbottom = (center_x, feet_y)
        self.vy = 0.0
        self.on_ground = True  # Main starts him standing on the flat floor.
        self.space_down = False  # Supplied: held Space must not auto-repeat jumps.
        self.facing = 1
        self.animation = "idle"
        self.animation_time = 0.0
        self.frame_index = 0

    def set_animation(self, name):
        # Your Week 9 reset rule stays unchanged.
        if self.animation != name:
            self.animation = name
            self.animation_time = 0.0
            self.frame_index = 0

    def update(self, dt, keys=None, events=()):
        # Main collects the event queue ONCE and passes this actor's events.
        for event in events:
            self._handle_event(event)

        # Existing Week 9 direction/facing and horizontal movement.
        direction = 0
        if keys is not None:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                direction -= 1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                direction += 1
            if direction != 0:
                self.facing = direction
        self.rect.x += direction * self.SPEED * dt
        bounds = self.surface.get_rect()
        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right

        # New physics goes before picture selection. Keep the previous FEET height.
        previous_bottom = self.rect.bottom
        self.apply_gravity(dt)
        self.land(previous_bottom)
        self.choose_animation(direction, keys)
        self.update_animation(dt)

    def apply_gravity(self, dt):
        # STEP 1 — TODO: add self.GRAVITY * dt to self.vy.
        # Limit self.vy to MAX_FALL_SPEED, then move self.rect.y by self.vy * dt.
        pass

    def land(self, previous_bottom):
        # STEP 2 — TODO: start with self.on_ground = False.
        # If falling, loop over self.platforms + self.floating_platforms.
        # Check horizontal overlap AND feet crossing the top from above.
        # On landing: set rect.bottom, vy = 0.0, on_ground = True.
        # Do not break: a higher crossed surface must beat the floor.
        pass

    def jump(self):
        # STEP 3 — TODO: only if self.on_ground, set self.vy = self.JUMP
        # and self.on_ground = False. Midair presses must not queue a jump.
        pass

    def choose_animation(self, direction, keys):
        # STEP 4 — TODO: if not self.on_ground, select "jump" and return.
        # Jump takes priority over idle/walk, even when no movement key is held.
        # Supplied Week 9 behavior: optional input, remembered facing.
        if keys is not None:
            if direction != 0:
                self.set_animation("walk")
            else:
                self.set_animation("idle")
        elif self.animation == "jump":
            self.set_animation("idle")  # No keyboard: return to idle after landing.

    def _handle_event(self, event):
        # Supplied input plumbing. Students write jump(), not an event framework.
        if event.type == pygame.WINDOWFOCUSLOST:
            self.space_down = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.space_down = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not self.space_down:
                self.space_down = True
                self.jump()

    def update_animation(self, dt):
        # Keep your Week 9 clock/list indexing; jump gets a supplied physics sampler.
        self.animation_time += dt
        frames = self.animations[self.animation]
        if self.animation == "jump":
            count = len(frames)
            progress = (self.vy - self.JUMP) / (abs(self.JUMP) * 2)
            self.frame_index = max(0, min(count - 1, int(progress * count)))
        else:
            speed = LUFFY["fps"][self.animation]
            self.frame_index = int(self.animation_time * speed) % len(frames)

    def draw(self):
        # Unchanged Week 9 pivot-aware drawing. No camera or physics here.
        frame = self.animations[self.animation][self.frame_index]
        image = frame["image"]
        foot_x, foot_y = frame["pivot"]
        if self.facing != self.sheet.source_facing:
            image = pygame.transform.flip(image, True, False)
            foot_x = image.get_width() - 1 - foot_x
        self.surface.blit(image, (self.rect.centerx - foot_x,
                                  self.rect.bottom - foot_y))
