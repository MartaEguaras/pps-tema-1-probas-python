def fibonacci(n):
  """Calcula la serie de Fibonacci hasta 'n' elementos."""
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]

  fib = [0, 1]
  while len(fib) < n:
    siguiente = fib[-1] + fib[-2]
    fib.append(siguiente)
  return fib