import requests
from bs4 import BeautifulSoup
import pandas as pd

class PrereqChecker:
    # 1 Fetching Webpage Content
    def fetch_webpage(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\nSuccessfully retrieved the webpage for Prerequisites. The original site is:\n{url}\n\n")
            return response.text
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

    #2 Extract course codes and prequisites
    def extract_course_info(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        courseblocks = soup.find_all('div', class_='courseblock')

        # Initialize lists to store course codes and prerequisites
        course_codes = []
        prerequisites = []

        # Iterate over each course block
        for courseblock in courseblocks:
            # Extract course code
            code_element = courseblock.find('span', class_='detail-code')
            code = code_element.strong.text.strip() if code_element and code_element.strong else 'No Code Found'
            course_codes.append(code)

            # Extract prerequisite
            prerequisite_link = courseblock.find('a', class_='bubblelink')
            prerequisite = prerequisite_link.text.strip() if prerequisite_link else 'None'  # Get text if available
            prerequisites.append(prerequisite)

        # Print the extracted course codes and prerequisites
        print("Course Codes and Prerequisites:")

        # create a datframe from the lists
        course_info_df = pd.DataFrame({
            'Course Code': course_codes,
            'Prerequisite': prerequisites
        })

        # Modify the 'Prerequisite' column to keep only the last 4 characters
        course_info_df['Prerequisite'] = course_info_df['Prerequisite'].apply(lambda x: x[-4:] if len(x) >= 4 else x)
        return course_info_df

    #3 Method to just return dataframe with Grad courses and that have prequisites &
    # filter DataFrame based on prerequisites and course codes
    def filter_course_info(self, dataframe):
        # Filter out rows where 'Prerequisite' is 'None'
        filtered_df = dataframe[dataframe['Prerequisite'] != 'None'].copy()
        # Filter for 'Course Code' values that are 6000 or greater- Grad courses only
        filtered_df = filtered_df[filtered_df['Course Code'].str[-4] == '6']
        # Reset index to start from 0
        filtered_df.reset_index(drop=True, inplace=True)
        return filtered_df

    #4 Method to save DataFrame to a CSV file
    def save_to_csv(self, dataframe, filename):
        dataframe.to_csv(filename, index=False)
        print(f"\nData with all Prerequisites saved to {filename}\n")

