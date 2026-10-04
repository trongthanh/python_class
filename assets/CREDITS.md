# Classroom assets — Luffy and flat ship deck

`luffy.png` is an unchanged copy of the prepared reference game's Luffy sheet:
`part_2/one_piece_game/game/assets/luffy.png`, originally supplied as
`part_2/one_piece_game/assets/Monkey D Luffy.png`.

It contains artwork from the Game Boy Advance **One Piece** game. The original
ripper/curator credit for this particular supplied Luffy sheet has not been
verified; do not attribute it to the rippers of the other character sheets.
No ownership or redistribution permission is claimed by this course.

The whole sheet is retained; Week 9 maps only the four idle and six walk poses.
The Python frame rectangles and foot pivots match the reference game's data.
The teacher-supplied helper removes the teal background at runtime.

`background.png` is a teacher-prepared 240 × 160 crop of
`part_2/one_piece_game/game/assets/ship_3.png` (source strip 2 of the original
`Alvidas Ship.png`, credited to **Cabamanman**). Source crop rectangle:
`(200, 111, 240, 160)`. The flat deck's y = 237 becomes y = 126 in the snapshot.
Transparent sky was composited over simple Pygame-drawn sky colors/clouds.
The crop is fixed artwork, not a parsed map; no stairs or gaps occur within it.

**Not CC0.** Keep local/classroom-only, subject to applicable permissions. Do not
publish the source or derivative artwork in a public homework ZIP without rights
clearance, or replace it with distributable artwork first. No audio or enemy art is
included in this week's pack.
