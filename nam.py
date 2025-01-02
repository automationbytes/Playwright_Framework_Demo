from collections import Counter

# Function to read file and count occurrences of names
def count_names(file_path):
    # Read the file and store names in a list
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file if line.strip()]  # Strip whitespace and ignore empty lines

    # Count occurrences of each name
    name_counts = Counter(names)

    return name_counts

# Specify the path to your text file
file_path = 'your_file.txt'  # Change this to your actual file path

# Get the counts of names
name_counts = count_names(file_path)

# Print the results
for name, count in name_counts.items():
    print(f"{name}: {count}")