
def fibonacci(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

fibonacci_2000 = fibonacci(2000)
print(fibonacci_2000)
