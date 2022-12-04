import os
# Read test data
f = open(os.path.join(os.path.dirname(__file__), 'day1.txt'), 'r')
testdata = f.read().splitlines()
Count = 0
SumArray = []

# Iterate testdata
# Check if testdata value is empty or not
# Count = Count + current value if testdata value is not empty
# If testdata value is empty store the current count value in a list and reset count value and continue next iteration
for i in range(0, len(testdata)):
    if testdata[i] != "":
        Count = Count+int(testdata[i])
    else:
        SumArray.append(Count)
        Count = 0
SumArray.append(Count)

# Sort Array in Descending order to find largest Number
SumArray.sort(reverse=True)
print("Total Max Calories :" + str(SumArray[0]))

TopThreeCaloriesSum = SumArray[0]+SumArray[1]+SumArray[2]
print("Top Three Calories Sum : " + str(TopThreeCaloriesSum))
