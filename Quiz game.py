print("Welcome to a little game of mine... ready to play?")
print("*Type yes or no only.")

inputpermission = input()
if inputpermission.lower() != "yes":
    quit()

marks = 10;

print("*Game Rules*")
print("*In this game, a series of 4 questions will be asked.")
print("*Each question carries 2.5 mark.")
print("*Incorrect answers will receive no marks.")
print("*Answer in Yes or No only.")
print("*The results will be shared at the end.")
print("The game is starting....")

print("1) Have you had a girlfriend before?")
firstquestion = 0;
while True:
    firstquestion = input();

    if firstquestion.lower() == "yes" or firstquestion.lower() == "no":
        break;
    print("Enter Yes or no only please:")
    

if firstquestion.lower() == "yes":
    print("2) Did she dump you?")
    while True:
        firstquestion = input();
        if firstquestion.lower() == "yes" or firstquestion.lower() == "no":
            break;
        print("Enter Yes or no only please:")

    if firstquestion.lower() == "yes" or "no":
        print("I feel sorry for you, brother :(")
    if firstquestion == "no":
        marks-= 2.5;
elif firstquestion.lower() == "no":
    print("2) Is she beautiful?")
    
    while True:
        firstquestion = input();
        if firstquestion.lower() == "yes" or firstquestion.lower() == "no":
            break;
        print("Enter Yes or no only please:")

    if firstquestion.lower() == "yes":
        print("Good for you!")
    elif firstquestion.lower() == "no":
        print("Shame on you then!")
        marks -= 2.5;

    

print("3) Have you ever called yourself handsome and believed it?")

while True:
        thirdquestion = input();
        if thirdquestion.lower() == "yes" or thirdquestion.lower() == "no":
            break;
        print("Enter Yes or no only please:")
if thirdquestion.lower() == "yes":
    print("Really?")
    marks-= 2.5;
elif thirdquestion.lower() == "no":
    print("Good!")

print("""4) Have you ever smiled back at someone only to realize they weren't looking at you?""")
while True:
        fourthQuestion = input();
        if fourthQuestion.lower() == "yes" or fourthQuestion.lower() == "no":
            break;
        print("Enter Yes or no only please:")

if fourthQuestion.lower() == "yes" or "no":
    print("Too bad for you; you should have looked behind!")
    if fourthQuestion.lower() == "no":
        marks-= 2.5;


print("You have received " + str(marks) + " scores.")
