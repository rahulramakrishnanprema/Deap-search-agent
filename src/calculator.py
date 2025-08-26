def add(numbers: list) -> float:
    """Calculates the sum of a list of numbers.

    Args:
        numbers: A list of numbers to sum.

    Returns:
        The sum of the numbers in the list.

    Raises:
        TypeError: If any element in the list is not a number.
    """
    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements in the list must be numbers.")
        total += number
    return total

# Example usage (assuming this is integrated into a larger calculator program):
# numbers = [1, 2, 3, 4, 5]
# try:
#     result = add(numbers)
#     print(f"The sum is: {result}")
# except TypeError as e:
#     print(f"Error: {e}")
