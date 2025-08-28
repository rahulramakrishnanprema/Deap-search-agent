# Auto-generated python solution for CUP-7
    # Generated: 2025-08-28 20:03:12
    # Requirement: Implement input validation for a calculator.  Reject non-numeric input, display an error message, and re-prompt the user until valid numeric input is received.  Return the validated numeric value.

    def get_validated_number(prompt: str) -> float:
    """
    Prompts the user for a numeric input and validates it.

    Args:
        prompt: The prompt message to display to the user.

    Returns:
        The validated numeric input as a float.

    Raises:
        ValueError: If the input cannot be converted to a float after multiple attempts.

    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # End of generated code for CUP-7
    