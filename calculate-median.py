import random

def asc_sort(numbers):
    n = len(numbers)
    for i in range(0, n - 1):  # Outer loop
        last = n - i - 1
        greatest: dict[str, int] = { 'value': numbers[0], 'index': 0 }
        for j in range(0, last + 1):  # Inner loop

            if greatest['value'] < numbers[j]:
                greatest['value'] = numbers[j]
                greatest['index'] = j

        # swap numbers
        temp_value = numbers[last]
        numbers[last] = greatest['value']
        numbers[greatest['index']] = temp_value

    return numbers

def calculate_median(numbers):
    sorted_numbers = asc_sort(numbers)

    print(f"sorted_numbers: {sorted_numbers}")
    n = len(sorted_numbers)

    if n % 2 == 1:  # Odd number of elements
        median = sorted_numbers[n // 2]
    else:  # Even number of elements
        mid1 = sorted_numbers[(n // 2) - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2

    return median

def main():
    # Generate a random list of 20 numbers between 0 and 12
    random_numbers = [random.randint(0, 12) for _ in range(20)]
    #random_numbers = [5, 12, 8, 3, 6, 5, 1, 2, 8, 6, 2, 9, 7, 3, 4, 4, 7, 12, 2, 2]
    print(f"Random list of numbers: {random_numbers}")

    median = calculate_median(random_numbers)
    print(f"Median: {median}")

if __name__ == "__main__":
    main()