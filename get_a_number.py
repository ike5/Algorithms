import random


def main():
    # Define the range and size of the list
    range_start = 1  # Starting number in range
    range_end = 1000000  # Ending number in range
    list_size = 100000  # Desired size of the list

    # Generate a list of unique random numbers
    random_list = random.sample(range(range_start, range_end + 1), list_size)

    # Print the first 10 numbers to verify (optional)
    print(random_list[:1000])


if __name__ == '__main__':
    main()
