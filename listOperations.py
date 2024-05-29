if __name__ == '__main__':
    N = int(input())
    List = []
    def listInsert(i,v):
        List[i]=v
    
    def listRemove (value):
        i = List.index(value)
        del List[i]
    
    def listAppend (value):
        List += value

    for n in N:
        inp = input()
        splitInput = inp.split()

        if splitInput[0] == "insert":
            listInsert (splitInput[1],splitInput[2])
        
        elif splitInput[0]== "remove":
            listRemove(splitInput[1])

        elif splitInput[0] == "append":
            listAppend(splitInput[1])
        
        elif splitInput[0] == "sort":
            list.sort()

        elif splitInput[0] == "print":
            print(list)

        elif splitInput[0] == "pop":
            list.pop(len(list))

        elif splitInput[0] == "reverse":
            list.reverse()