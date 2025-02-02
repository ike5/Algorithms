import math


# starting origin (0, 0)
# P = (4, 5)
# steps_x = 2, steps_y = 3
# backward_x = 1, backward_y = 1


# define distance formula
def distance(x1, y1, xp, yp):
    return math.sqrt((xp - x1) ** 2 + (yp - y1) ** 2)


# define update position
def update_position(origin, P, steps_x, steps_y, backward_x, backward_y, iterations):
    # calculate initial distance between origin and P. Set the max to this.
    x1, y1 = origin
    xp, yp = P
    d = distance(x1, y1, xp, yp)

    print(d)

    for i in range(iterations):
        x1 += steps_x
        y1 += steps_y
        if (i + 1) % 3 == 0:
            x1 -= backward_x
            y1 -= backward_y
        d = distance(x1, y1, xp, yp)
        print(f"Iteration {i + 1}, x1,y1 is ({x1}, {y1}), distance: {round(d,6)}")


if __name__ == "__main__":
    origin = (0, 0)
    P = (4, 5)
    steps_x, steps_y = 2, 3
    backward_x, backward_y = 1, 1
    iterations = 2

    update_position(origin, P, steps_x, steps_y, backward_x, backward_y, iterations)
