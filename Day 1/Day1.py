import os

f = open(os.path.join(os.path.dirname(__file__), 'day1.txt'), 'r')
testdata = f.read().splitlines()
Count = 0
SumArray =[]

for i in range(0, len(testdata)):
    if testdata[i] != "":
        Count= Count+int(testdata[i])
    else:
        SumArray.append(Count)
        Count=0
SumArray.append(Count)

SumArray.sort(reverse=True)
print("Total Max Calories :"+ str(SumArray[0]))

TopThreeCaloriesSum = SumArray[0]+SumArray[1]+SumArray[2]
print("Top Three Calories Sum : " + str(TopThreeCaloriesSum))