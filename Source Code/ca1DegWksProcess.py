class DegreeWorksProcessor:
    def __init__(self, user, degreeworks_path):
        #Initializes the DegreeWorksProcessor with a user object and a path to the DegreeWorks Excel file.
        self.user = user
        self.degreeworks_path = degreeworks_path
        self.degreeworks_dataframe = self.load_data()
        self.filtered_pendingCourses_df = self.filter_pending_courses()

    def load_data(self):
        #Reads the DegreeWorks data from the specified file path.
        #Returns: DataFrame: The data read from the Excel file.
        try:
            return self.user.convertDegreeWorksFile(self.degreeworks_path)
        except Exception as e:
            print(f"Error reading the Excel file: {e}")
            return None

    def filter_pending_courses(self):
        #Filters the DataFrame for rows where 'Current HRs' is less than 0 (i.e., pending courses).
        #Returns:    DataFrame: A filtered DataFrame with only the pending courses.
        if self.degreeworks_dataframe is not None:
            return self.degreeworks_dataframe[self.degreeworks_dataframe["Current HRs"] < 0].reset_index(drop=True)
        else:
            return None







