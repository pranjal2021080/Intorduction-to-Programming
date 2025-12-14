def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices
    Returns None if matrices cannot be multiplied
    """
    if len(matrix1[0]) != len(matrix2):
        return None
        
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] 
                        for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    return result

def scale_shape(coordinates, cx, cy):
    """
    Scale a 2D shape given by coordinates using scaling factors cx and cy
    """
    # Create shape matrix
    shape_matrix = [[coord[0], coord[1], 1] for coord in coordinates]
    
    # Create scaling matrix
    scaling_matrix = [
        [cx, 0, 0],
        [0, cy, 0],
        [0, 0, 1]
    ]
    
    # Multiply matrices
    result = matrix_multiply(shape_matrix, scaling_matrix)
    
    # Extract new coordinates
    return [(row[0], row[1]) for row in result]

def test():
    # Test matrix multiplication
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = matrix_multiply(matrix1, matrix2)
    assert result == [[19, 22], [43, 50]]
    
    # Test shape scaling
    shape = [(1, 1), (2, 2), (3, 1)]
    scaled_shape = scale_shape(shape, 2, 3)
    expected = [(2, 3), (4, 6), (6, 3)]
    
    # Compare with small tolerance for floating point differences
    for (x1, y1), (x2, y2) in zip(scaled_shape, expected):
        assert abs(x1 - x2) < 0.0001 and abs(y1 - y2) < 0.0001

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

if __name__ == "__main__":
    # Example usage
    shape = [(0, 0), (1, 0), (1, 1), (0, 1)]
    cx = float(input("Enter x scaling factor: "))
    cy = float(input("Enter y scaling factor: "))
    
    new_shape = scale_shape(shape, cx, cy)
    print("Original shape:", shape)
    print("Scaled shape:", new_shape)
    
    test()