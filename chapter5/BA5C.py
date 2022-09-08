def NullMatrix(n, m):
    return [[0]*(m+1) for i in range(n+1)]

def LCSBacktrack(v, w):
    s=NullMatrix(len(v),len(w))
    backtrack=[[""]*len(w) for i in range(len(v))]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            if(v[i-1]==w[j-1]):
                s[i][j]=max([s[i-1][j], s[i][j-1], s[i-1][j-1]+1])
            else:
                s[i][j]=max([s[i-1][j], s[i][j-1]])

            if s[i][j]==s[i-1][j]:
                backtrack[i-1][j-1]="down"
            elif s[i][j]==s[i][j-1]:
                backtrack[i-1][j-1]="right"
            elif (s[i][j]==s[i-1][j-1]+1 and v[i-1]==w[j-1]):
                backtrack[i-1][j-1]="diag"

    return backtrack

def OutputLCS(Backtrack, v, i, j, result):
    if (i==-1 or j==-1):
        print(result[::-1])
        return 

    if Backtrack[i][j]=="down":
        OutputLCS(Backtrack, v, i-1, j, result)
    elif Backtrack[i][j]=="right":
        OutputLCS(Backtrack, v, i, j-1, result)
    else:
        result+=v[i]
        OutputLCS(Backtrack, v, i-1, j-1, result)
        

### ispis
import sys
sys.setrecursionlimit(1500)

sample=''''''
v, w= sample.splitlines()

res = OutputLCS(LCSBacktrack(v, w), v, len(v)-1, len(w)-1, "")
