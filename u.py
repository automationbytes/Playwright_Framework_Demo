import os
import json
import pandas as pd

# Specify the directory containing the folders
base_directory = './your_base_directory'

# Prepare a list to hold the data for the DataFrame
data = []

# Iterate through each folder in the base directory
for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Look for JSON files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('reporto.json') or file_name.endswith('reportm.json'):
                file_path = os.path.join(folder_path, file_name)
                
                # Open and read the JSON file
                with open(file_path, 'r') as json_file:
                    try:
                        json_data = json.load(json_file)
                        
                        # Extract the required information
                        # Assuming the JSON structure has 'total', 'repname', and 'mfa' keys
                        total = json_data.get('total', 0)  # Default to 0 if not found
                        repname = json_data.get('repname', 'N/A')  # Default to 'N/A' if not found
                        mfa = json_data.get('mfa', 'N/A')  # Default to 'N/A' if not found
                        
                        # Append the data to the list
                        data.append({
                            'Folder Name': folder_name,
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