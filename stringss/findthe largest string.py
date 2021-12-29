# Read N string from input and find out the largest string

numofString = int(input())


def largestString(numofString):
    largestStringNumber = 0
    largestString = ''
    while(numofString!=0):
        stringInput = input()
        if len(stringInput) > largestStringNumber:
               largestStringNumber = len(stringInput)
               largestString = stringInput
        numofString -= 1
    print("start",largestString)


largestString(numofString)


    

