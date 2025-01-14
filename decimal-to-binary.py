def decimal_to_binary(n, binary_array=None):
    if binary_array is None:
        binary_array = []

    # when n is 0, end.
    if n == 0:
        return binary_array

    remainder = n % 2
    result = n // 2

    # Append the remainder when dividing by 2
    binary_array.insert(0, remainder)

    # Recursive call
    return decimal_to_binary(result, binary_array)

def main():
    while True:
            # Ask the user for a valid four-digit number
            user_input = int(input("Enter a valid four-digit number (1000-9999): "))
            if 1000 <= user_input <= 9999:
                break
            else:
                print("Invalid input.")

    binary_array_result = decimal_to_binary(user_input)
    binary_string = ''.join(map(str, binary_array_result))
    print(f"The binary representation of {user_input} is: {binary_string}")

# Run the main function
if __name__ == "__main__":
    main()