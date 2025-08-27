def subtract(a, b):
    """Subtracts b from a.

    Args:
        a: The minuend.
        b: The subtrahend.

    Raises:
        TypeError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b

# Example integration into a calculator menu (assuming menu structure exists)
def calculator_menu():
    # ... existing menu code ...
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
        # ... existing menu code ...

# Example usage (uncomment to test):
#calculator_menu()