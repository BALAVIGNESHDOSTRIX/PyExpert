'''

DEVELOPER NAME: M.BALAVIGNESH
IMPLEMENTED DATE : 17-11-2018

            ProjectName : GessMe

            Project Scope Details:
                This project is simple Example for how use the variable and import packages in real project
                and this is also simple game so you can play

            Project Uage Details:
                The Player have to enter the number from 1 to 5 and the System will guess the number from 1 to 5
                by using the randint() method from python random package i have imported here. when user entering
                the input number time the randint() also choosed the one number from 1 to 5 if the user entered and
                random method choosed number is equal it will print the use successfully choosed info or if not means
                print the try again statement.
'''

import random as rand #Package imported and as (alias)

class GuessMe:

    @staticmethod          #(Staticmethod decorator) for syaying this is a static method
    def FindGuess():

        Taken_num = int(input("Enter a Guess Number (1 to 5) : "))

        System_Guess = rand.randint(1,5) #randint(1,5) method to generate the random number within the 1 to 5

        if Taken_num == System_Guess:
            print("You are Guessed Correct No. Well done & Good Job dude")
        else:
            print("You are Guessed Wrong No. Sorry!..... Please Try again.")

guess = GuessMe() #Object creation
guess.FindGuess()
