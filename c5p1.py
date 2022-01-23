from Utility import Read

data = Read("input5.txt", "\n")
x1 = []
y1 = []
x2 = []
y2 = []

maxXValue = -1
maxYValue = -1

# print(data[5])
del data[-1] # add this to the Read function to test if the last element is nothing and remove it.


#add the below into a function for spliting
for dat in data:
	temp = dat.split(",")
	x1.append(temp[0])
	y2.append(temp[2])
	temp  = temp[1].split("->")
	temp[0] = temp[0].replace(" ","")
	y1.append(temp[0])
	temp[1] = temp[1].replace(" ","")
	x2.append(temp[1])


index = len(x1)

temp = max(x1)
temp2 = max(x2)
print("Temporary Values")
print(temp)
print(temp2)
maxValueX = temp if temp > temp2 else temp2
print("Max Value X")
print(maxValueX)

temp = min(x1)
temp2 = min(x2)
minValueX = temp if temp < temp2 else temp2
print("Temporary Values")
print(temp)
print(temp2)
print("Min Value X")
print(minValueX)

temp = max(y1)
temp2 = max(y2)
maxValueY = temp if temp > temp2 else temp2


temp = min(y1)
temp2 = min(y2)
minVlaueY = temp if temp < temp2 else temp2
