from student import Student
from course import Course

class UserInterface:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, student_id):
        student = Student(name, student_id)
        self.students.append(student)
        return student

    def add_course(self, name, course_id):
        course = Course(name, course_id)
        self.courses.append(course)
        return course

    def enroll_student(self, student, course):
        student.enroll(course)

    def run(self):
        while True:
            print("\n1. Add a Student\n2. Add a Course\n3. Enroll Student in Course\n4. Display Student's Courses\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                student_id = input("Enter student's ID: ")
                self.add_student(name, student_id)
            elif choice == '2':
                name = input("Enter course's name: ")
                course_id = input("Enter course's ID: ")
                self.add_course(name, course_id)
            elif choice == '3':
                student_id = input("Enter student's ID: ")
                course_id = input("Enter course's ID: ")
                student = next((student for student in self.students if student.student_id == student_id), None)
                course = next((course for course in self.courses if course.course_id == course_id), None)
                if student and course:
                    self.enroll_student(student, course)
                    print(f"{student.name} has been enrolled in {course.name}")
                else:
                    print("Student or course not found.")
            elif choice == '4':
                student_id = input("Enter student's ID: ")
                student = next((student for student in self.students if student.student_id == student_id), None)
                if student:
                    student.display_courses()
                else:
                    print("Student not found.")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
