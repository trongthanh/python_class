"""Week 10 sprite configuration: original idle/walk/jump rectangles and pivots.

Rect = source x, y, width, height. Pivot = local foot x, y inside that crop.
fps = animation pictures per second, not game-loop redraws per second.
Idle/walk use configured FPS. Jump poses follow vertical speed, not a loop FPS.
The teacher viewer uses the same sheet and crop/pivot values.
"""

LUFFY = {
    "image": "luffy.png",
    "background": [99, 206, 181],
    "source_facing": 1,
    "fps": {"idle": 6, "walk": 9},
    "actions": {
        "idle": [
            {"rect": [11, 8, 35, 52], "pivot": [17, 45]},
            {"rect": [60, 8, 36, 52], "pivot": [18, 45]},
            {"rect": [106, 8, 37, 52], "pivot": [18, 45]},
            {"rect": [155, 8, 38, 52], "pivot": [19, 45]},
        ],
        "jump": [
            {"rect": [16, 141, 36, 63], "pivot": [18, 54]},
            {"rect": [64, 141, 35, 63], "pivot": [17, 54]},
            {"rect": [107, 141, 39, 63], "pivot": [19, 54]},
            {"rect": [152, 141, 39, 63], "pivot": [19, 54]},
            {"rect": [199, 141, 37, 63], "pivot": [18, 54]},
            {"rect": [243, 141, 36, 63], "pivot": [18, 54]},
            {"rect": [289, 141, 37, 63], "pivot": [18, 54]},
            {"rect": [337, 141, 37, 63], "pivot": [18, 54]},
            {"rect": [382, 141, 37, 63], "pivot": [18, 54]},
            {"rect": [430, 141, 36, 63], "pivot": [18, 54]},
            {"rect": [473, 141, 36, 63], "pivot": [18, 54]},
            {"rect": [514, 141, 39, 63], "pivot": [19, 54]},
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
