def add(numbers):
  try:
    return sum(numbers)
  except TypeError:
    return "Error: Non-numeric input"
