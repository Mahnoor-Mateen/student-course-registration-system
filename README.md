# student-course-registration-system

This is a simple Course Registration System developed in Python for Superior University. It allows students to register for various courses and helps administrators manage student enrollments, course capacities, and waitlists. The system uses dictionaries to store student and course data and provides a menu-based interface to interact with.

The program starts by displaying a main menu with options to register students, view course or student information, add new courses or students, and auto-register all students using the First Come First Serve (FCFS) method.

Each course has a maximum seat limit. When the course capacity is full, any further students trying to register are added to the course’s waitlist. The FCFS registration automatically registers all students into available courses in order of their student IDs.

Here is what each menu option does:

1. **Register a student for a course** – You enter a student ID and course code. If there’s space, the student is enrolled; otherwise, they are added to the waitlist.
2. **View course information** – You can view details of all courses or a specific course, including the list of enrolled students and the waitlist.
3. **View student information** – This shows all students or a specific student's details along with their registered courses.
4. **Add Course** – You can add a new course by entering its code, name, teacher’s name, and maximum capacity.
5. **Add Student** – You can add a new student by entering their ID, name, and email.
6. **Auto-register all students (FCFS)** – This option goes through all students and tries to register them into all courses in order of their IDs.
7. **Exit** – Ends the program.

This system is fully interactive and runs in the terminal. It is designed to simulate a university course registration process in a simple and understandable way.


