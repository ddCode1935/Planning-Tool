class gradPlansProcessor:

    def __init__(self, user, gradPlanPath):
        self.user = user
        self.gradPlanPath = gradPlanPath
        self.gradPlan_dataframe =  self.load_gradPlan_data()

    def load_gradPlan_data(self):
        try:
            return self.user.convert_grad_study_plan_df(self.gradPlanPath)
        except Exception as e:
            print(f"Error reading the Excel file: {e}")
            return None

    def filter_grad_plan(self, concentration, start_term):
        start_term = start_term + " Start"
        # Ensure that the dataframe is not None
        if self.gradPlan_dataframe is not None:
            # Apply the filtering on 'Program' and 'Start Term' columns
            filtered_df = self.gradPlan_dataframe[
                (self.gradPlan_dataframe['Program'] == concentration) &
                (self.gradPlan_dataframe['Start Term'] == start_term)
                ]
            # Reset index of the filtered DataFrame
            filtered_df = filtered_df.reset_index(drop=True)
            return filtered_df
        else:
            print("Graduate Plan DataFrame is empty or not loaded.")
            return None

