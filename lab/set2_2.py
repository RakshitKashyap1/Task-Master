class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def __str__(self):
        return f"{self.__class__.__name__}({self.person_id}): {self.name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.courses = []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has been enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")

    def __str__(self):
        return (f"Student({self.person_id}): {self.name}, "
                f"Enrolled Courses: {[course.name for course in self.courses]}")


class Teacher(Person):
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)
        self.courses_taught = []

    def assign_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)
            print(f"{self.name} has been assigned to teach {course.name}.")
        else:
            print(f"{self.name} is already teaching {course.name}.")

    def __str__(self):
        return (f"Teacher({self.person_id}): {self.name}, "
                f"Courses Taught: {[course.name for course in self.courses_taught]}")


class Course:
    def __init__(self, name, course_id, teacher=None):
        self.name = name
        self.course_id = course_id
        self.teacher = teacher
        self.students = []

    def assign_teacher(self, teacher):
        if self.teacher is None:
            self.teacher = teacher
            teacher.assign_course(self)
            print(f"{teacher.name} has been assigned as the teacher for {self.name}.")
        else:
            print(f"{self.name} already has a teacher assigned.")

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self)
            print(f"{student.name} has been enrolled in {self.name}.")
        else:
            print(f"{student.name} is already enrolled in {self.name}.")

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "None"
        return (f"Course({self.course_id}): {self.name}, "
                f"Teacher: {teacher_name}, Students: {[student.name for student in self.students]}")


class School:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student):
        if student.person_id not in self.students:
            self.students[student.person_id] = student
            print(f"Added {student}")
        else:
            print(f"Student ID {student.person_id} already exists.")

    def add_teacher(self, teacher):
        if teacher.person_id not in self.teachers:
            self.teachers[teacher.person_id] = teacher
            print(f"Added {teacher}")
        else:
            print(f"Teacher ID {teacher.person_id} already exists.")

    def add_course(self, course):
        if course.course_id not in self.courses:
            self.courses[course.course_id] = course
            print(f"Added {course}")
        else:
            print(f"Course ID {course.course_id} already exists.")

    def get_student(self, student_id):
        return self.students.get(student_id, None)

    def get_teacher(self, teacher_id):
        return self.teachers.get(teacher_id, None)

    def get_course(self, course_id):
        return self.courses.get(course_id, None)

    def __str__(self):
        return (f"School({self.name}) - "
                f"{len(self.students)} students, {len(self.teachers)} teachers, {len(self.courses)} courses")


def main():
    my_school = School("My School")

    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Assign Teacher to Course")
        print("5. Enroll Student in Course")
        print("6. Display Students")
        print("7. Display Teachers")
        print("8. Display Courses")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            my_school.add_student(student)

        elif choice == '2':
            name = input("Enter teacher name: ")
            teacher_id = input("Enter teacher ID: ")
            teacher = Teacher(name, teacher_id)
            my_school.add_teacher(teacher)

        elif choice == '3':
            name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            course = Course(name, course_id)
            my_school.add_course(course)

        elif choice == '4':
            course_id = input("Enter course ID: ")
            course = my_school.get_course(course_id)
            if course:
                teacher_id = input("Enter teacher ID: ")
                teacher = my_school.get_teacher(teacher_id)
                if teacher:
                    course.assign_teacher(teacher)
                else:
                    print("Teacher not found.")
            else:
                print("Course not found.")

        elif choice == '5':
            course_id = input("Enter course ID: ")
            course = my_school.get_course(course_id)
            if course:
                student_id = input("Enter student ID: ")
                student = my_school.get_student(student_id)
                if student:
                    course.enroll_student(student)
                else:
                    print("Student not found.")
            else:
                print("Course not found.")

        elif choice == '6':
            print("\nStudents:")
            for student in my_school.students.values():
                print(student)

        elif choice == '7':
            print("\nTeachers:")
            for teacher in my_school.teachers.values():
                print(teacher)

        elif choice == '8':
            print("\nCourses:")
            for course in my_school.courses.values():
                print(course)

        elif choice == '9':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()