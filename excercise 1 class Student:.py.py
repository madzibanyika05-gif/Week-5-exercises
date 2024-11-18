class Student:
    def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_student_number(self):
        return self.student_number

# Example usage
student = Student("Mathew", "Madzibanyika", "1192518")
print(student.get_first_name())       # Output: Mathew
print(student.get_last_name())        # Output: Madzibanyika
print(student.get_full_name())        # Output: Mathew Madzibanyika
print(student.get_student_number())    # Output: 1192518
