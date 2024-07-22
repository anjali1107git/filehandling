def count_words_in_file(file_name):
    with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            print(f"The total number of words in '{file_name}' is {word_count}.")

count_words_in_file("anjali.txt")
