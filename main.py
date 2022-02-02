# Its a fun game. The code will generate a random number between 0-10. You have to guess the correct number.

import random

# This option will take input from users
pick = int(input("Enter your number between 0 - 10: "))

# It will generate random number between 0 - 10
rand = random.randrange(0,10)

# The game is begin
if pick == rand:
    print("Yahhhooooo!!! Number ",rand, "is the correct number!!!")

else:
    print("The number was: ", rand,". Please Try Again!!!")
    while (pick != rand):
        pick = int(input("Enter your number between 0 - 10: "))

        rand = random.randrange(0, 10)
        if pick == rand:
            print("Yahhhooooo!!! Number ",rand, "is the correct number!!!")
        else:
            print("The number was: ", rand,". Please Try Again!!!")
