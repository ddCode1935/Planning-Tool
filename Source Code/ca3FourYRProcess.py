import pandas as pd

# Adjust the display width and max column width
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_colwidth', None)  # Do not truncate column contents
pd.set_option('display.width', 100)  # Set width to a larger value to avoid truncation


class FourYrScheduleProcessor:
    def __init__(self, user, sched4YrPath):
        self.user = user
        self.sched4YrPath = sched4YrPath
        self.sced4Yr_dataframe =  self.load_4yrSched_data()

    def load_4yrSched_data(self):
        try:
            return self.user.convert_4yr_sched_df(self.sched4YrPath)
        except Exception as e:
            print(f"Error reading the Excel file: {e}")
            return None

    def filter_relevant_courses(self, df):
        filtered_df = df[
            (df['Considered (Y/N)'] == 'Yes, Grad') &
            (df['Offered (Y/N)'] == 'Yes')
            ]
    # Reset the index of the filtered DataFrame
        filtered_df = filtered_df.reset_index(drop=True)
        return filtered_df

    # New method to return the 'Class' column
    def get_class_column(self, filtered_df, schedule_df):
        # Check if the 'Class' column exists in filtered_df
        if 'Class' in filtered_df.columns:
            # Extract the 'Class' column from the filtered_df
            class_column = filtered_df[['Class']]

            # Check if 'Semester', 'Course', and 'Course Title' exist in schedule_df
            required_columns = ['Semester', 'Course', 'Course Title']
            if all(col in schedule_df.columns for col in required_columns):
                # Extract the relevant columns from schedule_df
                schedule_columns = schedule_df[['Semester', 'Course', 'Course Title']]

                # Get unique course values from the class_column
                class_courses = class_column['Class'].unique()

                # Filter schedule_columns to get rows where 'Course' is in class_courses
                filtered_schedule = schedule_columns[schedule_columns['Course'].isin(class_courses)]

                # Reset the index of the filtered schedule
                filtered_schedule.reset_index(drop=True, inplace=True)

                # Return the filtered schedule columns
                return filtered_schedule
            else:
                print(f"Error: One or more required columns {required_columns} not found in the schedule dataframe.")
                return None
        else:
            print("Error: 'Class' column not found in the filtered dataframe.")
            return None




