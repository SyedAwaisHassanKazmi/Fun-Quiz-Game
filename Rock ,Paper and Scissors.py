import random

#random.randint() gives random numbers between the range 0 and 2
#random.randrange() can also be used but it excludes the end values and include the values between them
randomsign = random.randint(0,2)

#list is similar to array in python

checklist = ["rock","paper","scissors"];


userresult = 0;
computerresult = 0;
loopbreak = 0;



while True: 
    randomInputs = random.randint(0,2);
    print("Enter Rock, Paper or Scissors only or press Q to quit: ")
    userInput = input().lower();
    if userInput not in checklist :
        if userInput == "q":
            break
        continue
    
#if user enters rock which is 1 and computer enters scissors which is 2 and so on....
    if (userInput == "rock" and checklist[randomInputs] == "scissors") or  (userInput == "paper" and checklist[randomInputs] == "rock")or (userInput == "scissors" and checklist[randomInputs] == "paper"):
        print("Computer gives "+checklist[randomInputs])
        print("You won!");
        userresult += 1;
        
#if user enters rock which is 0 and computer enters paper which is 1 and so on....
    elif (userInput == "rock" and checklist[randomInputs] == "paper")or(userInput == "paper" and checklist[randomInputs] == "scissors")or(userInput == "scissors" and checklist[randomInputs] == "rock"):
        print("Computer gives "+checklist[randomInputs])
        print("Computer wins!");
        computerresult += 1;
    elif userInput == checklist[randomInputs]:
        print("Computer gives "+checklist[randomInputs])
        print("The game is a tie!")

    
print("The computer has  won " + str(computerresult) +" times.");
print("The user has won " + str(userresult)+" times.")
    
    
if(computerresult > userresult ):
    print("The computer has won the entire Game.")
elif (computerresult < userresult):
    print("The user has won the entire Game.")
else:
    print("The Overall Game is a tie.")

