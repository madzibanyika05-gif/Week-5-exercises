class Student:
    student_count = 0  # Class attribute to keep track of the number of students

    def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        Student.student_count += 1  # Increment the count of students each time a Student is created

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_student_number(self):
        return self.student_number

    @classmethod
    def get_student_count(cls):
        return cls.student_count

# Create student objects
s1 = Student("John", "Smith", "1871")
s2 = Student("Sara", "Penrose", "1893")

# Test the class functions on s1
print(f"s1 First Name: {s1.get_first_name()}")        # Output: John
print(f"s1 Last Name: {s1.get_last_name()}")          # Output: Smith
print(f"s1 Full Name: {s1.get_full_name()}")          # Output: John Smith
print(f"s1 Student Number: {s1.get_student_number()}") # Output: 1871

# Test the class functions on s2
print(f"s2 First Name: {s2.get_first_name()}")        # Output: Sara
print(f"s2 Last Name: {s2.get_last_name()}")          # Output: Penrose
print(f"s2 Full Name: {s2.get_full_name()}")          # Output: Sara Penrose
print(f"s2 Student Number: {s2.get_student_number()}") # Output: 1893

# Display the total student count
print(f"Total number of students: {Student.get_student_count()}") # Output: 2

