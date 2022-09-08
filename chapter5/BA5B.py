def NullMatrix(n, m):
    return [[0]*(m+1) for i in range(n+1)]

def ManhattanTourist(n, m, Down, Right):
    s=NullMatrix(n,m)

    for i in range(1,n+1):
        s[i][0]=s[i-1][0]+Down[i-1][0]

    for j in range(1,m+1):
        s[0][j]=s[0][j-1]+right[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j]=max([s[i-1][j]+Down[i-1][j], s[i][j-1]+Right[i][j-1]])

    return s[n][m]

### ispis

sample_=''''''
sample=sample_.splitlines()
n, m=list(map(int,sample[0].split(" ")))
down=[]
right=[]

for i in range(1,n+1):
    down.append(list(map(int,sample[i].split(" "))))
for i in range(n+2,n+2+n+1):
    right.append(list(map(int,sample[i].split(" "))))

print(ManhattanTourist(n, m, down, right))
