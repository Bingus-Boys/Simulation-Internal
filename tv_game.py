# This program is made for my Stats201 Simulations Internal
# It uses the random module for python 3.7
# Tom Barthelmeh 2019
import random
import time


trialCounter = 0 # Counter for counting the num of trials.
# Number of trials that you want to do.
numOfTrials = int(input("How many trials would you like?\n  "))
outputString = "" # String here used for outputs.
courseCompletion = 0


#A1-10 meaning Attemps 1-10
outputString += str("Trial,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Tries\n")

print("--= Press enter to generate trials =--")
userInput = input('  ')
print("generating...")

while trialCounter < numOfTrials:

    # To write the trial number along the side.
    trialCounter += 1
    outputString += str(trialCounter)+","

    quit = False
    freePass = False
    freePassCounter = 0
    counter = 0
    obstacle = 1
    complete = False
    trials = 0


    while counter < 10:
        counter += 1
        percentage = random.randint(1,100) # Random integer between 1-100
        if not complete and not quit and not freePass:

            if percentage < 30:
                outputString += str(obstacle) + "-Pass,"
                obstacle += 1
                trials += 1
                if obstacle > 5:
                    complete = True

            elif percentage >= 31 and percentage <= 55:
                outputString += str(obstacle) + "-Quit,"
                quit = True

            elif percentage >= 56 and percentage <= 90:
                outputString += str(obstacle) + "-Fail,"
                trials += 1

            elif percentage > 90:
                outputString += str(obstacle) + "-Free,"
                freePass = True
                obstacle += 1
                trials += 1
                if obstacle > 5:
                    complete = True
                    freePass = False
        elif freePass:
            outputString += str(obstacle) + "-Free,"
            obstacle += 1
            freePass = False
            if obstacle > 5:
                complete = True

        elif quit:
            outputString += ","

        elif complete:
            outputString += ","




    #At the end we want to write the total
    if complete:
        courseCompletion += 1
        outputString += str(trials)+"\n"
    else:
        outputString += ",\n"



#Write the mean at the bottom

outputString += "Mean:,=AVERAGE(L2:L"+str(numOfTrials+1)+")"
outputString += "\nMedian:,=MEDIAN(L2:L"+str(numOfTrials+1)+")\n"
outputString += "Complete: , "+str(courseCompletion)


# Inputting the outputString with all of the conversions.
file = open("simulation.txt", "w+")
file.write(outputString)
file.close()

# Reading the lines to make a copy - seems tedious but can't do both in previous one.
file = open("simulation.txt","r")
data = file.readlines()
file.close()

# Makes a new .csv file with the data.
newFile = open("simulation.csv","w+")
for i in data:
    newFile.write(i)
newFile.close()

# Wipes the data from the file so it can be used again.
file = open("simulation.txt", "w")
file.write("")
file.close()

print("\n**Remember to either rename or delete CSV after use.**")
print("Press enter to finish")
finishCheck = input('  ')
