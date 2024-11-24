from ca0InputParser import InputParser

class aUser:
    def __init__(self):
        self._degreeworks_path = None
        self.GradPlan_df = None
        self.sched_4yr_df = None
        self._concentration = None
        self._start_term = None
        self._grad_plan_path = None
        self._yr_schedule_path = None
        self.DegreeWorks_df = None
        self.input_parser = InputParser()


        # Getter and Setter for degreeWorksFilePath
    def get_degreeworks_path(self):
        return self._degreeworks_path
    def set_degreeworks_path(self, path):
        self._degreeworks_path = path

    # Getter and Setter for concentration
    def get_concentration(self):
        return self._concentration
    def set_concentration(self, concentration):
        self._concentration = concentration

    # Getter and Setter for start_term
    def get_start_term(self):
        return self._start_term
    def set_start_term(self, term):
        self._start_term = term

    # Getter and Setter for grad_plan_path
    def get_grad_plan_path(self):
        return self._grad_plan_path

    def set_grad_plan_path(self, path):
        self._grad_plan_path = path

    # Getter and Setter for yr_schedule_path
    def get_yr_schedule_path(self):
        return self._yr_schedule_path

    def set_yr_schedule_path(self, path):
        self._yr_schedule_path = path



    #questions to ask
    #1a
    def ask_for_degreeworks(self):
        path = input("Please enter the path of the updated DegreeWorks document: ")
        self.set_degreeworks_path(path)
        return self.get_degreeworks_path()

    #1b
    def convertDegreeWorksFile(self, degreeworks_path):
        self.DegreeWorks_df = self.input_parser.convert_degreeworks_file(degreeworks_path)
        return self.DegreeWorks_df


    #2 - ask for concentration
    def ask_for_concentration(self):
        concentration = input("\n\nPlease enter the number of concentration as below between 1 and 5\n"
                              "1. CYBR -Cyber Defense\n"
                              "2. CYBR - Manangement\n"
                              "3. ACS -  Software Dev\n"
                              "4. ACS - AI and Data Science\n"
                              "5. ACS - General\n")
        #convert the input to an integer
        try:
            concentration = int(concentration)
        except ValueError:
            return "Invalid input, please enter a number between 1 and 5."

        # Check the input against the available concentration options
        if concentration == 1:
            self.set_concentration("CYBR -Cyber Defense")
        elif concentration == 2:
            self.set_concentration("CYBR - Management")
        elif concentration == 3:
            self.set_concentration("ACS -  Software Dev")
        elif concentration == 4:
            self.set_concentration("ACS -  AI and Data Science")
        elif concentration == 5:
            self.set_concentration("ACS -  General")
        else:
            return "Invalid option selected, please choose between 1 and 5."
        return self.get_concentration()

    #3 ask for the start term either fall or spring
    def ask_start_term(self):
        start_term = input("\nPlease enter your start term (Fall or Spring): ").strip().lower()
        #validate the input
        if start_term == "fall":
            self.set_start_term("Fall")
        elif start_term == "spring":
            self.set_start_term("Spring")
        else:
            return "Invalid input, please enter either 'Fall' or 'Spring'."
        return self.get_start_term()

    #4a
    def ask_for_grad_study_plans(self):
        self.set_grad_plan_path(input("Please enter the path of the Graduate Study Plans Excel document: "))
        return self.get_grad_plan_path()
    #4b
    def convert_grad_study_plan_df(self, gradPlan_path):
        self.GradPlan_df = self.input_parser.convert_grad_study_plan_df(gradPlan_path)
        return self.GradPlan_df

    #5a
    def ask_for_4yr_schedule(self):
        self.set_yr_schedule_path(input("\nPlease enter the path of the 4-year schedule: "))
        return self.get_yr_schedule_path()

    def convert_4yr_sched_df(self, yr_schedule_path):
        self.sched_4yr_df = self.input_parser.convert_4yr_sched_df(yr_schedule_path)
        return self.sched_4yr_df















