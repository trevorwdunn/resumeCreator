# This script is just designed to take in the data used to create a resume. 

# Some basic variables
userName # The name of the user
workStatus # Boolean, referes to wehther the user is currently employed
desiredJobType # String; the user selects from Full-Time, Part-Time, or Other (user-specified)
currentEmployer # String, refers to the user's current company name, if applicable
currentJobTitle # String, refers to the user's current job title, if applicable
newToWorkForce # Boolean, 'false' by default, refers to whether this is the user's first job.
standardWorkWeekAvailability # Boolean, refers to whether the user can work from 8-6 on Monday-Friday, automatically set to "False" if desiredJobType is Part-Time.
previousJobCount # integer. This is determined by continually asking the user "Would you like to add job history?" until the user answers in the negative.


