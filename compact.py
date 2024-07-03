import pandas as pd

# List of file names
file_names = ['File1.xlsx', 'File2.xlsx']

# Create an empty list to store individual DataFrames
data_frames = []

# Loop through each file and read the data into a DataFrame, then append it to the list
for file in file_names:
    data = pd.read_excel(file)
    data_frames.append(data)

# Concatenate all DataFrames in the list into a single DataFrame
combined_data = pd.concat(data_frames, ignore_index=True)

# Write the combined data to a new Excel file
combined_data.to_excel('combined_data.xlsx', index=False)
