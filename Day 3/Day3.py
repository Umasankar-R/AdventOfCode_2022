import string
import os
f = open(os.path.join(os.path.dirname(__file__), 'day3.txt'), 'r')
test = f.read().splitlines()

score = []
count = 0
testdata = test
print("Tesdata length: "+str(len(testdata)))

LowerCaseDictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
UpperCaseDictionary = dict(zip(string.ascii_uppercase, range(27, 53)))

UpperCaseDictionary.update(LowerCaseDictionary)
# print(UpperCaseDictionary)

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
