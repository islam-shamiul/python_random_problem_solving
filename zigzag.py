import sys, time



def zigZag():
    indent = 0
    indentTrue = True
    while True:
        print(' '*indent,end='')
        print("********")
        time.sleep(.1)

        if indentTrue:
            indent = indent+1
            
            if indent == 20 :
                indentTrue = False

        else:
            indent = indent-1

            if indent == 0 :
                indentTrue =True
try:
    zigZag()

except:
    sys.exit()

