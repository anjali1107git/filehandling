def display_short_words(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            short_words = [word for word in words if len(word) < 4]
            for word in short_words:
                print(word)
display_short_words("anjali.txt")
