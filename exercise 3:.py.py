class Tally:
    def __init__(self):
        self.count = 0  # Initialize the count to 0

    def inc(self):
        """Increment the count by 1."""
        self.count += 1

    def dec(self):
        """Decrement the count by 1, ensuring it does not go negative."""
        if self.count > 0:
            self.count -= 1
        else:
            print("Count cannot be negative.")

    def tally(self):
        """Return the current value of the count."""
        return self.count

# Example usage
tally = Tally()

# Incrementing the count
tally.inc()
tally.inc()
print("Current count after incrementing:", tally.tally())  # Output: 2

# Decrementing the count
tally.dec()
print("Current count after decrementing:", tally.tally())  # Output: 1

# Decrementing above zero
tally.dec()
tally.dec()  # This should show a message that the count cannot be negative
print("Current count after exceeding decrement:", tally.tally())  # Output: 0
