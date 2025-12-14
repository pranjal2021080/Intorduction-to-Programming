def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sin(x):
    x = x * (3.14159 / 180)  # Convert to radians
    result = 0
    n = 0
    term = x  # First term in the series
    while n < 10:  # 10 terms of Taylor series
        result += term
        n += 1
        term = (-1)**n * x**(2*n + 1) / factorial(2*n + 1)
    return result

def cos(x):
    x = x * (3.14159 / 180)  # Convert to radians
    result = 0
    n = 0
    term = 1  # First term in the series
    while n < 10:  # 10 terms of Taylor series
        result += term
        n += 1
        term = (-1)**n * x**(2*n) / factorial(2*n)
    return result

def tan(x):
    return sin(x) / cos(x)

def calculate_pole_height(angle, distance):
    height = distance * tan(angle)
    tip_distance = distance / cos(angle)
    return height, tip_distance

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
    
    # Test sin function
    assert abs(sin(30) - 0.5) < 0.001, "sin(30) should be approximately 0.5"
    assert abs(sin(90) - 1.0) < 0.001, "sin(90) should be approximately 1.0"
    assert abs(sin(0) - 0.0) < 0.001, "sin(0) should be approximately 0.0"
    
    # Test cos function
    assert abs(cos(60) - 0.5) < 0.001, "cos(60) should be approximately 0.5"
    assert abs(cos(0) - 1.0) < 0.001, "cos(0) should be approximately 1.0"
    assert abs(cos(90) - 0.0) < 0.001, "cos(90) should be approximately 0.0"
    
    # Test tan function
    assert abs(tan(45) - 1.0) < 0.001, "tan(45) should be approximately 1.0"
    assert abs(tan(0) - 0.0) < 0.001, "tan(0) should be approximately 0.0"
    
    # Test calculate_pole_height function
    height, tip_distance = calculate_pole_height(45, 10)
    assert abs(height - 10.0) < 0.001, "Height of the pole at 45 degrees and 10 meters distance should be approximately 10 meters"
    assert abs(tip_distance - 14.142) < 0.001, "Tip distance of the pole at 45 degrees and 10 meters distance should be approximately 14.142 meters"

    angle = float(input("Enter the angle of view (in degrees): "))
    distance = float(input("Enter the horizontal distance to the pole (in meters): "))
    
    height, tip_distance = calculate_pole_height(angle, distance)
    print(f"pole height: {height:.2f} meters")
    print(f"Distance to the tip of the pole: {tip_distance:.2f} meters")

if __name__ == "__main__":
    test()