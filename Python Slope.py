levelCount = 0
lastCalculatedSlope = 0
isLastSlope = False
lastCalculatedLevel = 0
isLastLevel = False

def getLevelDifference(levelOne, levelTwo):
    levelDifference = 0
    if(levelOne > levelTwo):
        levelDifference = levelOne - levelTwo
    else:
        levelDifference = levelTwo - levelOne
    return levelDifference

def getDistance():
    print("Enter the distance between the points in meters")
    while(True):
       try:
            distance = float(input())
            break
       except ValueError:
            print("Please enter a numeric value")
    return distance

def getLevels():
     global levelCount
     levelCount += 1
     level = None
     print("Enter level",levelCount)
     while(True):
        try:
            level = float(input())
            break
        except ValueError:
            print("Please enter a numeric value")
     return level
        

def slopeCalc(): #need to sort out executio flow of this function
    global levelCount
    global lastCalculatedSlope
    global isLastSlope
    global isLastLevel
    global lastCalculatedLevel
    global levelCount
    levelOne = 0
    distance = 0
    levelDifference = 0
    if(isLastLevel == True):
        print("Enter Y to use previously calculated level as the starting point or N for no")
        userInput = input()
        if(userInput == "Y" or userInput == "y"):
            levelOne = lastCalculatedLevel
            print("Level 1", levelOne)
            levelCount += 1
            levelTwo = getLevels()
            levelCount = 0
            distance = getDistance()
            levelDifference = getLevelDifference(levelOne, levelTwo)
        else:
            levelOne = getLevels()
            levelTwo = getLevels()
            levelCount = 0
            distance = getDistance()
            levelDifference = getLevelDifference(levelOne, levelTwo)
    else:
        levelOne = getLevels()
        levelTwo = getLevels()
        levelCount = 0
        distance = getDistance()
        levelDifference = round(getLevelDifference(levelOne, levelTwo),3)
    try:
        slope = round(distance / levelDifference, 0)
        print("That slope is 1:" + str(int(slope)))
        percentage = round(((1/slope)*100), 3)
        print("As a percentage is " + str(percentage) + " %")
        print()
        isLastSlope = True
        lastCalculatedSlope = slope #stores last value into here incase we want to reuse it in the future
    except ZeroDivisionError:
        print("No gradient between these points, cannot divide by 0")

def getSlope():
    global isLastSlope
    global lastCalculatedSlope
    if(isLastSlope == True):
        while(True):
            print("Enter P to use previously calculated slope or enter the slope you want to use")
            print("1:", end="")
            userInput = input()
            if(userInput == "P" or userInput == "p"):
                return round(lastCalculatedSlope,0)
            else:
                try:
                    return int(userInput)
                except ValueError:
                    print(end="")
                
    else:
         print("Enter the slope you want to use")
         print("1:", end="")
         userInput = int(input())
         return userInput

def getDirection():
    userInput = None
    while(True):
        print("Enter + for an uphill gradient, Enter - for a downhill gradient")
        userInput = input()
        if(userInput == '+' or userInput == '-'):
            break
    return userInput
         
def newLevel():
    global levelCount
    global lastCalculatedLevel
    global isLastLevel
    startLevel = getLevels()
    slope = getSlope()
    distance = getDistance()
    direction = getDirection()
    returnLevel = 0
    if(direction == '+'):
        returnLevel = round(startLevel + (distance/slope),3)
        print("New Level:",returnLevel)
    else:
        returnLevel = round(startLevel - (distance/slope), 3)
        print("New Level:", returnLevel)
    levelCount = 0
    isLastLevel = True
    lastCalculatedLevel = returnLevel
    
while(True):
    print("Enter S to calculate a slope or N for a new level. It is X to exit the app")
    userInput = input()
    if(userInput == "S" or userInput == "s"):
        slopeCalc()
    elif(userInput == "N" or userInput == "n"):
        newLevel()
    elif(userInput == "X" or userInput == "x"):
        print("Closing App")
        break
    

