# Magic Number APP - gives users multiple chances of [0,1,2] along with user's attempts (3)
import random

#creating list of 2-random numbers by random.randit(0, 9)
magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number():
    """ask for random number and converted into actual number by int()"""
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "you got the Magic Number!"
    if user_number not in magic_numbers:
        return "you did not get the Magic Number."



def run_program_times(chances):
    """run program 3 times along with attempts message for users"""
    for attempt in range(chances): # repeating attempts 3 times
        print("This is an attempt {}".format(attempt))
        message = ask_user_and_check_number()
        print(message)

attempts_by_user = int(input("Enter the number of attempts: "))
run_program_times(attempts_by_user)
