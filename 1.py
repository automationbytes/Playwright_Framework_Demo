import os
import json
import pandas as pd

# Specify the base directory containing the folders
base_directory = './your_base_directory'

# Prepare a list to hold the data for the DataFrame
data = []

# Use os.walk to traverse the directory tree
for dirpath, dirnames, filenames in os.walk(base_directory):
    for file_name in filenames:
        # Check for the specific JSON file endings
        if file_name.endswith('reportoud.json') or file_name.endswith('reportmfa.json'):
            file_path = os.path.join(dirpath, file_name)
            
            # Open and read the JSON file
            with open(file_path, 'r') as json_file:
                try:
                    json_data = json.load(json_file)
                    
                    # Check if json_data is a list
                    if isinstance(json_data, list):
                        # Initialize a dictionary to count occurrences of file paths
                        file_path_count = {}
                        
                        for item in json_data:
                            # Get the file_path
                            path = item.get('file_path')
                            if path:
                                # Increment the count for this file_path
                                if path in file_path_count:
                                    file_path_count[path] += 1
                                else:
                                    file_path_count[path] = 1
                        
                        # Now, we can prepare the data for the DataFrame
                        for path, count in file_path_count.items():
                            data.append({
                                'Folder Path': dirpath,  # Full path of the folder containing the file
                                'Report Name': file_name,
                                'Total': count,  # Count of occurrences of this file_path
                                'OUD Total': count  # Assuming OUD total is the same as total
                            })
                    else:
                        print(f"Unexpected JSON structure in file: {file_path}")

                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
output_file = 'report_summary.xlsx'
df.to_excel(output_file, index=False)

print(f"Data written to {output_file}")