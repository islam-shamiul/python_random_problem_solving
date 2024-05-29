def split_and_join(line):
    # write your code here
    splitLine = line.split(" ")
    result = "-".join(splitLine)
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)