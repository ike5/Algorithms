import random


def generate_random_list(range_start=1, range_end=10000, list_size=1000):
    """
    Generate a list of unique random numbers.
    """
    random_list = random.sample(range(range_start, range_end + 1), list_size)
    return random_list


def main():
    random_list = generate_random_list()
    print(random_list[:1000])


if __name__ == '__main__':
    main()
