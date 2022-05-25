def k_reversal(P,k):

    if("+"+str(k+1) in P):
        ind2=P.index("+"+str(k+1))
    else:
        ind2=P.index("-"+str(k+1))

    P=P[:k]+[ "+"+s[1:]  if s[0]=="-" else "-"+s[1:] for s in P[k:(ind2+1)] ][::-1]+P[(ind2+1):]

    return P

def GredySearch(P):
    sequence=[]
    for k in range(len(P)):
        if P[k]!=("+"+str(k+1)):
            P=k_reversal(P,k)
            sequence.append(P)

            if(P[k]=="-"+str(k+1)):
                P=P[:k]+["+"+str(k+1)]+P[(k+1):]
                sequence.append(P)

    return sequence
  
  
### ispis

sample=''
P=sample[1:-1].split(" ")

ros=GredySearch(P)
for r in ros:
    text="("+" ".join(r)+")"
    print(text)
