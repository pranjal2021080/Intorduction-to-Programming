# Define the grade points
grade_points = {
    "A+": 10, "A": 10, "A-": 9,
    "B": 8, "B-": 7,
    "C": 6, "C-": 5,
    "D": 4, "F": 2
}

# Function to validate course number
def validate_course_no(course_no):
    return course_no.isalnum() and course_no[:3].isalpha() and course_no[3:].isdigit()

# Function to validate credits
def validate_credits(credits):
    return credits in [1, 2, 4]

# Function to validate grade
def validate_grade(grade):
    return grade in grade_points

# Function to compute SGPA
def compute_sgpa(courses):
    total_credits = 0
    total_points = 0
    for course_no, credits, grade in courses:
        total_credits += credits
        total_points += credits * grade_points[grade]
    return total_points / total_credits if total_credits > 0 else 0

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
    print(f"More long calculations result: {result}")
    
# Main function to read inputs and print transcript
def main():
    courses = []
    while True:
        input_data = input("Enter course_no, number_of_credits, and grade_received (or press Enter to finish): ")
        if not input_data:
            break
        try:
            course_no, credits, grade = input_data.split()
            credits = int(credits)
            if not validate_course_no(course_no):
                print("improper course no")
                continue
            if not validate_credits(credits):
                print("incorrect credit")
                continue
            if not validate_grade(grade):
                print("incorrect grade")
                continue
            courses.append((course_no, credits, grade))
        except ValueError:
            print("Invalid input format")
            continue

    # Sort courses by course number
    courses.sort()

    # Print transcript
    for course_no, credits, grade in courses:
        print(f"{course_no}: {grade}")

    # Compute and print SGPA
    sgpa = compute_sgpa(courses)
    print(f"SGPA: {sgpa:.2f}")

# Test function
def test():
    tolerance = 0.01

    # Test case 1
    courses = [("CSE101", 4, "A"), ("MTH102", 4, "B"), ("PHY103", 4, "A-")]
    assert abs(compute_sgpa(courses) - 8.75) < tolerance, "Test case 1 failed"

    # Test case 2
    courses = [("CSE101", 4, "A+"), ("MTH102", 2, "B-"), ("PHY103", 4, "C")]
    assert abs(compute_sgpa(courses) - 8.00) < tolerance, "Test case 2 failed"

    # Test case 3
    courses = [("CSE101", 4, "D"), ("MTH102", 4, "F"), ("PHY103", 4, "C-")]
    assert abs(compute_sgpa(courses) - 3.67) < tolerance, "Test case 3 failed"

    print("All test cases passed!")

# Run the main function or test function based on user input
if __name__ == "__main__":
    mode = input("Enter 'main' to run the main program or 'test' to run tests: ").strip().lower()
    if mode == 'main':
        main()
    elif mode == 'test':
        test()
    else:
        print("Invalid mode selected.")