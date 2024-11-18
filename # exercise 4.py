class Tally:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def value(self):
        return self.count
# Create two Tally objects
t1 = Tally()
t2 = Tally()

# Increment t1 three times
t1.increment()
t1.increment()
t1.increment()

# Decrement t1 once
t1.decrement()

# Increment t2 four times
t2.increment()
t2.increment()
t2.increment()
t2.increment()

# Print the results
print("Value of t1:", t1.value())  # Output will be 2 (3 increments - 1 decrement)
print("Value of t2:", t2.value())  # Output will be 4
