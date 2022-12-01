listCountry = ['Bangladesh',"Australia","Canada"]

inputIndexItem = input("Item for index : ")

newValue = input("New value  : ")

listCountry.insert((listCountry.index(inputIndexItem))+1,newValue)

print(listCountry)