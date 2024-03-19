import os
import pandas as pd

# Replace 'file_path.csv' with the path to your CSV file
file_path = 'selenium-twitter-scraper-master/tweets/Extracted.csv'

# Import the CSV file into a pandas DataFrame
dataframe = pd.read_csv(file_path)

# Convert the 'Timestamp' column to datetime format
dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])

# Extract year and month from the timestamp
dataframe['Year_Month'] = dataframe['Timestamp'].dt.to_period('M')

# Group the dataframe by year and month
grouped_by_month = dataframe.groupby('Year_Month')

# Create a folder named 'diary' if it doesn't exist
folder_path = 'diary'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop through each month and concatenate content
for month, group in grouped_by_month:
    month_content = '\n'.join(group['Content'])  # Combine content for the month
    file_name = os.path.join(folder_path, f'{month}.txt')
    with open(file_name, 'w') as file:
        file.write(month_content)

print("Content for each month has been combined and saved into separate text files in the 'diary' folder.")
