import subprocess
import os
import pandas as pd
import csv

def run_scraper():
    command = 'python selenium-twitter-scraper-master/scraper -t 100 -q "Larsen and Tourbo" --latest'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    else:
        print("Scraper executed successfully.")

if __name__ == "__main__":
    run_scraper()
    print("file saved new")


    # Replace 'file_path.csv' with the path to your CSV file
    file_path = 'tweets/Extracted.csv'

    # Import the CSV file into a pandas DataFrame
    dataframe = pd.read_csv(file_path)

    # Convert the 'Timestamp' column to datetime format
    # dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])
    #
    # # Extract year and month from the timestamp
    # dataframe['Year_Month'] = dataframe['Timestamp'].dt.to_period('M')
    #
    # # Group the dataframe by year and month
    # grouped_by_month = dataframe.groupby('Year_Month')
    #
    # Create a folder named 'diary' if it doesn't exist
    folder_path = 'selenium-twitter-scraper-master/diary/new.txt'
    # if not os.path.exists(folder_path):
    #     os.makedirs(folder_path)

    # Loop through each month and concatenate content
    # for month, group in grouped_by_month:
    #     month_content = '\n'.join(group['Content'])  # Combine content for the month
    #     file_name = os.path.join(folder_path, f'new.txt')
    #     with open(file_name, 'w', encoding='utf-8') as file:
    #         file.write(month_content)

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if there is one

        with open(folder_path, 'w') as txt_file:
            for row in csv_reader:
                # Assuming your content is in the first column, change the index if different
                content = row[4]
                txt_file.write(content + '@#$%\n')


    print("Content for each month has been combined and saved into separate text files in the 'diary' folder.")


