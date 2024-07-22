def count_uppercase_in_file(file_name):
    with open(file_name, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"The total number of uppercase characters in '{file_name}' is {uppercase_count}.")
count_uppercase_in_file("anjali.txt")
