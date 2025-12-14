import os
import re
import random
from collections import Counter

def calculate_factors(text):
    """Calculate the factors F1, F2, F3, F4, and F5."""
    words = re.findall(r'\b\w+\b', text.lower())  # List of all words (case-insensitive)
    sentences = re.split(r'(?:[.!?])+', text)  # Split text into sentences using punctuation marks
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty and whitespace-only strings
    word_count = len(words)
    unique_word_count = len(set(words))
    sentence_count = len(sentences)
    
    # Factor F1
    F1 = unique_word_count / word_count if word_count > 0 else 0
    
    # Factor F2
    word_freq = Counter(words)
    top_5_count = sum(count for _, count in word_freq.most_common(5))
    F2 = top_5_count / word_count if word_count > 0 else 0
    
    # Factor F3
    long_or_short_sentences = sum(1 for s in sentences if len(s.split()) > 35 or len(s.split()) < 5)
    F3 = long_or_short_sentences / sentence_count if sentence_count > 0 else 0
    
    # Factor F4
    special_pattern = r'[.,;:-]+'
    special_seq = re.findall(special_pattern, text)
    F4 = len(special_seq) / word_count if word_count > 0 else 0
    
    # Factor F5
    F5 = 1 if word_count > 750 else 0

    return F1, F2, F3, F4, F5

def calculate_score(F1, F2, F3, F4, F5):
    """Calculate the net score."""
    return 4 + F1 * 6 + F2 * 6 - F3 - F4 - F5

def process_file(filename):
    """Process a single file and calculate the score and other outputs."""
    with open(filename, 'r') as file:
        text = file.read()

    # Calculate factors
    F1, F2, F3, F4, F5 = calculate_factors(text)
    score = calculate_score(F1, F2, F3, F4, F5)
    
    # Get the most common words and randomly selected words
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)
    most_common_words = [word for word, _ in word_freq.most_common(5)]
    random_words = random.sample(words, min(5, len(words))) if words else []

    return score, most_common_words, random_words
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
 
def test_text_analysis():
    """Test function for text analysis calculations."""
    # Test data
    test_text = (
        "Hello world! This is a test text with a few words. "
        "Some sentences are short. Some sentences are very long, containing more than thirty-five words, which is unusual. "
        "Random punctuation... Test: special; characters, appear: here."
    )
    
    # Expected results for factors
    expected_F1 = 16 / 20  # Unique words: 16, Total words: 20
    expected_F2 = 7 / 20  # Top 5 words appear 7 times
    expected_F3 = 2 / 4   # 2 sentences are very short or very long out of 4 total
    expected_F4 = 6 / 20  # 6 special sequences, Total words: 20
    expected_F5 = 0       # Word count is not greater than 750
    
    # Expected score
    expected_score = 4 + expected_F1 * 6 + expected_F2 * 6 - expected_F3 - expected_F4 - expected_F5
    
    # Test calculate_factors
    F1, F2, F3, F4, F5 = calculate_factors(test_text)
    assert abs(F1 - expected_F1) < 1e-5, f"F1 incorrect: {F1}"
    assert abs(F2 - expected_F2) < 1e-5, f"F2 incorrect: {F2}"
    assert abs(F3 - expected_F3) < 1e-5, f"F3 incorrect: {F3}"
    assert abs(F4 - expected_F4) < 1e-5, f"F4 incorrect: {F4}"
    assert F5 == expected_F5, f"F5 incorrect: {F5}"
    
    # Test calculate_score
    score = calculate_score(F1, F2, F3, F4, F5)
    assert abs(score - expected_score) < 1e-5, f"Score incorrect: {score}"
    
    # Test process_file (using temporary in-memory file)
    from io import StringIO
    
    test_file = StringIO(test_text)
    test_file.name = "test_file.txt"  # Simulating a file name
    with open(test_file.name, "w") as f:
        f.write(test_text)
    
    score, most_common_words, random_words = process_file(test_file.name)
    assert abs(score - expected_score) < 1e-5, f"Process file score incorrect: {score}"
    assert len(most_common_words) == 5, f"Most common words count incorrect: {most_common_words}"
    assert len(random_words) <= 5, f"Random words count incorrect: {random_words}"

    print("All tests passed!")

    
def main():
    # Input: Number of files
    num_files = int(input("Enter the number of files: "))
    filenames = [f"FILE{i + 1}.txt" for i in range(num_files)]

    # Output file
    with open("scores.txt", "w") as output_file:
        for filename in filenames:
            if not os.path.exists(filename):
                print(f"File {filename} not found. Skipping...")
                continue
            
            score, most_common_words, random_words = process_file(filename)
            
            # Write to output file
            output_file.write(f"{filename}\n")
            output_file.write(f"score: {score:.2f}\n")
            output_file.write(f"most common words: {', '.join(most_common_words)}\n")
            output_file.write(f"random words: {', '.join(random_words)}\n")
            output_file.write("\n")

    print("Scores have been written to scores.txt.")

if __name__ == "__main__":
    main()
