def polynomial(x):
    """Compute the value of the polynomial x^3 - 10.5*x^2 + 34.5*x - 35."""
    return x**3 - 10.5*x**2 + 34.5*x - 35

def derivative(x):
    """Compute the derivative of the polynomial x^3 - 10.5*x**2 + 34.5*x - 35."""
    return 3*x**2 - 21*x + 34.5

def newton_raphson(f, df, x0, epsilon=0.2, max_iterations=100):
    """
    Use the Newton-Raphson method to find a root of the polynomial.

    Parameters:
    f: The polynomial function.
    df: The derivative of the polynomial function.
    x0: The initial guess for the root.
    epsilon: The tolerance level to determine convergence.
    max_iterations: The maximum number of iterations allowed.

    Returns:
    The root found within the tolerance level, or None if no root is found.
    """
    x = x0

    for iteration in range(max_iterations):
        fx = f(x)
        if abs(fx) < epsilon:
            return x
        dfx = df(x)
        if dfx == 0:
            return None
        x = x - fx / dfx
    
    return None

def find_all_roots(f, df, x1, x2, step=0.5, epsilon=0.2, max_iterations=100):
    """
    Find all roots of the polynomial within the range [x1, x2] using the Newton-Raphson method.

    Parameters:
    f: The polynomial function.
    df: The derivative of the polynomial function.
    x1: The start of the range.
    x2: The end of the range.
    step: The step size for initial guesses.
    epsilon: The tolerance level to determine convergence.
    max_iterations: The maximum number of iterations allowed.

    Returns:
    A list of roots found within the range.
    """
    roots = []
    num_steps = int((x2 - x1) / step) + 1

    for i in range(num_steps):
        x = x1 + i * step
        root = newton_raphson(f, df, x, epsilon, max_iterations)
        if root is not None:
            # Check if the root is already found
            if not any(abs(root - r) < epsilon for r in roots):
                roots.append(root)
    
    return roots

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
    
def test():
    """Comprehensive test function with multiple assert statements."""
    # Known roots of the polynomial x**3 - 10.5*x**2 + 34.5*x - 35
    known_roots = [1.0, 3.0, 6.5]
    epsilon = 0.2
    
    # Test each known root
    for known_root in known_roots:
        found_root = newton_raphson(polynomial, derivative, known_root)
        assert abs(polynomial(found_root)) < epsilon, f"Root {known_root} not found"
    
    # Additional test cases with different initial guesses
    initial_guesses = [0.5, 2.5, 5.0, 7.0]
    for guess in initial_guesses:
        found_root = newton_raphson(polynomial, derivative, guess)
        assert any(abs(found_root - root) < epsilon for root in known_roots), f"Root not found for initial guess {guess}"
    
    # Test the find_all_roots function
    found_roots = find_all_roots(polynomial, derivative, 0, 10)
    for known_root in known_roots:
        assert any(abs(found_root - known_root) < epsilon for found_root in found_roots), f"Root {known_root} not found in range"
    
    # Edge case: No roots in the range
    no_roots = find_all_roots(polynomial, derivative, -10, -5)
    assert len(no_roots) == 0, "No roots should be found in the range [-10, -5]"
    
    # Edge case: Single point range
    single_point_root = newton_raphson(polynomial, derivative, 1.0)
    assert abs(polynomial(single_point_root)) < epsilon, "Root not found for single point range"

def main():
    while True:
        print("\nMenu:")
        print("1. Find a single root using the Newton-Raphson method")
        print("2. Find all roots within a given range")
        print("3. Run tests")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Ask for the initial guess x0 with input validation
            while True:
                try:
                    x0 = float(input("Enter the initial guess for the root (x0): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            
            # Find the root using the Newton-Raphson method
            root = newton_raphson(polynomial, derivative, x0)
            
            if root is not None:
                print(f"Root found: {root}")
            else:
                print("No root found within the given number of iterations.")
        
        elif choice == '2':
            # Ask for the range x1 and x2 with input validation
            while True:
                try:
                    x1 = float(input("Enter the start of the range (x1): "))
                    x2 = float(input("Enter the end of the range (x2): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values for the range.")
            
            # Find all roots within the given range
            roots = find_all_roots(polynomial, derivative, x1, x2)
            
            if roots:
                print(f"Roots found in the range [{x1}, {x2}]: {roots}")
            else:
                print(f"No roots found in the range [{x1}, {x2}].")
        
        elif choice == '3':
            # Run the test function
            test()
            print("All tests passed successfully.")
        
        elif choice == '4':
            # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()