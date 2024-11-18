# exercise 12

def to_binary(n):
    if n == 0:
        return ""  # Base case: the binary representation of 0 is an empty string
    elif n == 1:
        return "1"  # Base case: the binary representation of 1 is "1"
    else:
        return to_binary(n // 2) + str(n % 2)  # Recursive case

# Example usage:
print(to_binary(2))  # Output: "10"
print(to_binary(5))  # Output: "101"
print(to_binary(10))  # Output: "1010"
print(to_binary(0))  # Output: ""
