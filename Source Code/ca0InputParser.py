import pandas as pd

class InputParser:
    def convert_degreeworks_file(self, degreeworks_path):
        try:
            return pd.read_excel(degreeworks_path)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def convert_grad_study_plan_df(self, grad_plan_path):
        try:
            excel_data = pd.read_excel(grad_plan_path, sheet_name='Updated')
            columns_to_keep = ['Program', 'Start Term', 'Semester', 'Course']
            return excel_data[columns_to_keep]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def convert_4yr_sched_df(self, yr_schedule_path):
        try:
            excel_data = pd.read_excel(yr_schedule_path, sheet_name='Updated')
            columns_to_keep = ['Semester', 'Course', 'Course Title', 'Considered (Y/N)', 'Offered (Y/N)']
            filtered_data = excel_data[columns_to_keep]
            return filtered_data[filtered_data['Offered (Y/N)'] == 'Yes']
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
