import math

def calculate_velocity(t):
    assert t >= 0, "Time must be non-negative."
    a = 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t
    return a

def calculate_distance(a, b, delta=0.25):
    assert a >= 0 and b >= 0, "Start and end times must be non-negative."
    assert b > a, "End time must be greater than start time."
    assert delta > 0, "Delta must be positive."
    
    distance = 0
    t = a
    for t in range(int((b - a) / delta)):
        current_time = a + t * delta
        v1 = calculate_velocity(current_time)
        v2 = calculate_velocity(current_time + delta)
        avg_velocity = (v1 + v2) / 2
        distance += avg_velocity * delta
    
    assert distance >= 0, "Calculated distance must be non-negative."
    return distance

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
    # Test case
    start_time = 0
    end_time = 10
    distance = calculate_distance(start_time, end_time)
    assert distance >= 0, "Distance must be non-negative."
    print(f"Distance covered from {start_time}s to {end_time}s: {distance:.2f} meters")

if __name__ == "__main__":
    test()