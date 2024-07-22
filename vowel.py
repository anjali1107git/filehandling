def print_words_starting_with_vowel(file_name):
    vowels = "aeiouAEIOU"
    with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            # Split the content into words
            words = content.split()
            # Find words starting with a vowel
            words_starting_with_vowel = [word for word in words if word[0] in vowels]
            # Print the results
            print("Words starting with a vowel:")
            for word in words_starting_with_vowel:
                print(word)

print_words_starting_with_vowel("India.txt")