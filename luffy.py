"""Week 12 — the Week 11 walker gains short and rubber punches.

Positions and hitboxes stay in WORLD pixels; draw() still knows no camera.
The original crop/pivot data and single-pass attack picture sampler are supplied.
"""
import pygame

from frames import LUFFY
from spritesheet import SpriteSheet


class Luffy:
    SPEED = 105
    GRAVITY = 850
    JUMP = -350
    MAX_FALL_SPEED = 650
    STEP_HEIGHT = 12
    SHORT_TIME = 0.30
    WINDUP_TIME = 12 / LUFFY["fps"]["stretch_start"]
    LAUNCH_TIME = 0.25  # Supplied: five launch poses before the long fist.
    STRETCH_TIME = LAUNCH_TIME + 6 / LUFFY["fps"]["stretch_finish"]

    def __init__(self, surface, center_x, feet_y, platforms=(), floating_platforms=()):
        self.surface = surface
        self.platforms = list(platforms)
        self.floating_platforms = list(floating_platforms)
        self.sheet = SpriteSheet(LUFFY)
        self.animations = {}
        for name in LUFFY["actions"]:
            self.animations[name] = self.sheet.load_animation(name)
        self.rect = pygame.FRect(0, 0, 23, 39)
        self.rect.midbottom = (center_x, feet_y)
        self.vy = 0.0
        self.on_ground = True
        self.space_down = False
        # STEP 1 — TODO: add j_down and k_down, both initially False.
        self.facing = 1
        self.animation = "idle"
        self.animation_time = 0.0
        self.frame_index = 0
        self.action = ""  # "", "punch", "windup", or "stretch".
        self.action_time = 0.0
        self.hit_targets = []  # Objects already hit during THIS action.

    def set_animation(self, name):
        if self.animation != name:
            self.animation = name
            self.animation_time = 0.0
            self.frame_index = 0

    def update(self, dt, keys=None, events=()):
        for event in events:
            self._handle_event(event)
        self.update_attack(dt)

        direction = 0
        # Supplied bridge: attacks lock horizontal movement AND facing.
        # Gravity/landing still run, so an action cannot suspend Luffy in the air.
        if keys is not None and self.action == "":
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                direction -= 1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                direction += 1
            if direction != 0:
                self.facing = direction
        previous = self.rect.copy()
        self.rect.x += direction * self.SPEED * dt
        bounds = self.surface.get_rect()
        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
        if self.rect.right > bounds.right:
            self.rect.right = bounds.right
        self.climb_or_block(previous, direction)
        previous_bottom = self.rect.bottom
        self.apply_gravity(dt)
        self.land(previous_bottom)
        self.choose_animation(direction, keys)
        self.update_animation(dt)

    def start_attack(self, name):
        # STEP 1 — TODO: ignore busy/airborne starts; set action, reset clock and hit list.
        pass

    def update_attack(self, dt):
        # STEP 2 — TODO: advance the action clock and finish the short punch.
        pass

    def cancel_windup(self):
        # STEP 5 — TODO: cancel only the windup when K is released early.
        pass

    def attack_rect(self):
        # STEP 3 — TODO: make a front-facing world Rect only in the active window.
        return None

    def climb_or_block(self, previous, direction):
        # Unchanged Week 11 terrain rule.
        for platform in self.platforms:
            rise = previous.bottom - platform.top
            if rise <= 0:
                continue
            walked_in_from_left = (direction > 0 and previous.right <= platform.left
                                   and self.rect.right > platform.left)
            walked_in_from_right = (direction < 0 and previous.left >= platform.right
                                    and self.rect.left < platform.right)
            if not walked_in_from_left and not walked_in_from_right:
                continue
            if self.on_ground and rise <= self.STEP_HEIGHT:
                self.rect.bottom = platform.top
            elif walked_in_from_left:
                self.rect.right = platform.left
            else:
                self.rect.left = platform.right

    def apply_gravity(self, dt):
        self.vy += self.GRAVITY * dt
        self.vy = min(self.vy, self.MAX_FALL_SPEED)
        self.rect.y += self.vy * dt

    def land(self, previous_bottom):
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
        if self.on_ground and self.action == "":
            self.vy = self.JUMP
            self.on_ground = False

    def choose_animation(self, direction, keys):
        # Supplied: action poses take priority over the existing physics poses.
        if self.action == "punch":
            self.set_animation("punch")
        elif self.action == "windup":
            self.set_animation("stretch_start")
        elif self.action == "stretch":
            if self.action_time < self.LAUNCH_TIME:
                self.set_animation("stretch_start")
            else:
                self.set_animation("stretch_finish")
        elif not self.on_ground:
            self.set_animation("jump")
        elif keys is not None:
            if direction != 0:
                self.set_animation("walk")
            else:
                self.set_animation("idle")
        elif self.animation not in ("idle", "walk"):
            self.set_animation("idle")

    def _handle_event(self, event):
        # Supplied Week 10 Space handling and OS-repeat guard.
        if event.type == pygame.WINDOWFOCUSLOST:
            self.space_down = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.space_down = False
            # STEP 1 — TODO: release J; Step 5 will also release/cancel K.
        elif event.type == pygame.KEYDOWN and not getattr(event, "repeat", False):
            # STEP 1 — TODO: a fresh J press starts "punch".
            # STEP 5 — TODO: a fresh K press starts "windup".
            if event.key == pygame.K_SPACE and not self.space_down:
                self.space_down = True
                self.jump()

    def update_animation(self, dt):
        # Supplied art sampler: attack pictures play ONCE, never modulo-loop.
        self.animation_time += dt
        frames = self.animations[self.animation]
        if self.action == "punch":
            self.frame_index = min(4, int(self.action_time / self.SHORT_TIME * 5))
        elif self.action == "windup":
            self.frame_index = min(11, int(self.action_time * LUFFY["fps"]["stretch_start"]))
        elif self.action == "stretch":
            if self.action_time < self.LAUNCH_TIME:
                self.frame_index = min(16, 12 + int(self.action_time / self.LAUNCH_TIME * 5))
            else:
                finish_time = self.action_time - self.LAUNCH_TIME
                self.frame_index = min(5, int(finish_time * LUFFY["fps"]["stretch_finish"]))
        elif self.animation == "jump":
            progress = (self.vy - self.JUMP) / (abs(self.JUMP) * 2)
            self.frame_index = max(0, min(len(frames) - 1, int(progress * len(frames))))
        else:
            speed = LUFFY["fps"][self.animation]
            self.frame_index = int(self.animation_time * speed) % len(frames)

    def draw(self):
        # Unchanged Week 9 foot-pivot drawing. No camera arithmetic.
        frame = self.animations[self.animation][self.frame_index]
        image = frame["image"]
        foot_x, foot_y = frame["pivot"]
        if self.facing != self.sheet.source_facing:
            image = pygame.transform.flip(image, True, False)
            foot_x = image.get_width() - 1 - foot_x
        self.surface.blit(image, (self.rect.centerx - foot_x,
                                  self.rect.bottom - foot_y))
