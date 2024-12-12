import math


def distance(x1, y1, xp, yp):
    return math.sqrt((xp - x1) ** 2 + (yp - y1) ** 2)


def move_forward(steps_x, steps_y, iterations):
    x, y = 0, 0  # start at origin
    for i in range(iterations):
        x += steps_x
        y += steps_y
        print(f"Iteration {i + 1}: Current position: ({x}, {y})")


if __name__ == "__main__":
    move_forward(1, 2, 4)
