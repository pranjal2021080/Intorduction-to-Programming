import random
import requests

def check_valid_word(word):
    """Check if a word exists using the Free Dictionary API"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    return response.status_code == 200

def get_feedback(guess, target):
    """Generate feedback for the guess compared to target word"""
    result = ['-'] * 5
    used_target_chars = set()
    
    # First pass: mark correct positions
    for i in range(5):
        if guess[i] == target[i]:
            result[i] = guess[i]
            used_target_chars.add(i)
    
    # Find chars in wrong positions
    other_chars = set()
    for i, char in enumerate(guess):
        if result[i] == '-':  # if position not already marked correct
            # Check if char exists in target in a position not already used
            for j, target_char in enumerate(target):
                if j not in used_target_chars and char == target_char:
                    other_chars.add(char)
                    used_target_chars.add(j)
                    break
    
    return ''.join(result), sorted(list(other_chars))

def main():
    # List of 50+ five-letter words
    words = [
        "about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again",
        "agent", "agree", "ahead", "alarm", "album", "alert", "alike", "alive", "allow", "alone",
        "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena",
        "arise", "array", "aside", "asset", "audio", "audit", "avoid", "award", "aware", "badly",
        "baker", "bases", "basic", "basis", "beach", "began", "begin", "begun", "being", "below",
        "bench", "billy", "birth", "black", "blame", "blind", "block", "blood", "board", "boost"
    ]
    
    # Select random word
    target_word = random.choice(words)
    max_tries = 6
    tries = 0
    
    print("\nWelcome to the Word Guessing Game!")
    print(f"Try to guess the 5-letter word. You have {max_tries} attempts.")
    print("After each guess, you'll see:")
    print("- Letters in correct positions shown in their positions")
    print("- Letters present in the word but in wrong positions listed separately")
    
    while tries < max_tries:
        guess = input(f"\nEnter your guess ({max_tries - tries} tries left): ").lower()
        
        # Validate input
        if len(guess) != 5:
            print("Please enter exactly 5 characters!")
            continue
            
        if not guess.isalpha():
            print("Please enter only letters!")
            continue
        
        # Check if it's a valid word
        if not check_valid_word(guess):
            print("Not a valid word! Try again.")
            continue
        
        tries += 1
        
        # Check if guess is correct
        if guess == target_word:
            print(f"\nCongratulations! You've won! The word was: {target_word}")
            print(f"You got it in {tries} {'try' if tries == 1 else 'tries'}!")
            return
        
        # Generate feedback
        positions, other_chars = get_feedback(guess, target_word)
        print(f"Feedback: {positions}")
        if other_chars:
            print(f"Other characters present: {' '.join(other_chars)}")
    
    print(f"\nGame Over! The word was: {target_word}")
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
    # Test check_valid_word function
    assert check_valid_word("apple") == True, "Test case for 'apple' failed"
    assert check_valid_word("xyzabc") == False, "Test case for 'xyzabc' failed"

    # Test get_feedback function
    assert get_feedback("apple", "apple") == ("apple", []), "Test case for 'apple' vs 'apple' failed"
    assert get_feedback("apple", "apric") == ("ap--e", ['r', 'i', 'c']), "Test case for 'apple' vs 'apric' failed"
    assert get_feedback("apple", "lemon") == ("--e--", ['l']), "Test case for 'apple' vs 'lemon' failed"
    assert get_feedback("apple", "grape") == ("-p--e", ['a', 'r']), "Test case for 'apple' vs 'grape' failed"
    assert get_feedback("apple", "plums") == ("-l---", ['p']), "Test case for 'apple' vs 'plums' failed"

    print("All test cases passed!")

if __name__ == "__main__":
    main()
    test()