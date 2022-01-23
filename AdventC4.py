from Utility import Read
from Utility import ToInt

def CheckCard(dataA):
    result = 0
    status = False
    for dat in dataA:
        result += dat
    if result == 0:
        status = True
    return status


def WinningCard(wCard, number):
    finalScore = 0
    for num1 in wCard:
        finalScore += num1
    finalScore = finalScore * number
    print("Winning Score Is: ")
    print(finalScore)
    return finalScore



data = Read("input4.txt", "\n\n")
finalList = []
numSelect = data[0]
numSelect = data[0].split(",")
numSelect = ToInt(numSelect)
bingo = False
score = 0
location = []

cleanLast = data[-1].split("\n")
cleaned = cleanLast[0] + "\n" + cleanLast[1] + "\n" + cleanLast[2] + "\n" + cleanLast[3] + "\n" + cleanLast[4]
data[-1] = cleaned

data.pop(0)

for idx, dat in enumerate(data):
    dat = dat.replace("\n"," ")
    dat = dat.replace("  ", " ")
    
    data[idx] = dat

for dat in data:
    dat = dat.split(" ")
    finalList.append(ToInt(dat))

print(finalList[34][0:5])

copyList = finalList


for num in numSelect:
    for x, card in enumerate(copyList):
        for y, cell in enumerate(card):
            if cell == num:
                copyList[x][y] = 0
        # check the card
        bingo = CheckCard(card[0:5])
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(0)
            break
            
        bingo = CheckCard(card[6:10])
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(1)
            break
            
        bingo = CheckCard(card[11:15])
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(2)
            break
            
        bingo = CheckCard(card[16:20])
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(3)
            break
            
        bingo = CheckCard(card[21:25])
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(4)
            break
            
        bingo = CheckCard(list(card[i] for i in [0,5,10,15,20]))
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(5)
            break
            
        bingo = CheckCard(list(card[i] for i in [1,6,11,16,21]))
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(6)
            break
            
        bingo = CheckCard(list(card[i] for i in [2,7,12,17,22]))
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(7)
            break
            
        bingo = CheckCard(list(card[i] for i in [3,8,13,18,23]))
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(8)
            break
            
        bingo = CheckCard(list(card[i] for i in [4,9,14,19,24]))
        if bingo == True:
            score = WinningCard(card, num)
            location.append(x)
            location.append(9)
            break             
    if bingo == True:
        break







# for x, card in enumerate(copyList):
#         for y, cell in enumerate(card):
#             if cell == numSelect[0]:
#                 print(cell)
#                 print(copyList[x][y])

# print("The number to select is: ")
# print(numSelect[0])

