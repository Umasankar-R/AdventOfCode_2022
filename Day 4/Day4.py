import os
# Read the file containing Test data
f = open(os.path.join(os.path.dirname(__file__), 'day4.txt'), 'r')
test = f.read().splitlines()
# Initialize variables
testdata = test
score = []
scoreRound2 = []
scorecount = 0

# Iterate testdata for each Elves pair present
for assignment in testdata:
    # Round 1:
    # Get the First pair Elves and their sectionID range
    # Check if SectionID range of 1st elves completely present in 2nd elves range
    # Store value as True if Present, Else check vice versa and do the same
    # If range1 and range2 are completely Different, store value as False
    temp = assignment.split(",")
    assignment1 = temp[0].split("-")
    assignment2 = temp[1].split("-")
    asssignment1_range = [*range(int(assignment1[0]), int(assignment1[1])+1)]
    asssignment2_range = [*range(int(assignment2[0]), int(assignment2[1])+1)]
    if set(asssignment2_range).issubset(asssignment1_range):
        score.append(True)
    elif set(asssignment1_range).issubset(asssignment2_range):
        score.append(True)
    else:
        score.append(False)
    # Round 2:
    # Check if any of the 1st Elves SectionID is present in 2nd Elves range
    # Store the value as True if present, else check vice versa and do the same
    # If range1 and range2 are completely Different, store value as False
    if any(item in asssignment1_range for item in asssignment2_range):
        scoreRound2.append(True)
    elif any(item in asssignment2_range for item in asssignment1_range):
        scoreRound2.append(True)
    else:
        scoreRound2.append(False)
    asssignment1_range.clear()
    asssignment2_range.clear()
    temp.clear()

for i in score:
    if i == True:
        scorecount += 1
print("Round 1 : "+str(scorecount))
scorecount = 0
for i in scoreRound2:
    if i == True:
        scorecount += 1
print("Round 2 : "+str(scorecount))
