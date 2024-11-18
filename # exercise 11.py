# exercise 11

def product_up_to(n):
    if n <= 1:
        return 1  # Base case: the product of numbers up to 1 is 1
    else:
        return n * product_up_to(n - 1)  # Recursive case: n * product of numbers up to n-1

# Example usage:
n = 5
result = product_up_to(n)
print(f"Product of natural numbers from 1 to {n} is: {result}")  # Output: 120
