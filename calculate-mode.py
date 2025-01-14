import random

def get_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def calculate_mode(numbers):
    frequency: dict[str, int] = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    max_frequency = get_max(list(frequency.values()))
    mode = []
    for key, value in frequency.items():
        if value == max_frequency:
            mode.append(key)

    return mode, max_frequency

def main():
    # Generate a random list of 20 numbers between 0 and 12
    random_numbers = [random.randint(0, 12) for _ in range(20)]
    print(f"Random list of numbers: {random_numbers}")

    mode, frequency = calculate_mode(random_numbers)
    print(f"Mode(s): {mode} with a frequency of {frequency}")

if __name__ == "__main__":
    main()