def read_yearbook_file(filename):
    """Read yearbook data from file and create dictionary"""
    yearbook = {}
    current_student = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.endswith(':'):
                # New student section
                current_student = line[:-1]
                yearbook[current_student] = {}
            elif line and current_student:
                # Signature entry
                name, signed = line.split(',')
                yearbook[current_student][name.strip()] = int(signed.strip())
    
    return yearbook

def find_signature_stats(yearbook):
    """Find students with most and least signatures"""
    signature_counts = {}
    
    # Count signatures for each student
    for student, signatures in yearbook.items():
        count = sum(signatures.values())
        signature_counts[student] = count
    
    # Find max and min counts
    max_count = max(signature_counts.values())
    min_count = min(signature_counts.values())
    
    # Find students with max and min counts
    most_signatures = [student for student, count in signature_counts.items() 
                      if count == max_count]
    least_signatures = [student for student, count in signature_counts.items() 
                       if count == min_count]
    
    return most_signatures, least_signatures
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
    # Test with sample data
    yearbook = {
        'Alice': {'Bob': 1, 'Charlie': 1, 'David': 0},
        'Bob': {'Alice': 1, 'Charlie': 0, 'David': 1},
        'Charlie': {'Alice': 1, 'Bob': 1, 'David': 1},
        'David': {'Alice': 0, 'Bob': 0, 'Charlie': 0}
    }
    
    most, least = find_signature_stats(yearbook)
    print("Students with most signatures:", most)
    print("Students with least signatures:", least)
    
    # Test file reading
    try:
        yearbook = read_yearbook_file('yearbook.txt')
        most, least = find_signature_stats(yearbook)
        print("\nFrom file:")
        print("Students with most signatures:", most)
        print("Students with least signatures:", least)
    except FileNotFoundError:
        print("")

if __name__ == "__main__":
    test()