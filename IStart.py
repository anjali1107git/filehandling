def print_words_starting_with_i(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
            
            content = file.read()
            # Split the content into words
            words = content.split()
            # Find words starting with 'i' (case-insensitive)
            words_starting_with_i = [word for word in words if word.lower().startswith('i')]
            # Print the results
            print("Words starting with 'i':")
            for word in words_starting_with_i:
                print(word.strip())
            # Display the total count of such lines
             
print_words_starting_with_i("India.txt")
