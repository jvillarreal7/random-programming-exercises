from typing import List

# Canvas dimension constants
CANVAS_WIDTH = 8
CANVAS_HEIGHT = 8

# Initial positions
INITIAL_X = 4
INITIAL_Y = 4

# Color to be set
COLOR_TO_BE_SET = 3


def flood_fill(
    canvas: List[List], x: int, y: int, current_color: int, new_color: int
) -> None:
    """
    Flood fill recursive algorithm.
    """
    # Base cases:
    # 1) If x or y is outside the screen, then return
    if x < 0 or x >= CANVAS_WIDTH or y < 0 or y >= CANVAS_HEIGHT:
        return

    # 2) If color of canvas[x][y] is not the same as the current color, then return
    if canvas[x][y] != current_color:
        return

    # Replace color of canvas cell at (x, y)
    canvas[x][y] = new_color

    # Recursively call for north, east, south and west
    flood_fill(canvas, x + 1, y, current_color, new_color)
    flood_fill(canvas, x - 1, y, current_color, new_color)
    flood_fill(canvas, x, y + 1, current_color, new_color)
    flood_fill(canvas, x, y - 1, current_color, new_color)


def find_color(canvas: List[List], x: int, y: int, new_color: int) -> None:
    """
    Finds previous color on (x, y) and calls flood_fill().
    """
    current_color = canvas[x][y]
    flood_fill(canvas, x, y, current_color, new_color)


canvas = [
    [3, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

print("Initial canvas: ", *canvas, sep="\n")

find_color(canvas, INITIAL_X, INITIAL_Y, COLOR_TO_BE_SET)

print("Updated canvas: ", *canvas, sep="\n")
