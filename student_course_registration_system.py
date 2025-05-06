students = {
    "1001": {"name": "Ayesha Shoukat", "email": "ayesha@superior.edu.pk", "courses": []},
    "1002": {"name": "Mahnoor Mateen", "email": "mahnoor@superior.edu.pk", "courses": []},
    "1003": {"name": "Zain Ul Hassan", "email": "zain@superior.edu.pk", "courses": []},
    "1004": {"name": "Fatima Ahmed", "email": "fatima@superior.edu.pk", "courses": []},
    "1005": {"name": "Ahmad Ali", "email": "ahmad@superior.edu.pk", "courses": []},
    "1006": {"name": "Muneeb Ahmad", "email": "muneeb@superior.edu.pk", "courses": []},
    "1007": {"name": "Maryam Umair", "email": "maryam@superior.edu.pk", "courses": []},
    "1008": {"name": "Irum Fatima", "email": "irum@superior.edu.pk", "courses": []},
    "1009": {"name": "Laiba Mateen", "email": "laiba@superior.edu.pk", "courses": []},
    "1010": {"name": "Iqra Kanwal", "email": "iqra@superior.edu.pk", "courses": []}
}
courses = {
    "C101": {"name": "Operating Systems", "teacher": "Miss Kashmala", "max": 30, "current": 0, "waitlist": []},
    "C102": {"name": "OS Lab", "teacher": "Mr Muneeb Saleem", "max": 25, "current": 0, "waitlist": []},
    "C201": {"name": "Database Systems", "teacher": "Miss Aimen", "max": 30, "current": 0, "waitlist": []},
    "C202": {"name": "DB Lab", "teacher": "Miss Musharfa", "max": 25, "current": 0, "waitlist": []},
    "M301": {"name": "Discrete Maths", "teacher": "Mr Usama", "max": 40, "current": 0, "waitlist": []},
    "C301": {"name": "Software Design", "teacher": "Miss Irum Fatima", "max": 30, "current": 0, "waitlist": []}
}

def add_course(course_code, course_name, teacher, max_students):
    if course_code in courses:
        print(f"Course {course_code} already exists!")
    else:
        courses[course_code] = {
        "name": course_name,
        "teacher": teacher,
        "max": max_students,
        "current": 0,
        "waitlist": []
        }
        print(f"Course {course_name} ({course_code}) added successfully!")


def add_student(student_id, student_name, student_email):
    if student_id in students:
        print(f"Student {student_id} already exists!")
    else:
        students[student_id] = {
            "name": student_name,
            "email": student_email,
            "courses": []
        }
        print(f"Student {student_name} with student id: {student_id} added successfully!")

def fcfs_registration_for_all_students():
    desired_courses = list(courses.keys())  
    sorted_students = sorted(students.keys())
    for student_id in sorted_students:
        for course_code in desired_courses:
            register(student_id, course_code)


def register(student_id,course_code):
    #chck id is available or not
    if student_id not in students:
        print(f"Student {student_id} not found!")
        return False
    
    #check course id is available or not 
    if course_code not in courses:
        print(f"Course code {course_code} not found!")
        return False
    
    #save the desired studnt id in student
    student = students[student_id]
    #save the desired course code in course
    course = courses[course_code]
    # Check if student is already registered in the course
    if course_code in student["courses"]:
        print(f"Student {student['name']} is already registered in {course['name']}.")
        return False
    
    # Check if student is on waitlist
    if student_id in course["waitlist"]:
        print(f"Student {student_id} is already on the waitlist for {course_code}!")
        return False
    
    # FCFS Registration Logic
    if course["current"] < course["max"]:
        # Register the student
        student["courses"].append(course_code)
        course["current"] += 1
        print(f"Successfully registered {student['name']} ({student_id}) for {course['name']} ({course_code})")
        return True
    else:
        # Add to waitlist
        course["waitlist"].append(student_id)
        print(f"Course {course_code} is full. {student['name']} added to waitlist (position {len(course['waitlist'])})")
        return False

def show_course(course_code):
    # Check if course exists
    if course_code not in courses:
        print("Course not found!")
        return
    
    # Get course details
    course = courses[course_code]
    
    # Print basic info
    print(f"\nCourse: {course['name']} ({course_code})")
    print(f"Teacher: {course['teacher']}")
    print(f"Seats: {course['current']} / {course['max']} filled")
    
    # Show students in course
    print("\nStudents in this class:")
    count = 1
    for student_id in students:
        if course_code in students[student_id]["courses"]:
            print(f"{count}. {students[student_id]['name']}")
            count += 1
    
    # Show waitlist
    print("\nWaitlist:")
    if not course["waitlist"]:
        print("(Empty)")
    else:
        for student_id in course["waitlist"]:
            print(students[student_id]["name"])

def all_courses():
    print("\nAvailable Courses:")
    for course_code, course in courses.items():
        print(f"{course_code}: {course['name']} - {course['teacher']} (Max: {course['max']}, Current: {course['current']})")
        #show how many students are in waiting list only show numbers of student
        if course["waitlist"]:
            print(f"Waitlist: {len(course['waitlist'])} students")
        else:
            print("Waitlist: No students")


def all_students():
    print("\nAll Students:")
    for student_id, student in students.items():
        print(f"{student_id}: {student['name']} - {student['email']}")
        print(f"Registered Courses: {', '.join(student['courses']) if student['courses'] else 'None'}")
        print()



def show_student(student_id):
    if student_id not in students:
        print(f"Student {student_id} not found!")
        return
    
    student = students[student_id]
    print(f"\nStudent: {student['name']} ({student_id})")
    print(f"Email: {student['email']}")
    
    print("\nRegistered Courses:")
    for course_code in student["courses"]:
        course = courses[course_code]
        print(f"- {course['name']} ({course_code}) with {course['teacher']}")


def main_menu():
    print("=== Welcome to Superior University Course Registration ===")
    print("\n--- Course Registration System ---")
    choice=0
    while choice!=7:
        print("1. Register a student for a course")
        print("2. View course information")
        print("3. View student information")
        print("4. Add Course")
        print("5. Add Student")
        print("6. Auto-register all students (FCFS)")
        print("7. Exit")
        

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            register(student_id, course_code)
        elif choice == 2:
            a = input("Do you want to see all courses? (y/n): ")
            if a=='y' or a=='Y':
                all_courses()
            else:
                course_code = input("Enter course code: ")
                show_course(course_code)
        elif choice == 3:
            b= input("Do you want to see all students? (y/n): ")
            if b=='y' or b=='Y':
                all_students()
            else:
                student_id = input("Enter student ID: ")
                show_student(student_id)
        elif choice == 4:
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            teacher = input("Enter teacher's name: ")
            max_students = int(input("Enter maximum number of students: "))
            add_course(course_code, course_name, teacher, max_students)
        elif choice == 5:
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")
            add_student(student_id, student_name, student_email)
        elif choice == 6:
            fcfs_registration_for_all_students()
        elif choice == 7:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu() 


