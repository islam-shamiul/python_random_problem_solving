import math
import os
import random
import re
import sys

def solve(s):
    m=s.split(" ")
    for i in range(0,len(m)):
        m[i] = m[i].capitalize()                    
    str_ = " ".join(m)
    print(str_)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = "let test"

    result = solve(s)

    #fptr.write(result + '\n')

    #fptr.close()
