listNoReverse = [1,2,3,4,5]
listToReverse = []

for i in range(0,len(listNoReverse)):
    listToReverse.append(listNoReverse[len(listNoReverse)-(i+1)])

print(listToReverse)