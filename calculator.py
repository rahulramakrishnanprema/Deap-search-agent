def add(numbers: list):
    """Calculates the sum of a list of numbers.

    Args:
        numbers: A list of numbers to sum.

    Returns:
        The sum of the numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: if the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError(f"Invalid input: {number} is not a number.")
        total += number
    return total


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


if __name__ == "__main__":
    while True:
        print("\nSelect operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == '5':
            break

        try:
            if choice == '1':
                num_list = []
                while True:
                    num_str = input("Enter a number (or type 'done'): ")
                    if num_str.lower() == 'done':
                        break
                    try:
                        num = float(num_str)
                        num_list.append(num)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                print(f"Sum: {add(num_list)}")
            elif choice == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Difference: {subtract(num1, num2)}")
            elif choice == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Product: {multiply(num1, num2)}")
            elif choice == '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Quotient: {divide(num1, num2)}")
            else:
                print("Invalid input")
        except (TypeError, ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
