def getPenalty():
    penalty={
    "A":[2, -2,  0,  0, -3,  1, -1, -1, -1, -2, -1,  0,  1,  0, -2,  1,  1,  0, -6, -3],
    "C":[-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4,  0, -2, -2, -8,  0],
    "D":[0, -5,  4,  3, -6,  1,  1, -2,  0, -4, -3,  2, -1,  2, -1,  0,  0, -2, -7, -4],
    "E":[ 0, -5,  3,  4, -5,  0,  1, -2,  0, -3, -2,  1, -1,  2, -1,  0,  0, -2, -7, -4],
    "F":[-3, -4, -6, -5,  9, -5, -2,  1, -5,  2,  0, -3, -5, -5, -4, -3, -3, -1,  0,  7],
    "G":[1, -3,  1,  0, -5,  5, -2, -3, -2, -4, -3,  0,  0, -1, -3,  1,  0, -1, -7, -5],
    "H":[-1, -3,  1,  1, -2, -2,  6, -2,  0, -2, -2,  2,  0,  3,  2, -1, -1, -2, -3,  0],
    "I":[-1, -2, -2, -2,  1, -3, -2,  5, -2,  2,  2, -2, -2, -2, -2, -1,  0,  4, -5, -1],
    "K":[-1, -5,  0,  0, -5, -2,  0, -2,  5, -3,  0,  1, -1,  1,  3,  0,  0, -2, -3, -4],
    "L":[-2, -6, -4, -3,  2, -4, -2,  2, -3,  6,  4, -3, -3, -2, -3, -3, -2,  2, -2, -1],
    "M":[-1, -5, -3, -2,  0, -3, -2,  2,  0,  4,  6, -2, -2, -1,  0, -2, -1,  2, -4, -2],
    "N":[0, -4,  2,  1, -3,  0,  2, -2,  1, -3, -2,  2,  0,  1,  0,  1,  0, -2, -4, -2],
    "P":[1, -3, -1, -1, -5,  0,  0, -2, -1, -3, -2,  0,  6,  0,  0,  1,  0, -1, -6, -5],
    "Q":[0, -5,  2,  2, -5, -1,  3, -2,  1, -2, -1,  1,  0,  4,  1, -1, -1, -2, -5, -4],
    "R":[-2, -4, -1, -1, -4, -3,  2, -2,  3, -3,  0,  0,  0,  1,  6,  0, -1, -2,  2, -4],
    "S":[1,  0,  0,  0, -3,  1, -1, -1,  0, -3, -2,  1,  1, -1,  0,  2,  1, -1, -2, -3],
    "T":[1, -2,  0,  0, -3,  0, -1,  0,  0, -2, -1,  0,  0, -1, -1,  1,  3,  0, -5, -3],
    "V":[0, -2, -2, -2, -1, -1, -2,  4, -2,  2,  2, -2, -1, -2, -2, -1,  0,  4, -6, -2],
    "W":[-6, -8, -7, -7,  0, -7, -3, -5, -3, -2, -4, -4, -6, -5,  2, -2, -5, -6, 17,  0],
    "Y":[-3,  0, -4, -4,  7, -5,  0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2,  0, 10]
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

def movesToStrings(first, second, moves, taxiPosition):
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
        elif move=="taxi":
            pointer_w1+=taxiPosition[0]
            pointer_w2+=taxiPosition[1]
    
    return "".join(w1), "".join(w2)

def constructMoves(backtrack, n, m):
    taxiPosition=(1,1)
    moves=[]

    while n>0 or m>0:
        moves.append(backtrack[n][m])
        if backtrack[n][m]=="down":
            n=n-1
        elif backtrack[n][m]=="right":
            m=m-1
        elif backtrack[n][m]=="diag":
            n=n-1
            m=m-1
        elif backtrack[n][m]=="taxi":
            taxiPosition=(n,m)
            n=0
            m=0

    return moves[::-1], taxiPosition

def NullMatrix(n, m):
    return [[0]*(m+1) for i in range(n+1)]

def globalAlignment(first, second):
    s=NullMatrix(len(first), len(second))
    backtrack=[[""]*(len(second)+1) for i in range(len(first)+1)]

    for i in range(1,len(first)+1):
        s[i][0]=max(0, s[i-1][0]-5)
    for j in range(1,len(second)+1):
        s[0][j]=max(0, s[0][j-1]-5)

    for i in range(1,len(first)+1):
        if s[i][0]==0:
            backtrack[i][0]="taxi"
        else:
            backtrack[i][0]="down"
    for j in range(1,len(second)+1):
        if s[0][j]==0:
            backtrack[0][j]="taxi"
        else:
            backtrack[0][j]="right"

    penalty=getPenalty()
    index=getIndexOfLetter()
    for i in range(1, len(first)+1):
        for j in range(1, len(second)+1):
            s[i][j]=max(0, s[i-1][j]-5, s[i][j-1]-5, s[i-1][j-1]+penalty[first[i-1]][index[second[j-1]]])

            if s[i][j]==0:
                backtrack[i][j]="taxi"
            else:
                if (s[i][j]==s[i-1][j]-5):
                    backtrack[i][j]="down"
                elif (s[i][j]==s[i][j-1]-5):
                    backtrack[i][j]="right"
                else:
                    backtrack[i][j]="diag"

    rowMax=[0]*len(s)
    rowMaxIndex=[0]*len(s)
    for i in range(len(s)):
        rowMax[i]=max(s[i])
        rowMaxIndex[i]=s[i].index(rowMax[i])
    
    n=rowMax.index(max(rowMax))
    m=rowMaxIndex[n]
    
    return s[n][m], movesToStrings(first, second, constructMoves(backtrack, n, m)[0], constructMoves(backtrack, n, m)[1])


### ispis

sample_='''MEANLY
PENALTY'''
sample=sample_.splitlines()

first=sample[0]
second=sample[1]

res=globalAlignment(first, second)
print(res[0])
print(res[1][0])
print(res[1][1])
