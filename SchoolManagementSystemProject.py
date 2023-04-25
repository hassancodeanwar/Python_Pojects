from abc import ABC, abstractmethod
from typing import List

class Person(ABC):
    def __init__(self, name, national_id):
        self.name = name
        self._national_id = national_id # Protected attribute

    @abstractmethod
    def get_details(self):
        pass

    # Getter method for _national_id
    def get_national_id(self):
        return self._national_id

    # Setter method for _national_id
    def set_national_id(self, national_id):
        self._national_id = national_id


class Student(Person):
    def __init__(self, name, national_id, student_id, grade):
        super().__init__(name, national_id)
        self.student_id = student_id
        self.grade = grade
        self.__enrollment_status = "Enrolled" # Private attribute

    def get_details(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}" \
               f"\nGrade: {self.grade}" \
               f"\nEnrollment Status: {self.__enrollment_status}"

    # Getter method for __enrollment_status
    def get_enrollment_status(self):
        return self.__enrollment_status

    # Setter method for __enrollment_status
    def set_enrollment_status(self, enrollment_status):
        self.__enrollment_status = enrollment_status


class Course:
    def __init__(self, course_id, name, grade):
        self.course_id = course_id
        self.name = name
        self.grade = grade

    def get_course_info(self):
        return f"Name: {self.name}\nCourse ID: {self.course_id}\nGrade: {self.grade}"


class Subject:
    def __init__(self, name):
        self.name = name
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def get_subject_info(self):
        courses_info = "\n".join([course.get_course_info() for course in self.courses])
        return f"Subject Name: {self.name}\nCourses:\n{courses_info}"


class Teacher(Person):
    def __init__(self, name, national_id, salary, subject):
        super().__init__(name, national_id)
        self.salary = salary
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}\nSubject: {self.subject.name}\n"

    # Getter method for salary
    def get_salary(self):
        return self.salary

    # Setter method for salary
    def set_salary(self, salary):
        self.salary = salary


class School:
    def __init__(self, name, address, phone, email, website):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.website = website
        self.teachers: List[Teacher] = []
        self.students: List[Student] = []
        self.courses: List[Course] = []
        self.subjects: List[Subject] = []
    def get_info(self):
        return f"Name: {self.name}" \
               f"\nAddress: {self.address}\nPhone: {self.phone}" \
               f"\nEmail: {self.email}\nWebsite: {self.website}"

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_student(self, student: Student):
        self.students.append(student)

    def add_course(self, course: Course):
        self.courses.append(course)

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)
    
    def get_teachers_details(self):
        return "\n".join([teacher.get_details() for teacher in self.teachers])
       
    def get_students_details(self):
        return "\n".join([student.get_details() for student in self.students])

    def get_subjects_details(self):
        return "\n".join([subject.get_subject_info() for subject in self.subjects])

print("\nSchool INFO...................")
school = School("ABC School", "Egypt-Giza", "0555-5566", "abcschool@gmail.com", "www.ABCSchool.com")
print(school.get_info(), "\n")

# Create courses
course1 = Course("11A", "Arabic", "Grade 1")
course2 = Course("11B", "English", "Grade 1")
course3 = Course("12A", "Frinsh", "Grade 2")
course4 = Course("12B", "Math", "Grade 2")
course5 = Course("13A", "Physics", "Grade 3")
course6 = Course("13B", "Chemistry", "Grade 3")

# Create subjects and add courses to them
subject1 = Subject("Arts")
subject1.add_course(course1)
subject1.add_course(course2)
subject1.add_course(course3)

subject2 = Subject("Engineering")
subject2.add_course(course4)

subject3 = Subject("Science")
subject3.add_course(course5)
subject3.add_course(course6)


# Create teachers
teacher1 = Teacher("Mr. Ahmed", "303071", 3000, subject1)
teacher2 = Teacher("Mr. Mamdouh", "303072", 4000, subject2)
teacher3 = Teacher("Mr. Sayed", "303073", 4000, subject3)
teacher4 = Teacher("Mr. Alaa", "303074", 4000, subject2)
teacher5 = Teacher("Mr. Emaad", "303075", 4000, subject3)
teacher6 = Teacher("Mr. Hamada", "303076", 4000, subject3)

# Create students
student1 = Student("Moaz", "3030", "211943", "Grade 1")
student2 = Student("Hassan", "3031", "211944", "Grade 1")
student3 = Student("Hazem", "3032", "211945", "Grade 2")
student4 = Student("Rmadan", "3033", "211946", "Grade 3")

# Add objects to the school
school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_teacher(teacher3)

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)

school.add_course(course1)
school.add_course(course2)
school.add_course(course3)
school.add_course(course4)
school.add_course(course5)
school.add_course(course6)

school.add_subject(subject1)
school.add_subject(subject2)
school.add_subject(subject3)

# Print details
print("Teachers:")
print(school.get_teachers_details())

print("\n")

print("Students:")
print(school.get_students_details())

# Test getter and setter methods
print("\n")
print("Testing Getter and Setter Methods:")

# Get national_id of student1 (protected attribute)
print(student1.get_national_id())

# Set national_id of student1 using set_national_id() method
student1.set_national_id("3035")

# Get national_id of student1 after changing it
print(student1.get_national_id())

# Get enrollment_status of student1 (private attribute)
try:
    print(student1.__enrollment_status)
except AttributeError:
    print("AttributeError: 'Student' object has no attribute '__enrollment_status'")

# Set enrollment_status of student1 using set_enrollment_status() method
student1.set_enrollment_status("Dropped")

# Get enrollment_status of student1 after changing it
print(student1.get_enrollment_status())

# Get salary of teacher1 (public attribute)
print(teacher1.salary)

# Set salary of teacher1 using set_salary() method
teacher1.set_salary(3500)

# Get salary of teacher1 after changing it
print(teacher1.get_salary())