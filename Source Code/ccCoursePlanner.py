class coursePlanner:
    def prioritize_courses(self, schedule_df, prereq_df):
        # Drop duplicate courses to retain only the first occurrence
        unique_courses_df = schedule_df.drop_duplicates(subset=['Course'], keep='first')

        # Iterate over the courses in the schedule_df
        for _, row in unique_courses_df.iterrows():
            course = row['Course']

            # Check if the course is in the 'Course Code' column of prereq_df
            prereq_row = prereq_df[prereq_df['Course Code'] == course]

            if not prereq_row.empty:
                # Get the prerequisite for this course
                prerequisite = prereq_row['Prerequisite'].values[0]

                # Print the message
                print(f"\nYour pending Course : {course} has prerequisite of {prerequisite}, please take this course {prerequisite} first")

        # Return the dataframe with only the first occurrence of each course
        return unique_courses_df

