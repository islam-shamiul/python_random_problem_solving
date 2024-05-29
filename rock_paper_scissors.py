import random, sys

w=0
l=0
t=0

print("ROCK, PAPER, SCISSORS" )
valid_inputs = ['r','p','s','q']


try:
    while True:
        print("%s Wins , %s Lossess, %s Ties" %(w,l,t))
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        while True:
            move = str(input())

            
            while move not in valid_inputs:
                print("Invalid input. Please enter 'r', 's', 'p', or 'q'.")
                break

            if (move == 'p'):
                print("PAPER versus...")
                break
        
            elif(move=='r'):
                print("ROCK versus...")
                break
        
            elif(move == 's'):
                print("SCISSORS versus...")
                break

            elif (move == 'q'):
                sys.exit()

        randomNumber = random.randint(1,3)

        if (randomNumber == 1):
            computerMove = 'r'
            print("Computer choose rock")

        if (randomNumber == 2):
            computerMove = 'p'
            print("Computer choose PAPER")

        if (randomNumber == 3):
            computerMove = 's'
            print("Computer choose SCISSORS")


        if move == computerMove :
            print ("Tie")
            t = t+1
        
        elif move =='r' and computerMove =='s':
            print("you win!")
            w = w+1

        elif move =='p' and computerMove =='r':
            print("you win!")
            w = w+1

        elif move =='s' and computerMove =='p':
            print("you win!")
            w = w+1

        else:
            print("you lose!")
            l=l+1
except:
    print("Quiting the Programe")
    