f = open("input.txt", "r")
data = f.read()
items = data.split("\n")
print(items[0])
items = items[:-1]
print(len(items))
print(items[1999])
count = 0

# Test Case 1
# for x in range(len(items)-2):
#     if float(items[x]) < float(items[x+1]):
#         count += 1

count = 0
remainder = len(items) % 3
print(remainder)
windowRange = len(items) // 3
print(windowRange)
for x in range(len(items) - 2 - 1):
    if float(items[x]) + float(items[x+1]) + float(items[x+2]) < float(items[x+1]) + float(items[x+2]) + float(items[x+3]):
        count += 1
print(count)