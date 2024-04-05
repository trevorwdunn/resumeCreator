# This script is just designed to take in the data used to create a resume. 
# Created by Trevor Dunn
# Created on April 4, 2024
# Desired Function: Create an automated resume without formatting
# Purpose: I'm learning python, and this seemed like a good project to create. 

# Some basic variables
userName # The name of the user
currentEmploymentStatus # Boolean, referes to wehther the user is currently employed
desiredJobType # String; the user selects from Full-Time, Part-Time, or Other (user-specified)
currentEmployer # String, refers to the user's current company name, if applicable
currentJobTitle # String, refers to the user's current job title, if applicable
newToWorkForce # Boolean, 'false' by default, refers to whether this is the user's first job.
standardWorkWeekAvailability # Boolean, refers to whether the user can work from 8-6 on Monday-Friday, automatically set to "False" if desiredJobType is Part-Time.
previousJobCount # integer. This is determined by continually asking the user "Would you like to add job history?" until the user answers in the negative.

# TO DO: 
# Create function to get previous job data for the user. Make sure this function can be called within itself, if necessary. This is done for looping purposes. 
# Create a function which gets the user's skills and can output them
# Create a function which allows a user to add anything of their choosing. This should allow the user to copy and paste formatted information. 

def get_basic_information():
    userName = input("What is your name?\n")
    currentEmploymentStatus = input("Are you currently employed\n")
    desiredJobType = input("""What type of job are you looking for?
                           1) Full-Time | 2) Part-Time | 3) Other""")
    # Use the current employment status to determine whether to ask about employer information. 
    if currentEmploymentStatus == False:
        currentEmployer = "null"
        currentJobTitle = "null"
        newToWorkForce = input("Are you new to the workforce\n")
        if newToWorkForce == True: 
            previousJobCount = 0
        else: 
            previousJobCount = int(input("How many previous jobs have you had? Please enter an integer.\n"))
    else: 
        currentEmployer = input("What is the name of your current employer?\n")
        currentJobTitle = input("What is your current job title\n")
        previousJobCount = int(input("How many jobs have you had in total? Please enter an integer.\n"))
    # TO DO: Implement logic to get schedule availability


def get_previous_job_data():

