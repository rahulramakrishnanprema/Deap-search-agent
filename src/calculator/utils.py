def multiply(numbers: list) -> float:
    """Computes the product of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The product of the numbers in the list.

    Raises:
        TypeError: If the input list contains non-numeric values.
    """
    product = 1
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("Input list must contain only numbers.")
        product *= number
    return product
