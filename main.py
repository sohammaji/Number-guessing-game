import time
import random

correct=False
ran_num=random.randint(1,100)  #generates a random number between 1 to 100
counter=1  #creating a counter which countes the number of attempts of the user

while correct==False:
    #taking user input
    n=int(input("Enter any number between 1 to 100: "))
    #in case the entered number is correct
    if n==ran_num:
        correct=True
    #in case the entered number is greater than the actual number
    elif n>ran_num:
        print(f"Number is less than {n}. Try again...")
    #in case the entered number is less than the actual number
    elif n<ran_num:
        print(f"Number is greater than {n}. Try again...")
    counter+=1  #increment of the counter after each attempt

#printing  the result when user guesses the correct number
print(f"You have guessed the correct number in {counter} attempts.")
time.sleep(5)  #shows the result for 5 seconds before exiting the program