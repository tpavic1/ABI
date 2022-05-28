def Breakpoints(P):

    produzeni_P=[0]+P+[len(P)+1]
    count=0

    for i in range(len(P)+1):
        if(produzeni_P[i+1]!=produzeni_P[i]+1):
            count+=1

    return count
  
### ispis

sample=""
P=list(map(int,sample[1:-1].split(" ")))

print(Breakpoints(P))
