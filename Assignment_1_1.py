intList_1 = []
intList_2 = []

for i in range(3):
    intListItem = input("Input for List 1 : ")    
    intList_1.append(int(intListItem))    

for j in range(3):
    intListItem = input("Input for List 2 : ")
    intList_2.append(int(intListItem))

for i in range(3):    
    intList_1[i]=intList_1[i]+intList_2[i]

print(intList_1)