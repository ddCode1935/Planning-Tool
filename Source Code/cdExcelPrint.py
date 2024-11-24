import os

class ExcelPrint:
    def print_to_excel(self, dataframe):
        # Ask user for a directory to save the Excel file, or use current working directory
        file_path = input("\nEnter the full path where the Excel file should be saved"
                          "\n(leave blank to save in current directory): ").strip()

        # If no path is provided, use the current directory
        if not file_path:
            file_path = os.getcwd()  # Current working directory

        # Ask for the filename
        file_name = input("\nEnter the name for the Excel file"
                          "\n(leave blank for 'FinalCoursePlan'): ").strip()

        if not file_name:
            file_name = "FinalCoursePlan"

        # Add .xlsx extension if not provided
        if not file_name.endswith(".xlsx"):
            file_name += ".xlsx"

        # Combine file path and file name to get the full file path
        full_file_path = os.path.join(file_path, file_name)

        try:
            # Save the DataFrame to an Excel file
            dataframe.to_excel(full_file_path, index=False)
            print(f"Data successfully written to {full_file_path}")
        except Exception as e:
            print(f"An error occurred while writing to Excel: {e}")

