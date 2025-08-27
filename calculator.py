def subtract(a, b):
  try:
    return float(a) - float(b)
  except ValueError:
    return "Invalid input"

# ... existing calculator code ...
print(subtract(10,5))
print(subtract('a',5))