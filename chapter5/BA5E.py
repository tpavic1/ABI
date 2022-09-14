def getPenalty():
    penalty={
    "A":[4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
    "C":[0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    "D":[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
    "E":[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
    "F":[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
    "G":[0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
    "H":[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
    "I":[-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
    "K":[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
    "L":[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
    "M":[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
    "N":[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
    "P":[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
    "Q":[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
    "R":[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
    "S":[1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
    "T":[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
    "V":[0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
    "W":[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
    "Y":[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
    }
    return penalty

def getIndexOfLetter():
    index={
    "A":0,
    "C":1,
    "D":2,
    "E":3,
    "F":4,
    "G":5,
    "H":6,
    "I":7,
    "K":8,
    "L":9,
    "M":10,
    "N":11,
    "P":12,
    "Q":13,
    "R":14,
    "S":15,
    "T":16,
    "V":17,
    "W":18,
    "Y":19
    }
    return index

def movesToStrings(first, second, moves):
    pointer_w1=0
    pointer_w2=0

    w1=[]
    w2=[]

    for move in moves:
        if move=="down":
            w1.append(first[pointer_w1])
            pointer_w1+=1
            w2.append("-")
        elif move=="right":
            w2.append(second[pointer_w2])
            pointer_w2+=1
            w1.append("-")
        elif move=="diag":
            w1.append(first[pointer_w1])
            pointer_w1+=1
            w2.append(second[pointer_w2])
            pointer_w2+=1
    
    return "".join(w1), "".join(w2)

def constructMoves(backtrack):
    n=len(backtrack)-1
    m=len(backtrack[0])-1
    moves=[]

    while n>0 or m>0:
        moves.append(backtrack[n][m])
        if backtrack[n][m]=="down":
            n=n-1
        elif backtrack[n][m]=="right":
            m=m-1
        else:
            n=n-1
            m=m-1

    return moves[::-1]

def NullMatrix(n, m):
    return [[0]*(m+1) for i in range(n+1)]

def globalAlignment(first, second):
    s=NullMatrix(len(first), len(second))
    backtrack=[[""]*(len(second)+1) for i in range(len(first)+1)]

    for i in range(1,len(first)+1):
        s[i][0]=s[i-1][0]-5
    for j in range(1,len(second)+1):
        s[0][j]=s[0][j-1]-5

    for i in range(1,len(first)+1):
        backtrack[i][0]="down"
    for j in range(1,len(second)+1):
        backtrack[0][j]="right"

    penalty=getPenalty()
    index=getIndexOfLetter()
    for i in range(1, len(first)+1):
        for j in range(1, len(second)+1):
            s[i][j]=max(s[i-1][j]-5, s[i][j-1]-5, s[i-1][j-1]+penalty[first[i-1]][index[second[j-1]]])

            if (s[i][j]==s[i-1][j]-5):
                backtrack[i][j]="down"
            elif (s[i][j]==s[i][j-1]-5):
                backtrack[i][j]="right"
            else:
                backtrack[i][j]="diag"
    
    return s[len(first)][len(second)], movesToStrings(first, second, constructMoves(backtrack))


### ispis

sample_='''PLEASANTLY
MEANLY'''
sample=sample_.splitlines()

first=sample[0]
second=sample[1]

res=globalAlignment(first, second)
print(res[0])
print(res[1][0])
print(res[1][1])
