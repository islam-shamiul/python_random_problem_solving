if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    for c in s:
        if not isalnum:
            if c.isalnum():
                isalnum = True
                print("True")
        if not isalpha:
            if c.isalpha():
                isalpha = True
                print("True")
        if not isdigit:
            if c.isdigit():
                isdigit = True
                print("True")
        if not islower:
            if c.islower():
                islower = True
                print("True")
        if not isupper:   
            if c.isupper():
                isupper = True
                print("True")
        
