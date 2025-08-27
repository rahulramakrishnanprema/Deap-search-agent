def add(numbers: list):
    """Calculates the sum of a list of numbers.

    Args:
        numbers: A list of numbers to sum.

    Returns:
        The sum of the numbers in the list.

    Raises:
        TypeError: If the input list contains non-numeric values.
    """
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Input list must contain only numbers.")
    return sum(numbers)

# Example integration within a calculator program
if __name__ == "__main__":
    try:
        numbers = [1, 2, 3, 4, 5]
        result = add(numbers)
        print(f"The sum is: {result}")

        invalid_numbers = [1, 2, 'a', 4, 5]
        result = add(invalid_numbers)
        print(f"The sum is: {result}") #This line should not be reached
    except TypeError as e:
        print(f"Error: {e}")
