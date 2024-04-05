# This script is just designed to take in the data used to create a resume. 
# Created by Trevor Dunn
# Created on April 4, 2024
# Desired Function: Create an automated resume without formatting
# Purpose: I'm learning python, and this seemed like a good project to create. 

# Some basic variables
userName # The name of the user
workStatus # Boolean, referes to wehther the user is currently employed
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
