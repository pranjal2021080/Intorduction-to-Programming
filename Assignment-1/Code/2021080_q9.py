import random

def random_walk(n, m):
    assert n > 0 and m > 0, "Target coordinates must be positive integers."
    x, y = 0, 0
    steps = 0
    max_steps = 10000  # Set a reasonable upper limit for steps to avoid infinite loop
    for _ in range(max_steps):
        if x >= n and y >= m:
            break
        direction = random.choice(['x', 'y'])
        distance = random.randint(0, 5)
        if direction == 'x' and x < n:
            x = min(x + distance, n)
        elif direction == 'y' and y < m:
            y = min(y + distance, m)
        steps += 1
    return steps

def average_steps_to_destination(n, m, tolerance=0.1):
    assert 0 < tolerance < 1, "Tolerance must be between 0 and 1."
    total_steps = 0
    prev_avg = float('inf')
    max_walks = 10000  # Set a reasonable upper limit for walks to avoid infinite loop
    
    for num_walks in range(1, max_walks + 1):
        total_steps += random_walk(n, m)
        avg_steps = total_steps / num_walks
        
        if num_walks > 1 and abs(avg_steps - prev_avg) / prev_avg < tolerance:
            break
        
        prev_avg = avg_steps
    
    assert avg_steps > 0, "Average steps should be a positive number."
    assert num_walks <= max_walks, "Number of walks should not exceed the maximum limit."
    
    return avg_steps, num_walks
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
    while True:
        try:
            n = int(input("Enter the x-coordinate of the destination: "))
            m = int(input("Enter the y-coordinate of the destination: "))
            assert n > 0 and m > 0, "Target coordinates must be positive integers."
            break
        except ValueError:
            print("Invalid input. Please enter positive integers for the coordinates.")
        except AssertionError as e:
            print(e)
    
    avg_steps, num_simulations = average_steps_to_destination(n, m)
    
    # Additional assertions
    assert avg_steps > 0, "Average steps should be positive"
    assert num_simulations > 0, "Number of simulations should be positive"
    assert num_simulations <= 10000, "Number of simulations should not exceed the maximum limit"
    assert 0 < avg_steps < (n + m) * 5, "Average steps should be within a reasonable range"
    
    print(f"Destination: ({n}, {m})")
    print(f"Average number of steps: {avg_steps:.2f}")
    print(f"Number of simulations: {num_simulations}")

if __name__ == "__main__":
    test()