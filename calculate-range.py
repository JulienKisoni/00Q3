import random

def get_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def get_min(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

def calculate_range(numbers):
    smallest = get_min(numbers)
    largest = get_max(numbers)
    range_value = largest - smallest
    return smallest, largest, range_value

def main():
    # Generate a random list of 20 numbers between 0 and 12
    random_numbers = [random.randint(0, 12) for _ in range(20)]
    print(f"Random list of numbers: {random_numbers}")

    smallest, largest, range_value = calculate_range(random_numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
    print(f"Range: {range_value}")

if __name__ == "__main__":
    main()