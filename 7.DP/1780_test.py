# factorial 함수 구현


def factorial_recursive(n):
  if n > 0:
    return n * factorial_recursive(n - 1)
  return 1

print(factorial_recursive(5))