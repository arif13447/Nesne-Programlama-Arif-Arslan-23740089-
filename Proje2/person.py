class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"Student - Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"Teacher - Name: {self.name}, Age: {self.age}, Subject: {self.subject}"
    
if __name__ == "__main__":
    student = Student("Ahmet", 20, "235846")
    teacher = Teacher("Mr. Ömer", 40, "Matematik")

    print(student.display_info())
    print(teacher.display_info())
    
if __name__ == "__main__":
    student = Student("Ali", 20, "245682")
    teacher = Teacher("Mr. Ömer", 40, "Matematik")

    print(student.display_info())
    print(teacher.display_info())
    
if __name__ == "__main__":
    student = Student("Ayşe", 20, "235158")
    teacher = Teacher("Mr. Ömer", 40, "Matematik")

    print(student.display_info())
    print(teacher.display_info())