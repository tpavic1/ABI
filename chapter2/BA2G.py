import random

def ProfileProbability(profile, kmer, k):
    probability=1
    for i in range(k):
        if kmer[i]=="A":
            probability*=profile[0][i]
        elif kmer[i]=="C":
            probability*=profile[1][i]
        elif kmer[i]=="G":
            probability*=profile[2][i]
        else:
            probability*=profile[3][i]
    return probability

def ProfileMostProbableKmer(text, profile, k):
    probability=0
    mostProbableKmer=text[:k]
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        probability_=ProfileProbability(profile, kmer, k)
        if probability_>probability:
            probability=probability_
            mostProbableKmer=kmer
    return mostProbableKmer

# using pseudocount
def Count(motifs):
    rows=4
    cols=len(motifs[0])
    count=[[0]*cols for i in range(rows)]
    for i in range(cols):
        for motif in motifs:
            if(motif[i]=="A"):
                count[0][i]+=1
            elif(motif[i]=="C"):
                count[1][i]+=1
            elif(motif[i]=="G"):
                count[2][i]+=1
            else:
                count[3][i]+=1
    count=[list(map(lambda x: x+1,row)) for row in count]
    return count

def Profile(count, numOfMotifs):
    return [list(map(lambda x: x/(numOfMotifs+4), row)) for row in count]

def Score(count):
    cols=len(count[0])
    score=0
    for j in range(cols):
        col=[count[0][j], count[1][j], count[2][j], count[3][j]]
        maxValue=max(col)
        colScore=sum(col)-maxValue-3
        score+=colScore
    return score

def ProfileRandomlyGeneratedKmer(profile, text, k):
    probs=[]
    for i in range(len(text)-k+1):
        kmer=text[i:(i+k)]
        probs.append(ProfileProbability(profile, kmer, k))
    divisor=sum(probs)
    probs=[p/divisor for p in probs]
    r=random.uniform(0,1)
    s=0
    for j,p in enumerate(probs):
        s+=p
        if(r<s):
            return(text[j:(j+k)])

def GibbsSampleOneIteration(Dna, k, t, N):
    indexes=[random.randint(0,len(Dna[0])-k) for string in Dna]
    motifs=[Dna[i][indexes[i]:(indexes[i]+k)] for i in range(len(Dna))]
    bestMotifs=[motif for motif in motifs]
    for j in range(N):
        i=random.randint(0,t-1)
        count=Count(motifs[:i] + motifs[(i+1):])
        profile=Profile(count,len(Dna)-1)
        motifs[i]=ProfileRandomlyGeneratedKmer(profile, Dna[i], k)
        if Score(Count(motifs))<Score(Count(bestMotifs)):
            bestMotifs=[motif for motif in motifs]
    return bestMotifs

def GibbsSample(Dna, k, t, N):
    bestMotifs=GibbsSampleOneIteration(Dna, k, t, N)
    for i in range(1,20):
        motifs=GibbsSampleOneIteration(Dna, k, t, N)
        if Score(Count(motifs))<Score(Count(bestMotifs)):
            bestMotifs=[motif for motif in motifs]
    return bestMotifs

### ispis

sample_=''''''
sample=sample_.splitlines()
k, t, N = [int(x) for x in sample[0].split(" ")]
Dna=sample[1:]

res=GibbsSample(Dna,k,t,N)
for r in res:
    print(r)
    
