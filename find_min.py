# O(1) - constant
import random


def find_min(x, y):
    if x < y:
        return x
    else:
        return y


if __name__ == '__main__':
    x = random.random()
    y = random.random()

    print(f"x = {x}")
    print(f"y = {y}")
    smallest_number = find_min(x, y)
    print(f"The min is: {smallest_number}")
