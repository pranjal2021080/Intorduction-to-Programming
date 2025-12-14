def f(x, y):
    """Function representing the derivative y' = f(x, y)."""
    return x + y

def euler_method(x0, y0, x, h):
    """
    Approximate the solution of the differential equation y' = f(x, y)
    using Euler's method from x0 to x with step size h.

    Parameters:
    x0 (float): Initial x value.
    y0 (float): Initial y value y(x0).
    x (float): The x value at which to find the y value.
    h (float): Step size for the approximation.

    Returns:
    float: Approximated value of y at x.
    """
    n = int((x - x0) / h)
    y = y0
    
    for _ in range(n):
        y += h * f(x0, y)
        x0 += h

    return y
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

def _test():
    """Test function for the Euler method implementation."""
    
    # Test case 1: Check initial condition
    y_at_x0 = euler_method(0, 1, 0, 0.1)
    assert y_at_x0 == 1, "Initial condition test failed"
    
    # Test case 2: Simple test with known results
    # Approximate y(0.1) using Euler's method with y' = x + y and y(0) = 1
    expected_y_0_1 = 1.1  # Since the derivative is x + y, a small step size might hint y ~ y0 + x0 + y0
    y_0_1 = euler_method(0, 1, 0.1, 0.1)
    assert abs(y_0_1 - expected_y_0_1) < 0.05, "Euler method approximation test failed at x = 0.1"

    # Additional test cases
    # Test case 3: Larger step size
    expected_y_0_2 = 1.2  # Approximate y(0.2) with larger step size
    y_0_2 = euler_method(0, 1, 0.2, 0.2)
    assert abs(y_0_2 - expected_y_0_2) < 0.1, "Euler method approximation test failed at x = 0.2 with larger step size"

    # Test case 4: Smaller step size
    expected_y_0_05 = 1.05  # Approximate y(0.05) with smaller step size
    y_0_05 = euler_method(0, 1, 0.05, 0.05)
    assert abs(y_0_05 - expected_y_0_05) < 0.01, "Euler method approximation test failed at x = 0.05 with smaller step size"

    # Test case 5: Different initial condition
    expected_y_0_1_diff_init = 2.2  # Approximate y(0.1) with y(0) = 2
    y_0_1_diff_init = euler_method(0, 2, 0.1, 0.1)
    assert abs(y_0_1_diff_init - expected_y_0_1_diff_init) < 0.05, "Euler method approximation test failed at x = 0.1 with different initial condition"

    print("All tests passed!")

def main():
    """Main function to test Euler's method."""
    _test()  # Run tests

    try:
        x = float(input("Enter the value of x: "))
        h = 0.1  # Step size
        y0 = 1   # Initial condition y(0) = 1
        x0 = 0   # Initial x value

        y = euler_method(x0, y0, x, h)
        print(f"The value of y at x = {x} is approximately {y:.4f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()