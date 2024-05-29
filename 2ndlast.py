if __name__ == '__main__':
    # list of input data
    dataList = []
    # set of all scores
    scores = set()
    # names of students with lowest scores
    lowestName = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # adding input data to a dictionary
        dataList.append([name, score])
        # making set of scores
        scores.add(score)
    # determining the 2nd lowest score
    secondLowest = sorted(scores)[1]
    # exploring our data list
    for name, score in dataList:
        # making a list of names with lowest scores
        if score == secondLowest:
            lowestName.append(name)
    # sorting names and printing them each in a line
    for name in sorted(lowestName):
        print(name, end='\n')