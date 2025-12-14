def print_top_half(n, level):
    if level == 0:
        return
    
    # Print stars on the left
    left_stars = '*' * level
    # Calculate and print spaces in the middle
    middle_spaces = ' ' * (2 * (n - level))
    # Print stars on the right
    right_stars = '*' * level
    
    print(left_stars + middle_spaces + right_stars)
    
    # Recursive call for the next level
    print_top_half(n, level - 1)
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

def test_diamond():
    """Test function for diamond printing functions."""
    import io
    import sys
    
    # Capture the output of print statements
    def capture_output(func, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    # Test `print_top_half`
    top_half_result = capture_output(print_top_half, 5, 5)
    expected_top_half = (
        "*****          *****\n"
        "****            ****\n"
        "***              ***\n"
        "**                **\n"
        "*                  *\n"
    )
    assert top_half_result == expected_top_half, "Top half output is incorrect."

    # Test `print_bottom_half`
    bottom_half_result = capture_output(print_bottom_half, 5, 1)
    expected_bottom_half = (
        "*                  *\n"
        "**                **\n"
        "***              ***\n"
        "****            ****\n"
        "*****          *****\n"
    )
    assert bottom_half_result == expected_bottom_half, "Bottom half output is incorrect."

    # Test `print_diamond`
    diamond_result = capture_output(print_diamond, 5)
    expected_diamond = expected_top_half + expected_bottom_half
    assert diamond_result == expected_diamond, "Diamond output is incorrect."

    print("All tests passed for diamond printing functions!")

# Uncomment the following line to run tests when needed
# test_diamond()
    
def print_bottom_half(n, level):
    if level > n:
        return
    
    # Print stars on the left
    left_stars = '*' * level
    # Calculate and print spaces in the middle
    middle_spaces = ' ' * (2 * (n - level))
    # Print stars on the right
    right_stars = '*' * level
    
    print(left_stars + middle_spaces + right_stars)
    
    # Recursive call for the next level
    print_bottom_half(n, level + 1)

def print_diamond(n):
    # Print the top half of the diamond
    print_top_half(n, n)
    # Print the bottom half of the diamond
    print_bottom_half(n, 1)

# Example usage:
# Take user input
n = int(input("Enter the number of levels for the diamond: "))
print_diamond(n)