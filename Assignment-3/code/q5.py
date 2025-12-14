import os

def upload_marks(file_path):
    """Read marks from a file and store them in a dictionary."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please ensure the file is in the correct directory.")
        return {}

    students = {}
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            roll_no = data[0]
            marks = list(map(float, data[1:]))
            total_marks = sum(marks)
            students[roll_no] = {"marks": marks, "total_marks": total_marks, "grade": None}
    return students


def calculate_cutoffs(students, policy):
    """Calculate grade cutoffs based on the policy."""
    total_scores = sorted([student["total_marks"] for student in students.values()], reverse=True)
    cutoffs = {}

    for i, limit in enumerate(policy):
        grade = "A" if i == 0 else "B" if i == 1 else "C" if i == 2 else "D" if i == 3 else "F"
        lower_limit = max(limit - 2, 0)
        upper_limit = limit + 2

        best_cutoff = None
        max_gap = 0

        for j in range(len(total_scores) - 1):
            if lower_limit <= total_scores[j] <= upper_limit:
                gap = total_scores[j] - total_scores[j + 1]
                if gap > max_gap:
                    max_gap = gap
                    best_cutoff = (total_scores[j] + total_scores[j + 1]) / 2

        cutoffs[grade] = best_cutoff if best_cutoff is not None else lower_limit

    return cutoffs


def do_grading(students, cutoffs):
    """Assign grades to students based on cutoffs."""
    for student in students.values():
        for grade, cutoff in cutoffs.items():
            if student["total_marks"] >= cutoff:
                student["grade"] = grade
                break


def generate_summary(students, assessments, cutoffs):
    """Generate a summary of the grading."""
    print("Assessments and Weights:")
    for assessment, weight in assessments:
        print(f"  {assessment}: {weight}%")

    print("Grade Cutoffs:")
    for grade, cutoff in cutoffs.items():
        print(f"  {grade}: {cutoff:.2f}")

    print("Grade Distribution:")
    grade_counts = {grade: 0 for grade in cutoffs.keys()}
    for student in students.values():
        grade_counts[student["grade"]] += 1

    for grade, count in grade_counts.items():
        print(f"  {grade}: {count}")


def save_grades(students, output_file):
    """Save grades to a file."""
    with open(output_file, "w") as file:
        for roll_no, student in students.items():
            file.write(f"{roll_no}, {student['total_marks']:.2f}, {student['grade']}\n")
    print(f"Grades saved to {output_file}")


def search_student(students, roll_no, assessments):
    """Search and display a student's details."""
    if roll_no in students:
        student = students[roll_no]
        print(f"Roll No: {roll_no}")
        for i, (assessment, _) in enumerate(assessments):
            print(f"  {assessment}: {student['marks'][i]}")
        print(f"Total Marks: {student['total_marks']:.2f}")
        print(f"Grade: {student['grade']}")
    else:
        print(f"Student with roll no {roll_no} not found.")
def test_course_grading():
    """Test function for the Course grading system."""
    # Initialize course
    cname, credits = "Test Course", 3
    assessments = [("Assignment", 40), ("Midterm", 30), ("Final", 30)]
    policy = [85, 70, 55, 40, 20]  # Grade cutoffs
    course = Course(cname, credits, assessments, policy)

    # Simulate uploading marks
    test_data = [
        ("S101", [30, 20, 25]),  # Total: 75
        ("S102", [35, 25, 30]),  # Total: 90
        ("S103", [10, 15, 10]),  # Total: 35
        ("S104", [25, 15, 20])   # Total: 60
    ]
    for roll_no, marks in test_data:
        course.students.append(Student(roll_no, marks))

    # Perform grading
    course.do_grading()

    # Assertions
    assert len(course.students) == 4, "Student count mismatch."
    assert course.students[0].total_marks == 75, "Total marks incorrect for S101."
    assert course.students[1].grade == "A", "Grade assignment incorrect for S102."
    assert course.students[2].grade == "F", "Grade assignment incorrect for S103."
    assert course.cutoffs["A"] == 85, "Incorrect cutoff for grade A."
    assert course.cutoffs["F"] == 20, "Incorrect cutoff for grade F."

    print("All tests passed!")
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned    

# Main Program
cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40, 30]

file_path = "marks.txt"
students = upload_marks(file_path)
if students:
    cutoffs = calculate_cutoffs(students, policy)
    do_grading(students, cutoffs)

    while True:
        print("\nOptions:")
        print("1. Generate Summary")
        print("2. Save Grades to File")
        print("3. Search Student Record")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_summary(students, assessments, cutoffs)
        elif choice == "2":
            output_file = "grades.txt"
            save_grades(students, output_file)
        elif choice == "3":
            roll_no = input("Enter roll number: ")
            search_student(students, roll_no, assessments)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
