print("Welcome to this WW2 quiz game")

playing = input("Will you like to play? ")

if playing.lower() != "yes":
    quit()

print("Let's play")
score = 0

answer = input("Which countries invaded poland at the onset of ww2? ")
if answer.lower() == "germany and soviet union":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is the name of germany's dictator during ww2? ")
if answer.lower() == "adolf hitler":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Where did the germans suffer their first major defeat? ")
if answer.lower() == "stalingrad":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Which country first made use of a nuclear weapon? ")
if answer.lower() == "america":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Which country attacked pearl habour? ")
if answer.lower() == "empire of japan":
    print("Correct!")
else:
    print("Incorrect!")

print("you got " + str(score) + " correct")
print("you got " + str((score / 4) * 100) + " correct")