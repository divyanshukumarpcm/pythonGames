#Author = Divyanshu Kumar
#Tiime - 07-09-2020 9:48 AM
import random
print ("Welcome, You will need to guess the number [0,100] randomised by the computer and based \n on number of attempts \n You will be scored!")
rand = random.randint(0,100)
userguess=int(input("Guess the number..."))
score=100
while userguess!=rand:
    score=score-1
    print("Wrong guess! Try again...Score: ",score)
    if userguess<rand:
        print("Guess higher: ")
    else:
        print("Guess lower")
    userguess=int(input())
print("Correct! Your Score: ",score)

    
