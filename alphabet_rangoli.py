import string
def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase
    l = []

    for i in range(0,size):
        s ="-".join(alphabet[i:size])
        l.append(s[::-1]+s[1:])

    for i in l[::-1] :
        print (i.center(4*n -3,"-"))
    
    for i in l[1:] :
        print (i.center(4*n -3,"-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)