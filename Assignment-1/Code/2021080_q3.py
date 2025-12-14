def digit_to_text(digit):
    assert 0 <= digit <= 9, "Digit must be between 0 and 9"
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return digits[digit]

def two_digit_to_text(number):
    assert 0 <= number < 100, "Number must be between 0 and 99"
    if number < 10:
        return digit_to_text(number)
    elif number < 20:
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return teens[number - 10]
    else:
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[number // 10] + (" " + digit_to_text(number % 10) if number % 10 != 0 else "")

def convert_number_to_text(number):
    assert 0 <= number < 100, "Number must be between 0 and 99"
    return two_digit_to_text(number)

def run_tests():
    test_numbers = [5, 13, 43, 85, 0, 99]
    expected_results = ["five", "thirteen", "forty three", "eighty five", "", "ninety nine"]
    for num, expected in zip(test_numbers, expected_results):
        result = convert_number_to_text(num)
        print(f"{num}: {result}")
        assert result == expected, f"Test failed for {num}: expected {expected}, got {result}"

if __name__ == "__main__":
    run_tests()
    user_input = int(input("Enter a number between 0 and 99: "))
    print(convert_number_to_text(user_input))