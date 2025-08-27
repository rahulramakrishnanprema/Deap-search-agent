def subtract(a, b):
    """Subtracts b from a.

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        The difference between a and b.

    Raises:
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b

# Assume calculator menu structure is already implemented
def calculator_menu():
    while True:
        # ... existing menu code ...
        if choice == 'subtract':
            try:
                a = float(input("Enter minuend: "))
                b = float(input("Enter subtrahend: "))
                result = subtract(a, b)
                print(f"Result: {result}")
            except TypeError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        # ... rest of the menu ...

# Example usage (if running this file directly):
#calculator_menu()