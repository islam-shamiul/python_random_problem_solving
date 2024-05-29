catNames = []

while True:
    print("Enter The name of cat " + str(len(catNames)+1)  + "(Or enter nothing to stop.)")

    name = input()

    if name == ' ':
        break
    catNames = catNames + [name]

print("The cat names are:")   

for names in catNames:
    print(" " + names)