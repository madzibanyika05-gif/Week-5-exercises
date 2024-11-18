# exercise 9
class NatSet:
    def __init__(self, initial_numbers=None):
        self.numbers_set = set()
        if initial_numbers is None:
            initial_numbers = []
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

    def card(self):
        """Returns the number of elements in the set."""
        return len(self.numbers_set)

    def elem(self, n):
        """Checks whether n is included in the set."""
        return n in self.numbers_set

    def sum(self):
        """Returns the sum of all numbers in the set."""
        return sum(self.numbers_set)

    def product(self):
        """Returns the product of all numbers in the set."""
        if not self.numbers_set:
            return 1  # Return 1 for the product of an empty set
        result = 1
        for number in self.numbers_set:
            result *= number
        return result

    def is_empty(self):
        """Checks if the set is empty."""
        return len(self.numbers_set) == 0

    def union(self, other):
        """Performs the union of this set with another NatSet."""
        if not isinstance(other, NatSet):
            raise TypeError("The argument must be an instance of NatSet.")
        self.numbers_set = self.numbers_set.union(other.numbers_set)

# Example usage:
nat_set1 = NatSet(initial_numbers=[1, 2, 3])
nat_set2 = NatSet(initial_numbers=[3, 4, 5])

print("Numbers in set 1:", nat_set1.numbers())  # Output: [1, 2, 3]
print("Numbers in set 2:", nat_set2.numbers())  # Output: [3, 4, 5]

# Using the new methods
print("Cardinality of set 1:", nat_set1.card())  # Output: 3
print("Element 2 in set 1?", nat_set1.elem(2))   # Output: True
print("Sum of set 1:", nat_set1.sum())           # Output: 6
print("Product of set 1:", nat_set1.product())   # Output: 6
print("Is set 1 empty?", nat_set1.is_empty())    # Output: False

# Performing union
nat_set1.union(nat_set2)
print("Numbers in set 1 after union:", nat_set1.numbers())  # Output: [1, 2, 3, 4, 5]

# Checking if set is empty
print("Is set 2 empty?", nat_set2.is_empty())  # Output: False
