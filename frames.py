"""Supplied frame lists, sliced from one_piece_game/game/frames.py.

Only rows 1 (idle) and 2 (walk) are mapped this week. Rectangles are irregular:
do not divide the sheet into equal cells. Each pivot is a local foot anchor.
The whole original Luffy sheet is preserved, ready for later lessons.
"""

LUFFY = {
    "image": "luffy.png",
    "background": [99, 206, 181],
    "source_facing": 1,
    "actions": {
        "idle": [
            {"rect": [11, 8, 35, 52], "pivot": [17, 45]},
            {"rect": [60, 8, 36, 52], "pivot": [18, 45]},
            {"rect": [106, 8, 37, 52], "pivot": [18, 45]},
            {"rect": [155, 8, 38, 52], "pivot": [19, 45]},
        ],
        "walk": [
            {"rect": [16, 75, 43, 55], "pivot": [21, 47]},
            {"rect": [68, 75, 33, 55], "pivot": [16, 47]},
            {"rect": [109, 75, 39, 55], "pivot": [19, 47]},
            {"rect": [156, 75, 38, 55], "pivot": [19, 47]},
            {"rect": [205, 75, 31, 55], "pivot": [15, 47]},
            {"rect": [246, 75, 38, 55], "pivot": [19, 47]},
        ],
    },
}
