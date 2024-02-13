class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"Courses enrolled by {self.name}:")
        for course in self.courses:
            print(course.name)
