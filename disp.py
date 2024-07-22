def display_lines_with_more_than_twelve_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Iterate over each line
            for line in lines:
                words = line.split()
                # Check if the line has more than twelve words
                if len(words) > 20:
                    print(line.strip())

display_lines_with_more_than_twelve_words("India.txt")
#