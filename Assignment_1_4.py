list1 = [5, 20, 15, 20, 25, 50, 20]
print(list1)

removeValue = input("Remove item : ")

removeValue = int(removeValue)

for i in list1:
    if i == removeValue:
        list1.remove(removeValue)

print("List after delete")
print(list1)
