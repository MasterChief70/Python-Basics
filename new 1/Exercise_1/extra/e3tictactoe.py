import random
l1=['_','_','_','_','_','_','_','_','_']
t=1

z=input("Enter Who Wants to Start ->").lower()
while t<10:
    if t%2==0:
        a=int(input("Enter Player 2 =>>"))
        if l1[a-1] =='_':
            l1[a-1]='X'
        else:
            print("Error")
            t=t-1
    elif t%2!=0:
        b=int(input("Enter Player 1 =>>"))
        if l1[b-1]=='_':
            l1[b-1]='O'
        else:
            print("Error")
            t=t-1
    print("After",t,"Turn")
    print(l1[0],l1[1],l1[2])
    print(l1[3],l1[4],l1[5])
    print(l1[6],l1[7],l1[8])
    if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='X':
        print("Player 2 Wins")
        t=15
    elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='X':
        print("Player 2 Wins")
        t = 15
    elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='X':
        print("Player 2 Wins")
        t = 15
    if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='O':
        print("Player 1 Wins")
        t = 150
    elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='O':
        print("Player 1 Wins")
        t = 150

    t=t+1

if t==10:
    print("**********  MATCH DRAW  **********")
elif t==15:
    print("**********  PLAYER 2 WINS  **********")
else:
    print("**********  PLAYER 1 WINS  **********")
