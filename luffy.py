"""Week 11 — your finished Week 10 Luffy, plus one supplied rule for ship steps.

Nothing here knows about the camera. Luffy still lives in WORLD pixels and
draws on the world surface he was given. This week's TODOs are in world.py.
"""
import pygame

from frames import LUFFY
from spritesheet import SpriteSheet


class Luffy:
    SPEED = 105  # Keep your Week 9 movement tuning.
    GRAVITY = 850  # Pixels per second added to vertical speed each second.
    JUMP = -350  # Negative goes up. About a 70-pixel jump with this gravity.
    MAX_FALL_SPEED = 650
    STEP_HEIGHT = 12  # New: walk up small steps; taller ones need a jump.

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
        previous = self.rect.copy()  # New: where the body was before moving.
        self.rect.x += direction * self.SPEED * dt
        bounds = self.surface.get_rect()  # Now the whole ship, not the window.
        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right
        self.climb_or_block(previous, direction)  # New this week, supplied.

        # New physics goes before picture selection. Keep the previous FEET height.
        previous_bottom = self.rect.bottom
        self.apply_gravity(dt)
        self.land(previous_bottom)
        self.choose_animation(direction, keys)
        self.update_animation(dt)

    def climb_or_block(self, previous, direction):
        # Supplied Week 11 rule. The ship floor has steps of different heights.
        # Small step: walk up it. Taller step: it acts as a wall, so jump.
        for platform in self.platforms:
            rise = previous.bottom - platform.top  # How far above the feet?
            if rise <= 0:
                continue  # Not above the feet: gravity and land() handle it.
            walked_in_from_left = (direction > 0 and previous.right <= platform.left
                                   and self.rect.right > platform.left)
            walked_in_from_right = (direction < 0 and previous.left >= platform.right
                                    and self.rect.left < platform.right)
            if not walked_in_from_left and not walked_in_from_right:
                continue
            if self.on_ground and rise <= self.STEP_HEIGHT:
                self.rect.bottom = platform.top  # Step up.
            elif walked_in_from_left:
                self.rect.right = platform.left  # Bump: stop at the wall.
            else:
                self.rect.left = platform.right

    def apply_gravity(self, dt):
        # STEP 1 — acceleration changes speed; speed changes position.
        self.vy += self.GRAVITY * dt
        self.vy = min(self.vy, self.MAX_FALL_SPEED)
        self.rect.y += self.vy * dt

    def land(self, previous_bottom):
        # STEP 2 — only feet crossing a top while falling can land.
        self.on_ground = False
        if self.vy >= 0:
            for platform in self.platforms + self.floating_platforms:
                overlaps_x = self.rect.right > platform.left and self.rect.left < platform.right
                crosses_top = previous_bottom <= platform.top and self.rect.bottom >= platform.top
                if overlaps_x and crosses_top:
                    self.rect.bottom = platform.top
                    self.vy = 0.0
                    self.on_ground = True

    def jump(self):
        # STEP 3 — one jump, only from a surface.
        if self.on_ground:
            self.vy = self.JUMP
            self.on_ground = False

    def choose_animation(self, direction, keys):
        # STEP 4 — being airborne wins over a held movement key.
        if not self.on_ground:
            self.set_animation("jump")
            return
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
        # Unchanged Week 9 pivot-aware drawing, at WORLD positions on the world
        # surface. No camera maths here: the World's camera picks the view.
        frame = self.animations[self.animation][self.frame_index]
        image = frame["image"]
        foot_x, foot_y = frame["pivot"]
        if self.facing != self.sheet.source_facing:
            image = pygame.transform.flip(image, True, False)
            foot_x = image.get_width() - 1 - foot_x
        self.surface.blit(image, (self.rect.centerx - foot_x,
                                  self.rect.bottom - foot_y))
