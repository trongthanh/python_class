# Classroom assets — original Luffy sheet and flat ship deck

`luffy.png` is an unchanged copy of the prepared reference game's Luffy sheet:
`part_2/one_piece_game/game/assets/luffy.png`, originally supplied as
`part_2/one_piece_game/assets/Monkey D Luffy.png`. It is also identical to
`part_2/week_09/teacher/assets/luffy.png`, used by the animation viewer.

It contains artwork from the Game Boy Advance **One Piece** game. The original
ripper/curator credit for this particular supplied Luffy sheet has not been
verified; do not attribute it to the rippers of other character sheets.
No ownership or redistribution permission is claimed by this course.

The whole original sheet is retained; Week 10 maps four idle, six walk and
twelve jump poses. `frames.py` supplies the same irregular rectangles and foot
pivots as the viewer, plus idle/walk animation FPS. Jump poses are selected by
vertical speed. Students remove the opaque teal background at drawing time
with `set_colorkey()`; the source PNG is unchanged.

`background.png` is a teacher-prepared 240 × 160 crop of
`part_2/one_piece_game/game/assets/ship_3.png` (source strip 2 of the original
`Alvidas Ship.png`, credited to **Cabamanman**). Source crop rectangle:
`(200, 111, 240, 160)`. The flat deck's y = 237 becomes y = 126 in the snapshot.
Transparent sky was composited over simple Pygame-drawn sky colors/clouds.
The crop is fixed artwork, not a parsed map; no stairs or gaps occur within it.

**Not CC0.** Keep local/classroom-only, subject to applicable permissions. Do not
publish source or derivative artwork in a public homework ZIP without rights
clearance, or replace it with distributable artwork first. No audio or enemy art
is included in this week's pack. The brown training ledge is drawn with Pygame
rectangles in main.py, not additional external artwork.
