class DirectorySystem:
    def __init__(self):
        self.megalist = []
        
    def _find_or_create_position(self, char, lst):
        """Helper method to find or create position for a character in a list"""
        for item in lst:
            if isinstance(item, list) and item[0] == char:
                return item
        new_list = [char]
        lst.append(new_list)
        # Sort only the list items by their first character
        lst.sort(key=lambda x: x[0] if isinstance(x, list) else '')
        return new_list
    
    def add_word(self, word):
        """Add a word to the directory"""
        word = word.lower()
        if not word:
            return
            
        # Find or create first level
        first_char = word[0]
        found = False
        for item in self.megalist:
            if isinstance(item, list) and item[0] == first_char:
                current = item
                found = True
                break
                
        if not found:
            current = [first_char]
            self.megalist.append(current)
            self.megalist.sort(key=lambda x: x[0] if isinstance(x, list) else '')
        
        # Build nested structure for remaining characters
        for char in word[1:]:
            found = False
            for item in current:
                if isinstance(item, list) and item[0] == char:
                    current = item
                    found = True
                    break
            if not found:
                new_list = [char]
                current.append(new_list)
                current.sort(key=lambda x: x[0] if isinstance(x, list) else '')
                current = new_list
        
        # Add the complete word if it doesn't exist
        if word not in current:
            current.append(word)
        
    def create_directory(self, words):
        """Create directory from a list of space-separated words"""
        for word in words.split():
            self.add_word(word)
            
    def _find_words_with_prefix(self, prefix, current_list, words):
        """Helper method to find all words starting with a given prefix"""
        for item in current_list:
            if isinstance(item, str) and item.startswith(prefix):
                words.append(item)
            elif isinstance(item, list):
                self._find_words_with_prefix(prefix, item, words)
                
    def find_words_with_prefix(self, prefix):
        """Find all words that start with the given prefix"""
        prefix = prefix.lower()
        words = []
        current = self.megalist
        
        # Navigate to the position of the last prefix character
        for char in prefix:
            found = False
            for item in current:
                if isinstance(item, list) and item[0] == char:
                    current = item
                    found = True
                    break
            if not found:
                return []
                
        self._find_words_with_prefix(prefix, current, words)
        return sorted(words)
    
    def _count_words_with_substring(self, substring, current_list):
        """Helper method to count words containing a substring"""
        count = 0
        for item in current_list:
            if isinstance(item, str):
                if substring in item:
                    count += 1
            elif isinstance(item, list):
                count += self._count_words_with_substring(substring, item)
        return count
    
    def count_words_with_substring(self, substring):
        """Count all words containing the given substring"""
        return self._count_words_with_substring(substring.lower(), self.megalist)
    
    def _delete_word_recursive(self, word, current_list):
        """Helper method to recursively delete a word"""
        if not current_list:
            return False
            
        for i, item in enumerate(current_list):
            if isinstance(item, str) and item == word:
                current_list.pop(i)
                return True
            elif isinstance(item, list):
                if self._delete_word_recursive(word, item):
                    # If the list is empty after deletion, remove it
                    if len(item) <= 1:  # Only contains the character
                        current_list.pop(i)
                    return True
        return False
    
    def delete_word(self, word):
        """Delete a word from the directory"""
        return self._delete_word_recursive(word.lower(), self.megalist)
    
    def interactive_search(self):
        """Interactive search system"""
        print("Enter letters one by one (press Enter without input to finish):")
        prefix = ""
        while True:
            char = input(f"Current prefix '{prefix}': ").lower()
            if not char:
                break
            prefix += char
            words = self.find_words_with_prefix(prefix)
            print(f"Words starting with '{prefix}': {words}")
            
    def display_directory(self):
        """Display the current state of the directory"""
        print("Current Directory Structure:")
        print(self.megalist)
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

def main():
    # Create an instance of DirectorySystem
    ds = DirectorySystem()
    
    # Initialize with sample words
    sample_words = "The quick brown fox jumps over the lazy dog"
    ds.create_directory(sample_words)
    
    while True:
        print("\nDirectory System Menu:")
        print("1. Display current directory")
        print("2. Add new word")
        print("3. Delete word")
        print("4. Find words with prefix")
        print("5. Count words with substring")
        print("6. Interactive search")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            ds.display_directory()
            
        elif choice == '2':
            word = input("Enter word to add: ")
            ds.add_word(word)
            print(f"Added '{word}' to directory")
            
        elif choice == '3':
            word = input("Enter word to delete: ")
            if ds.delete_word(word):
                print(f"Successfully deleted '{word}'")
            else:
                print(f"Word '{word}' not found")
                
        elif choice == '4':
            prefix = input("Enter prefix to search: ")
            words = ds.find_words_with_prefix(prefix)
            print(f"Words starting with '{prefix}': {words}")
            
        elif choice == '5':
            substring = input("Enter substring to count: ")
            count = ds.count_words_with_substring(substring)
            print(f"Number of words containing '{substring}': {count}")
            
        elif choice == '6':
            ds.interactive_search()
            
        elif choice == '7':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()