def IndexOf(permutation, num):
    if(num in permutation):
        return permutation.index(num)
    else:
        return permutation.index(-num)

def MapToString(P):
    mapped=[]
    for p in P:
        if p<0:
            mapped.append(str(p))
        else:
            mapped.append("+"+str(p))
    return mapped

def GreedySorting(P):
    reversal=[]

    for k in range(len(P)):
        if P[k]!=(k+1):
            index=IndexOf(P, k+1)
            P=P[:k]+[-p for p in P[k:index+1][::-1]]+P[index+1:]
            reversal.append(MapToString(P))
            if P[k]==(-(k+1)):
                P[k]=k+1
                reversal.append(MapToString(P))
        
    return reversal


### ispis

sample=''''''
P=list(map(int,sample[1:-1].split(" ")))
res=GreedySorting(P)

for r in res:
    print("("+" ".join(r)+")")
