def binary_to_decimal(binary_array):
    decimal_value = 0
    power = len(binary_array) - 1

    for digit in binary_array:
        decimal_value += digit * (2 ** power)
        power -= 1

    return decimal_value

def main():
    while True:
        try:
            user_input = input("Enter a valid binary number (e.g., 1011): ")

            # Validation
            if not all(char in '01' for char in user_input):
                raise ValueError("Invalid input")

            # Convertion
            binary_array = [int(char) for char in user_input]
            break
        except ValueError as e:
            print(e)

    decimal_result = binary_to_decimal(binary_array)
    print(f"The decimal representation of {user_input} is: {decimal_result}")

# Run the main function
if __name__ == "__main__":
    main()