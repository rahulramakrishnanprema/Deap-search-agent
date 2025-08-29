// MCP Generated: 2025-08-29 09:19:27 - Generate Python code for a calculator.  The user selects (+, -, *, /).  The program takes two numeri

/**
 * Generates Python code for a simple calculator.
 * The calculator performs addition, subtraction, multiplication, and division on two numerical inputs.
 * Error handling is included for division by zero.
 */
function generatePythonCalculatorCode(): string {
  return `
import sys

def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers and returns the difference."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers and returns the product."""
  return x * y

def divide(x, y):
  """Divides two numbers and returns the quotient.
  Handles division by zero error.
  """
  if y == 0:
    return "Division by zero error!"
  else:
    return x / y

def main():
  """Main function to handle user input and perform calculations."""
  if len(sys.argv) != 3:
    print("Usage: python calculator.py <operator> <number1> <number2>")
    return

  operator = sys.argv[1]
  try:
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
  except ValueError:
    print("Invalid input. Please enter numbers.")
    return

  if operator == '+':
    result = add(num1, num2)
  elif operator == '-':
    result = subtract(num1, num2)
  elif operator == '*':
    result = multiply(num1, num2)
  elif operator == '/':
    result = divide(num1, num2)
  else:
    print("Invalid operator. Please use +, -, *, or /.")
    return

  print(f"Result: {result}")

if __name__ == "__main__":
  main()
`;
}


/**
 * Main function to write the generated Python code to a file.
 */
function main() {
  const pythonCode = generatePythonCalculatorCode();
  const fs = require('fs'); // Import Node.js fs module

  try {
    fs.writeFileSync('calculator.py', pythonCode);
    console.log('Python calculator code generated successfully in calculator.py');
  } catch (err) {
    console.error('Error writing to file:', err);
  }
}


// Run the main function
main();

```

This TypeScript program generates a complete, functional Python calculator program that handles division by zero and invalid input.  The generated Python code is written to a file named `calculator.py`. Remember to have Node.js installed to run this TypeScript code.  You can then run the generated `calculator.py` from your terminal using `python calculator.py <operator> <number1> <number2>`.  For example: `python calculator.py + 5 3`