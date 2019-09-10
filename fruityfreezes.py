# This program is made for the Statistics 201 Simulation Internal
# It uses the random module for python 3.7
# Developed by Bingus Boys (find us on scratch and github)

import random

trialCounter = 0  # Counter for counting the num of trials.
# Number of trials that you want to do.
numOfTrials = int(input("How many trials would you like?\n  "))
outputString = ""  # String here used for outputs.

movieCounter = 0

# i1-10 meaning ice-blocks 1-10
outputString += str("Trial,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,Total,\n")

print("--= Press enter to generate trials =--")
userInput = input('  ')
print("generating...")

while trialCounter < numOfTrials:

    # To write the trial number along the side.
    trialCounter += 1
    outputString += str(trialCounter)+","
    test = True
    total = 0
    counter = 0
    stampList = []

    while counter < 10:
        counter += 1
        percentage = random.randint(1, 100)  # Random integer between 1 and 100
        if test:
            total += 1
            if percentage >= 0 and percentage <= 40:  # Designate
                outputString += "Apple,"
                if "apple" not in stampList:
                    stampList.append("apple")
            elif percentage >= 41 and percentage <= 70:  # Designate
                outputString += "Pineapple,"
                if "pineapple" not in stampList:
                    stampList.append("pineapple")
            elif percentage >= 71 and percentage <= 90:  # Designate
                outputString += "Grape,"
                if "grape" not in stampList:
                    stampList.append("grape")
            elif percentage >= 91 and percentage <= 100:  # Designate
                outputString += "Strawberry,"
                if "strawberry" not in stampList:
                    stampList.append("strawberry")
            if len(stampList) == 4:
                test = False
        else:
            outputString += ","

    outputString += str(total)+"\n"
    if not test:
        movieCounter += 1


# Write the mean at the bottom

outputString += "Mean:,=AVERAGE(L2:L"+str(numOfTrials+1)+")"
outputString += "\nMedian:,=MEDIAN(L2:L"+str(numOfTrials+1)+")"
outputString += "\nMovie Passes:,"+str(movieCounter)

# Inputting the outputString with all of the conversions.
file = open("simulation.txt", "w+")
file.write(outputString)
file.close()

# Reading the lines to make a copy - seems tedious but can't do both in
# previous one.
file = open("simulation.txt", "r")
data = file.readlines()
file.close()

# Makes a new .csv file with the data.
newFile = open("simulation.csv", "w+")
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

# Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's
# not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a
# Dark Lord of the Sith, so powerful and so wise he could use the Force to
# influence the midichlorians to create life… He had such a knowledge ofthedark
# side that he could even keep the ones he cared about from dying. The darkside
# of the Force is a pathway to many abilities some consider to be unnatural. He
# became so powerful… the only thing he was afraid of was losinghis power,which
# eventually, of course, he did. Unfortunately, he taught his apprentice
# everything he knew, then his apprentice killed him in his sleep. Ironic. He
# could save others from death, but not himself.
