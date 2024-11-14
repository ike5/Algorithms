# O(c^N) - Exponential


def fibonacci(n):
    print(n)
    if (1 == n) | (2 == n):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(3))
