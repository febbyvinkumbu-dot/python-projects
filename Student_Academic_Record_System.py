
# ==========================================
# STUDENT ACADEMIC RECORD MANAGEMENT SYSTEM
# Name: Your Full Name
# Student ID: Your Student Number
# ==========================================

students = {}


# ==========================================
# HELPER FUNCTIONS
# ==========================================
def get_valid_mark(course_name):
    while True:
        try:
            mark = int(input(f"Enter marks for {course_name} (0 - 100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")


def determine_grade(avg):
    if avg >= 75:
        return "A"
    if avg >= 65:
        return "B"
    if avg >= 50:
        return "C"
    if avg >= 40:
        return "D"
    return "F"


# ==========================================
# ADD NEW STUDENT
# ==========================================
def register_student():
    student_id = input("Student ID: ")

    if student_id in students:
        print("This student already exists.")
        return

    full_name = input("Full Name: ")
    program_name = input("Program: ")

    courses = {}
    try:
        count = int(input("How many courses? "))
    except ValueError:
        print("Invalid number.")
        return

    for i in range(count):
        course = input(f"Course {i + 1} name: ").title()
        courses[course] = get_valid_mark(course)

    students[student_id] = {
        "name": full_name,
        "program": program_name,
        "courses": courses
    }

    print("Student successfully registered.")


# ==========================================
# DISPLAY ALL STUDENTS
# ==========================================
def display_students():
    if not students:
        print("No students found.")
        return

    print("\nRegistered Students:")
    for sid, details in students.items():
        print(f"- {sid}: {details['name']}")


# ==========================================
# STUDENT REPORT
# ==========================================
def student_report():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student record not found.")
        return

    student = students[student_id]
    marks = student["courses"]

    total = sum(marks.values())
    average = total / len(marks)
    grade = determine_grade(average)

    print("\n====== STUDENT REPORT ======")
    print("Name   :", student["name"])
    print("Program:", student["program"])
    print("\nCourses and Marks:")
    for course, score in marks.items():
        print(f"  {course} -> {score}")

    print("\nTotal Marks :", total)
    print("Average     :", round(average, 2))
    print("Final Grade :", grade)


# ==========================================
# MODIFY STUDENT MARKS
# ==========================================
def modify_marks():
    student_id = input("Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    course = input("Course to update: ").title()

    if course not in students[student_id]["courses"]:
        print("Course does not exist.")
        return

    students[student_id]["courses"][course] = get_valid_mark(course)
    print("Marks updated successfully.")


# ==========================================
# REMOVE STUDENT
# ==========================================
def remove_student():
    student_id = input("Enter Student ID to remove: ")

    if student_id in students:
        del students[student_id]
        print("Student record removed.")
    else:
        print("Student not found.")


# ==========================================
# MAIN MENU
# ==========================================
def run_system():
    while True:
        print("""
========= STUDENT RECORD SYSTEM =========
1. Register Student
2. View All Students
3. View Student Report
4. Update Student Marks
5. Delete Student
6. Exit
""")

        choice = input("Select option (1-6): ")

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            student_report()
        elif choice == "4":
            modify_marks()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            print("Exiting system. Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


# ==========================================
# PROGRAM START
# ==========================================
run_system()
