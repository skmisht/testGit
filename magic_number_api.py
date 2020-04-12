# api gives user multiple chances of [0,1,2] along with user's attempts (3)
import random
magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "you got the Magic Number!"
    if user_number not in magic_numbers:
        return "you did not get the Magic Number."



def run_program_times(chances):
    for attempt in range(chances):
        print("This is an attempt {}".format(attempt))
        message = ask_user_and_check_number()
        print(message)

attempts_by_user = int(input("Enter the number of attempts: "))
run_program_x_times(attempts_by_user)
