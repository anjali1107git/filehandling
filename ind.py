def count_word_occurrences(file_name, target_word):
    with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            # Convert the entire text to lowercase to make the search case-insensitive
            text_lower = text.lower()
            # Split the text into words
            words = text_lower.split()
            # Count occurrences of the target word
            word_count = words.count(target_word.lower())
            print(f"The word '{target_word}' occurs {word_count} times in the file '{file_name}'.")

count_word_occurrences("India.txt", "India")

