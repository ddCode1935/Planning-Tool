##This will be running everything- the control
import aUser
import ca1DegWksProcess
from ca2GradPlanProcess import gradPlansProcessor
from ca3FourYRProcess import FourYrScheduleProcessor
import cbPrereqCheck
from ccCoursePlanner import coursePlanner
from cdExcelPrint import ExcelPrint


user1 = aUser.aUser()

#Part A: Questions asked to User
#1a File path 1- Degreeworks
#current path is : C:\Users\Daniel\Downloads\DegreeWorksUpdated.xlsx
degreeWorksFilePath = user1.ask_for_degreeworks()
print("You entered:", degreeWorksFilePath, "\n\n")
degreeWorks_df= user1.convertDegreeWorksFile(degreeWorksFilePath)
print("Degree Works courses are as follows:\n", degreeWorks_df)

#1b pending course print
degreeWorksProcess1 = ca1DegWksProcess.DegreeWorksProcessor(user1, degreeWorksFilePath)
degreeWorksProcess1.load_data()
pendingClasses= degreeWorksProcess1.filter_pending_courses()
print("\nYour current Pending classes are:\n", pendingClasses)

#2 Ask for concentration
userConcentration1 = user1.ask_for_concentration()
userConcentration2 = user1.get_concentration()
print("Your concentration is:", userConcentration2, "\n")

#3 Ask for start term
startTerm = user1.ask_start_term()
print("Your start term is: ", startTerm, "\n")

#4a Graduate Plans file
#current path is : C:\Users\Daniel\Downloads\Graduate_Study_Plans_Template.xlsx
gradPlanFilePath = user1.ask_for_grad_study_plans()
print("You entered the Graduate Study Plan path:", gradPlanFilePath, "\n")
gradPlan_df= user1.convert_grad_study_plan_df(gradPlanFilePath)

#4b grad plan print
gradPlanProcess1 = gradPlansProcessor(user1, gradPlanFilePath)
allGradPlans_df= gradPlanProcess1.load_gradPlan_data()
filteredGradPlan = gradPlanProcess1.filter_grad_plan(userConcentration2, startTerm)
# DataFrame before printed
print("\nThe summary of the original appropriate course plan\nfor all Graduate Programs is:\n", allGradPlans_df)
# DataFrame after printed
print("\nBelow is what your original Graduate Plan would have been \n"
      "by your specific Program and Start Term:\n", filteredGradPlan)

#5 Four Year Schedule
#current path is : C:\Users\Daniel\Downloads\4-year_schedule_template.xlsx
fourYrSchedPath = user1.ask_for_4yr_schedule()
print("\nYou entered the 4-Year Schedule path:", fourYrSchedPath, "\n\n")


#Part B-
# 4-YR schedule print
yr4Schedule1 = FourYrScheduleProcessor(user1, fourYrSchedPath)
completeSchedule_df= yr4Schedule1.load_4yrSched_data()
filteredSched_df = yr4Schedule1.filter_relevant_courses(completeSchedule_df)
print("\nThis is the entire graduate course schedule for "
      "\nthe next four year:\n", filteredSched_df)

pendingCourseOfferingNext4Yrs = yr4Schedule1.get_class_column(pendingClasses, filteredSched_df)
print("\nBelow is when the courses will be offerred for next 4 years for your specific pending classes."
      "\nConsider taking in them in the earliest semester:\n", pendingCourseOfferingNext4Yrs)

# Prerequisite
Prereq1 =  cbPrereqCheck.PrereqChecker()
prereqUrl = 'https://catalog.columbusstate.edu/course-descriptions/cpsc/'
htmlContent = Prereq1.fetch_webpage(prereqUrl)
courseInfo_df = Prereq1.extract_course_info(htmlContent)
print("Here are the courses and Prereq that were "
      "\nsuccesfully retrieved from the website:\n", courseInfo_df)
Prereq1.save_to_csv(courseInfo_df, 'all_course_prereq.csv')

# Extract Grad courses and that have prequisites only
filtered_course_info_df1 = Prereq1.filter_course_info(courseInfo_df)
print("\nAll of the grad courses with Prequisites are:\n", filtered_course_info_df1)

# Use CoursePlanner (compute) class
coursePlanner1 = coursePlanner()
finalCoursePlan = coursePlanner1.prioritize_courses(pendingCourseOfferingNext4Yrs, filtered_course_info_df1)
print('\n**********************Final Course Plan*********************:\n', finalCoursePlan)

# Print to Excel
excelPrint1 = ExcelPrint()
excelPrint1.print_to_excel(finalCoursePlan)



# Your program logic here

input("Press Enter to exit...")




