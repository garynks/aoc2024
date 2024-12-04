l1 = []
l2 = []

with open('1.txt', 'r') as file:
    for line in file:
        locationIDs = line.split()
        l1.append(int(locationIDs[0]))
        l2.append(int(locationIDs[1]))
    
l1.sort()
l2.sort()

totalDistance = 0
for i in range(len(l1)):
    totalDistance += abs(l1[i] - l2[i])

print(totalDistance)
