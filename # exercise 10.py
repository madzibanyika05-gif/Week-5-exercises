# exercise 10

def sum_up_to_rec(n):
    if n <= 0:
        return 0  # Base case: if n is 0 or negative, return 0
    else:
        return n + sum_up_to_rec(n - 1)  # Recursive case: n + sum of numbers up to n-1

# Example usage:
n = 5
result = sum_up_to_rec(n)
print(f"Sum of natural numbers from 1 to {n} is: {result}")  # Output: 15
