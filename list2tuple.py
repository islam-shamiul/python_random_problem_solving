if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupleHash = tuple(integer_list)
    print(hash(tupleHash))