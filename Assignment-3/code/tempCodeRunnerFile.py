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
n = 5
print_diamond(n)