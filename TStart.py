def count_and_display_lines_starting_with_t(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
            # Initialize a counter for lines starting with 'T'
            count = 0
            # Read and process each line
            for line in file:
                # Check if the line starts with 'T' (case-insensitive)
                if line.strip().lower().startswith('t'):
                    count += 1
                    print(line.strip())
            # Display the total count of such lines
            print(f"\nTotal number of lines starting with 'T': {count}")
 
# Usage
count_and_display_lines_starting_with_t("India.txt")

