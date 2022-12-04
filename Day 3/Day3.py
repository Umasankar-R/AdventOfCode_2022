import string
import os
# Read test data
f = open(os.path.join(os.path.dirname(__file__), 'day3.txt'), 'r')
test = f.read().splitlines()

score = []
count = 0
testdata = test
print("Tesdata length: "+str(len(testdata)))

# Create two dictionaries
# Dictionary 1 with Keys as lowercase alphabets and values ranging from 1 to 26
# Dictionary 2 with Keys as uppercase alphabets and values ranging from 27 to 52
LowerCaseDictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
UpperCaseDictionary = dict(zip(string.ascii_uppercase, range(27, 53)))

# Merge uppercase and lowercase dictionaries into a single dictionary
UpperCaseDictionary.update(LowerCaseDictionary)

# Iterate testdata
# Split the first testdata value into two halves
# Iterate first and second halves string char's and check if both contains any one char in common
# If common string is present assign the char's value to count from dictionary
# Reset count value
for _ in testdata:
    res_first = _[0:len(_)//2]
    res_second = _[len(_)//2 if len(_) % 2 == 0
                   else ((len(_)//2)+1):]
    for __ in res_first:
        for ___ in res_second:
            if __ == ___:
                count = UpperCaseDictionary[__]
    score.append(count)
    count = 0
print("Round1 : "+str(sum(score)))

score.clear()

# Assign and initialize index variable temp_i
# Iterate testdata for n number of times where n is length of testdata/3 as each iteration takes 3 values from testdata
# InEach iteration next get three strings from testdata using index variable and store them in temporary list
# Iterate Char's of all three strings stored in temporary list and check if any char's is common in all three strings
# If common char is present assign the value of the char to count from dictionary
# Reset the count
# Increment the the index value insteps of three
temp_i = 0
for i in range(0, int((len(testdata)/3))):
    temp = [testdata[temp_i], testdata[temp_i+1], testdata[temp_i+2]]
    for j in temp[0]:
        for k in temp[1]:
            for l in temp[2]:
                if j == k and k == l:
                    __ = j
                    count = UpperCaseDictionary[__]
    score.append(count)
    count = 0
    temp_i = temp_i+3

print("Round2 : "+str(sum(score)))
