def Max(data):
	maxVal = data[0]
	for dt in data:
		if maxVal < dt:
			maxValue = dt
	return maxVal

def Min(data):
	minVal = data[0]
	for dt in data:
		if minVal > dt:
			minValue = dt
	return minVal


def Read(filename, splitter):
    file = open( filename, "r")
    data = file.read()
    data = data.split(splitter)
    if data[-1] == []:
        data = data[:-1]
    else:
        print("This is the last element")
        print(data[-1])
        print("Note: It might need some additonal Parsing")
    return data


def ToInt(inputData):
    outputData = []
    temp = []
    # outputData = [int(i) for i in inputData]
    for idx, i in enumerate(inputData):
        if i == "":
            # print(inputData)
            # print(idx)
            wait = 0
        else:
            temp.append(int(i))
    
    outputData = temp
    return outputData
