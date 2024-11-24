import random

print("              **Game overview**")
print("*In this game you have to guess a number between 0 to whatever number you want");

tries =0 ;
print("Select the number upto which you want to guess the number: ")
userschoice = input()
#isdigit() is used to check weather the number entered by the user is a digit or not

#Will take input from the user repeatdly until it is a digit
if userschoice.isdigit() != True:
    while True:
        userschoice = input("Enter only numbers please: ")
        if userschoice.isdigit():
            break


randomnumber = random.randint(0,int(userschoice));
randomumber = int(randomnumber);
print(randomnumber);
print("Enter the number you guessed: ");
#retry if number is not the guessed number
while True:
    usersanswer = input();
    #Will take input from the user repeatdly until it is a digit
    if usersanswer.isdigit() != True:
        while True:
            usersanswer = input("Enter only numbers please: ")
            if usersanswer.isdigit():
                break

    if int(usersanswer) == randomnumber:
       print("You have correctly Guessed the number");
       break
    elif int(usersanswer) > randomnumber :
          print("Incorrect Guess try again");
          print("Hint: You are above from the number:")
    elif int(usersanswer) < randomnumber:
        print("Incorrect Guess try again");
        print("Hint: You are below from the number:")
        

    
    tries += 1;
  
    
print("You have guessed the number in " + str(tries) +" tries")


