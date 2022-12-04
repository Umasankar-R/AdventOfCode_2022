import os
# Read test data
f = open(os.path.join(os.path.dirname(__file__), 'day2.txt'), 'r')
test = f.read().splitlines()

score = []
count = 0
testdata = test
# Opponent Option: Rock, Paper, Scissors
A, B, C = 1, 2, 3
# Player Option: Rock, Paper, Scissors
x, y, z = 1, 2, 3
# Points for Winning/drawing/Losing the match
win, draw, loss = 6, 3, 0
# Player Choice for Losing, drawing or Winning the Match for Round 2
X = loss
Y = draw
Z = win

# Round 1:
# Iterrate testdata values
# Split the current testdata value into a list of [Opponents_play, Players_play]
# Assign Count value based on Match result of Player: draw, win, or lose + Players_play for all 9 possibilities
# Reset Count value
for i in testdata:
    temp = i.split()
    opponent = temp[0]
    player = temp[1]
    if opponent == "A" and player == "X":
        count = x+draw
    elif opponent == 'B' and player == 'Y':
        count = y+draw
    elif opponent == "C" and player == "Z":
        count = z+draw
    if opponent == "A" and player == "Y":
        count = y+win
    if opponent == "C" and player == "X":
        count = x+win
    if opponent == "B" and player == "Z":
        count = z+win
    if opponent == "A" and player == "Z":
        count = z+loss
    if opponent == "C" and player == "Y":
        count = y+loss
    if opponent == "B" and player == "X":
        count = x+loss
    score.append(count)
    count = 0
print("Round 1: "+str(sum(score)))
score.clear()

# Round 2:
# Split the current testdata value into a list of [Opponent_play, Player_choice]
# Assign Count value based on the Choice of Player to draw(Y), lose(X) or win(Z) + Players_play for all 9 possibilities
# Reset Count value
for i in testdata:
    temp = i.split()
    opponent = temp[0]
    player = temp[1]
    if opponent == "A" and player == "Y":
        count = Y+x
    if opponent == "B" and player == "Y":
        count = Y+y
    if opponent == "C" and player == "Y":
        count = Y+z

    if opponent == "A" and player == "X":
        count = X+z
    if opponent == "B" and player == "X":
        count = X+x
    if opponent == "C" and player == "X":
        count = X+y

    if opponent == "A" and player == "Z":
        count = Z+y
    if opponent == "B" and player == "Z":
        count = Z+z
    if opponent == "C" and player == "Z":
        count = Z+x
    score.append(count)
    count = 0
print("Round 2: "+str(sum(score)))
