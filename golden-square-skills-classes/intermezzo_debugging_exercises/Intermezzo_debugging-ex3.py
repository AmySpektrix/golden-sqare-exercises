def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

