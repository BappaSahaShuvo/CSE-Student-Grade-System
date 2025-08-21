class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.courses = {}  # store subject: grade

    def add_course(self, subject, grade):
        """Add course and grade for the student"""
        self.courses[subject] = grade

    def calculate_gpa(self):
        """Calculate average GPA"""
        if not self.courses:
            return 0.0
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return round(gpa, 2)

    def performance(self):
        """Classify performance"""
        gpa = self.calculate_gpa()
        if gpa >= 3.5:
            return "🌟 Excellent"
        elif 3.0 <= gpa < 3.5:
            return "👍 Good"
        elif 2.0 <= gpa < 3.0:
            return "🙂 Average"
        else:
            return "⚠️ Poor"

    def display_info(self):
        """Show student details"""
        print(f"\n👤 Name: {self.name}")
        print(f"🆔 Roll: {self.roll}")
        print("📚 Courses & Grades:")
        for subject, grade in self.courses.items():
            print(f"   - {subject}: {grade}")
        print(f"📊 GPA: {self.calculate_gpa()}")
        print(f"💡 Performance: {self.performance()}")


class GradeSystem:
    def __init__(self):
        self.students = []  # store multiple Student objects

    def add_student(self, student):
        self.students.append(student)

    def show_all_records(self):
        if not self.students:
            print("\n⚠️ No student records found!")
        else:
            print("\n📋 All Student Records:")
            for student in self.students:
                student.display_info()


# -------- Main Program --------
system = GradeSystem()

while True:
    print("\n--- 🎓 CSE Student Grade Management ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    student = Student(name, roll)

    # Add multiple courses
    while True:
        subject = input("Enter course name: ")
        grade = float(input("Enter grade (0.0 - 4.0): "))
        student.add_course(subject, grade)

        more = input("Add another course? (y/n): ").lower()
        if more != 'y':
            break

    system.add_student(student)

    choice = input("\nDo you want to add another student? (y/n): ").lower()
    if choice != 'y':
        break

# Show all student records
system.show_all_records()
