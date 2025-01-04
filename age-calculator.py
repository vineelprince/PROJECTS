#AGE CALCULATOR PROGRAM

from datetime import datetime

def age_calculator():
    print("**********Welcome to the Age Calculator Program**********")
    print("Enter your date of birth in the following format: YYYY-MM-DD")
    dob = input("Date of Birth: ")
    dob = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    print(f"You are {age} years old.")
    
age_calculator()

#END OF PROGRAM
