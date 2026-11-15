# Week 12 asset credits and restrictions

These One Piece game rips are not CC0 Kenney art. No ownership or redistribution
permission is claimed by this course. Keep this slice for classroom/local use;
do not publish source/derivative art in a public ZIP without rights clearance
or replacing it with distributable artwork.

- `luffy.png`: unchanged original irregular Luffy sheet from Week 11
  (1090 × 678), prepared from the teacher reference's nine-row
  `Monkey D Luffy.png`. Source game: **One Piece (Game Boy Advance)**,
  developed by Dimps and published by Bandai. Existing source/ripper credits
  remain on the original sheet; no new author credit is claimed here.
- `ship_2.png`: byte-identical to Week 11's cropped lower deck. Its original
  1269 × 320 crop was trimmed to 1266 × 303 (3 transparent right columns,
  17 nearly empty bottom rows); column 0 was filled from column 1 to preserve
  floor x-coordinates, and 139 half-transparent pixels were made solid.
  Sky holes remain transparent.
- `sky.png`: unchanged Week 11/reference sky (576 × 192); background art
  cropped from `Assets and Fonts.png` in the same local One Piece asset pack.
- `frames.py`: supplied Python configuration preserves the reference game's
  original irregular crop Rects and foot pivots. The punch, windup and finish
  rows are newly used here; the underlying sheet is unchanged.
- `pirate.png`: unchanged original Pirate sheet from the teacher reference,
  prepared from `Enemies - Pirate.png` in the same One Piece GBA pack. Source
  credits remain on the sheet. `PIRATE` uses its first idle crop at
  `(20, 37, 45, 44)` with foot pivot `(21, 43)` and orange color key
  `(255, 128, 0)`. Week 12 draws this one static picture; it does not animate.
  The same copyrighted-art restrictions apply. No audio is included.

Collision platforms were traced from the reference `ship_*_guide.png` red
lines. Those teacher guides and the large original source pack are not shipped.
The lower-deck gate is moved two pixels left to fit Week 11's cropped picture.
This snapshot uses only the lower deck; other ship art is not included.
