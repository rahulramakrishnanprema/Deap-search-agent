def multiply(numbers):
  p=1
  for n in numbers:
    try:
      p*=float(n)
    except:
      return "Error: Non-numeric input"
  return p