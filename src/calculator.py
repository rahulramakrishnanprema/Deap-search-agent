def multiply(numbers):
  p=1
  for n in numbers:
    if not isinstance(n,(int,float)): raise TypeError
    p*=n
  return p