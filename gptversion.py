# This is a chatgpt 3.5-generated version of the project. 



# Some basic variables
userName = input("What is your name?\n")
workStatus = input("Are you currently employed? (yes/no)\n").lower() == 'yes'
desiredJobType = input("What type of job are you looking for? (Full-Time/Part-Time/Other)\n")
currentEmployer = input("What is the name of your current employer? (If not applicable, leave blank)\n")
currentJobTitle = input("What is your current job title? (If not applicable, leave blank)\n")
newToWorkForce = input("Is this your first job? (yes/no)\n").lower() == 'yes'
standardWorkWeekAvailability = False if desiredJobType.lower() == 'part-time' else True
previousJobCount = 0

def get_previous_job_data():
    global previousJobCount
    while True:
        answer = input("Would you like to add job history? (yes/no)\n").lower()
        if answer == 'yes':
            previousJobCount += 1
        elif answer == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_user_skills():
    skills = input("Enter your skills (separated by comma):\n").split(',')
    return [skill.strip() for skill in skills]

def add_custom_info():
    custom_info = input("Enter any additional information:\n")
    return custom_info

def create_resume():
    print("\nResume:")
    print(f"Name: {userName}")
    print(f"Currently Employed: {'Yes' if workStatus else 'No'}")
    print(f"Desired Job Type: {desiredJobType}")
    print(f"Current Employer: {currentEmployer}")
    print(f"Current Job Title: {currentJobTitle}")
    print(f"New to Workforce: {'Yes' if newToWorkForce else 'No'}")
    print(f"Standard Work Week Availability: {'Yes' if standardWorkWeekAvailability else 'No'}")
    print(f"Previous Job Count: {previousJobCount}")

    get_previous_job_data()
    print(f"Previous Job Count after getting data: {previousJobCount}")

    skills = get_user_skills()
    print("Skills:")
    for skill in skills:
        print(skill)

    custom_info = add_custom_info()
    print("Additional Information:")
    print(custom_info)

# Call the function to create the resume
create_resume()

