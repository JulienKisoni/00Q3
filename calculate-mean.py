import random

def get_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_mean(numbers):
    total = get_sum(numbers)
    number_of_elements = len(numbers)
    result = total / number_of_elements
    return result

def main():
    random_numbers = [random.randint(0, 12) for _ in range(20)]
    print(f"Random list of numbers: {random_numbers}")

    mean = calculate_mean(random_numbers)
    print(f"Mean: {mean:.2f}")  # Format to 2 decimal places

if __name__ == "__main__":
    main()