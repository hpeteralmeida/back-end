# Second George's lesson about programming languages 
# This code is set to verificate if a password is correct

define_password = str(input("Set a password: "))
# The first line is the start of the code, requiring the user to create a password
attempts = 3
# This line tells the program how may attemps the user still has
while attempts > 0:
    # This sets a cycle that runs until the number of attempts is 0
    confirm_password = str(input("Confirm youe password: "))
    # The user has to confirm the password here
    if confirm_password == define_password:
        print("Correct password")
        break
        #This line verifies if the password is correct and, if so, breaks the cycle 
    else:
        attempts -= 1
        if attempts > 0:
            print (f"incorrect password. Try again! \nYou still have {attempts} attempts")
        # if the password is incorrect, the user loses one attempt and is asked to try again
        else:
            print ("You have used all your attempts")
            # if the user runs out of attemps, the programm ends  
