# exercise 7
class NatSet:
    def __init__(self):
        self.numbers_set = set()

    def add(self, number):
        if isinstance(number, int) and number >= 0:  # Check for natural number
            self.numbers_set.add(number)
        else:
            raise ValueError("Only natural numbers (0 and positive integers) can be added.")

    def remove(self, number):
        if number in self.numbers_set:
            self.numbers_set.remove(number)
        else:
            raise ValueError("Number not found in the set.")

    def has_number(self, number):
        return number in self.numbers_set

    def numbers(self):
        return list(self.numbers_set)

# Example usage:
nat_set = NatSet()

# Adding natural numbers
nat_set.add(5)
nat_set.add(3)
nat_set.add(10)

print("Numbers in set:", nat_set.numbers())  # Output: [3, 5, 10]

# Checking if a number is in the set
print("Has 5?", nat_set.has_number(5))  # Output: True
print("Has 7?", nat_set.has_number(7))  # Output: False

# Removing a number
nat_set.remove(3)
print("Numbers in set after removal:", nat_set.numbers())  # Output: [5, 10]

# Attempting to add a non-natural number
try:
    nat_set.add(-1)
except ValueError as e:
    print(e)  # Output: Only natural numbers (0 and positive integers) can be added.

# Attempting to remove a number not in the set
try:
    nat_set.remove(7)
except ValueError as e:
    print(e)  # Output: Number not found in the set.
