# exercise 8

class NatSet:
    def __init__(self, initial_numbers=None):
        self.numbers_set = set()
        # If no initial_numbers is provided, set it to an empty list
        if initial_numbers is None:
            initial_numbers = []
        # Add each number in the initial collection to the set
        for number in initial_numbers:
            self.add(number)

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
# Creating an instance with an initial collection of numbers
nat_set_with_initial = NatSet(initial_numbers=[5, 3, 10])
print("Numbers in set with initial collection:", nat_set_with_initial.numbers())  # Output: [3, 5, 10]

# Creating an instance without providing any initial numbers
nat_set_empty = NatSet()
print("Numbers in set without initial collection:", nat_set_empty.numbers())  # Output: []

# Adding more natural numbers
nat_set_empty.add(7)
print("Numbers in set after addition:", nat_set_empty.numbers())  # Output: [7]

# Checking if a number is in the set
print("Has 5?", nat_set_with_initial.has_number(5))  # Output: True

# Removing a number
nat_set_with_initial.remove(3)
print("Numbers in set after removal:", nat_set_with_initial.numbers())  # Output: [5, 10]

# Attempting to add a non-natural number
try:
    nat_set_with_initial.add(-1)
except ValueError as e:
    print(e)  # Output: Only natural numbers (0 and positive integers) can be added.
