from Utility import Read
from Utility import ToInt

def CheckCard(dataA):
    result = 0
    status = False
    for dat in dataA:
        result += dat
    if result == -5:
        status = True
    return status

def WinningCard(wCard, number):
    finalScore = 0
    for num1 in wCard:
        if num1 == -1:
            finalScore = finalScore
        else:
            finalScore += num1
    finalScore = finalScore * number
    print(finalScore)

data = Read("input4.txt", "\n\n")
finalList = []
numSelect = data[0]
numSelect = data[0].split(",")
numSelect = ToInt(numSelect)
cardNum = []
bingo = False

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

# print("original Winning Card")
# print(finalList[22])
# original failure is i used the replacement number 0

# original failure number the indexing was incorrect
# print(finalList[99][0:5])
# print(finalList[99][5:10])
# print(finalList[99][10:15])
# print(finalList[99][15:20])
# print(finalList[99][20:25])
for i in range(len(finalList)): cardNum.append(1)

for num in numSelect:
    for x, card in enumerate(finalList):
        for y, cell in enumerate(card):
            if num == cell:
                finalList[x][y] = -1
        #Check Card
        bingo = CheckCard(card[0:5])
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

        bingo = CheckCard(card[5:10])
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

        
        bingo = CheckCard(card[10:15])
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

                        
        bingo = CheckCard(card[15:20])
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

            
        bingo = CheckCard(card[20:25])
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

           
            
        bingo = CheckCard(list(card[i] for i in [0,5,10,15,20]))
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

            
        bingo = CheckCard(list(card[i] for i in [1,6,11,16,21]))
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

            
        bingo = CheckCard(list(card[i] for i in [2,7,12,17,22]))
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

            
        bingo = CheckCard(list(card[i] for i in [3,8,13,18,23]))
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

            
        bingo = CheckCard(list(card[i] for i in [4,9,14,19,24]))
        if bingo == True:
            cardNum[x] = 0
            if sum(cardNum) == 0:
                print("Winning Card: ")
                print(card)
                print(num)
                WinningCard(card, num)
                break

    if sum(cardNum) == 0:
        break


# print("Final Winning Card")
# print(finalList[22])
# print(cardNum)