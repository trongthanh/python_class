# Classroom assets — original Luffy sheet, the lower-deck scene and sky

`luffy.png` is an unchanged copy of the prepared reference game's Luffy sheet:
`part_2/one_piece_game/game/assets/luffy.png`, originally supplied as
`part_2/one_piece_game/assets/Monkey D Luffy.png`. It is identical to the
Week 9 viewer and Week 10 copies. Week 11 still maps four idle, six walk and
twelve jump poses; `frames.py` is unchanged.

It contains artwork from the Game Boy Advance **One Piece** game. The original
ripper/curator credit for this particular supplied Luffy sheet has not been
verified; do not attribute it to the rippers of other character sheets.
No ownership or redistribution permission is claimed by this course.

`ship_2.png` is a cropped copy of `part_2/one_piece_game/game/assets/ship_2.png`
(as committed), the full game's second playable scene: **source strip 3** of the
original `Alvidas Ship.png`, credited to **Cabamanman**. The 1269 × 320 original
was cropped to **1266 × 303** (3 see-through columns off the right, 17 nearly
empty rows off the bottom), its see-through column 0 filled from column 1 so
floor x-coordinates are unchanged, and its 139 half-transparent pixels made
solid. The sky stays transparent; picture colors are
not collision data. The floor, ledge and exit numbers in `world.py` were traced
from the red and green marks in
`part_2/one_piece_game/game/assets/ship_2_guide.png`, a teacher reference that
is not shipped or drawn here.

`sky.png` is an unchanged copy of `part_2/one_piece_game/game/assets/sky.png`
(576 × 192), shrunk by the teacher-only `prepare_assets.py` from
`part_2/one_piece_game/assets/sky_background.png`. Its original source/credit
is not recorded in this course; treat it with the same restrictions.

Week 10's flat-deck `background.png` is no longer used and is not included.

**Not CC0.** Keep local/classroom-only, subject to applicable permissions. Do not
publish source or derivative artwork in a public homework ZIP without rights
clearance, or replace it with distributable artwork first. No audio or enemy art
is included in this week's pack. The gold exit frame is drawn with Pygame.
