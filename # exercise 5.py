# exercise 5
class Tally:
    def __init__(self):
        self.count = 0

    def incBy(self, value=1):
        self.count += value

    def decBy(self, value=1):
        self.count -= value

    def value(self):
        return self.count

# Create two Tally objects
t1 = Tally()
t2 = Tally()

# Increment t1 three times by 1
t1.incBy()
t1.incBy()
t1.incBy()

# Decrement t1 once by 1
t1.decBy()

# Increment t2 four times by 1
t2.incBy()
t2.incBy()
t2.incBy()
t2.incBy()

# Print the results
print("Value of t1:", t1.value())  # Output will be 2 (3 increments - 1 decrement)
print("Value of t2:", t2.value())  # Output will be 4
