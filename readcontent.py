def read_and_display_file():
    with open("anjali.txt", 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without leading/trailing whitespace
read_and_display_file()
