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
                    
                    # Extract the required information
                    total = json_data.get('total', 0)  # Default to 0 if not found
                    repname = json_data.get('repname', 'N/A')  # Default to 'N/A' if not found
                    mfa = json_data.get('mfa', 'N/A')  # Default to 'N/A' if not found
                    
                    # Append the data to the list
                    data.append({
                        'Folder Path': dirpath,  # Full path of the folder containing the file
                        'Report Name': repname,
                        'MFA': mfa,
                        'Total': total,
                        'OUD Total': total  # Assuming OUD total is the same as total
                    })
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
output_file = 'report_summary.xlsx'
df.to_excel(output_file, index=False)

print(f"Data written to {output_file}")