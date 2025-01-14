import random
import math

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

def calculate_variance(numbers, mean):
    squared_differences_sum = 0
    number_of_elements = len(numbers)
    for number in numbers:
        squared_differences_sum += (number - mean) ** 2  # Sum of (x - mean)^2
    return squared_differences_sum / number_of_elements  # Average of squared differences

def calculate_standard_deviation(variance):
    return math.sqrt(variance)  # Square root of the variance

def main():
    # Generate a random list of 20 numbers between 0 and 12
    random_numbers = [random.randint(0, 12) for _ in range(20)]
    print(f"Random list of numbers: {random_numbers}")

    mean = calculate_mean(random_numbers)

    variance = calculate_variance(random_numbers, mean)
    print(f"Variance: {variance:.2f}")

    standard_deviation = calculate_standard_deviation(variance)
    print(f"Standard Deviation: {standard_deviation:.2f}")

if __name__ == "__main__":
    main()