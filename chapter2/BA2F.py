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


def FormPseudoCount(motifs):
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

def FormProfileFromPseudoCount(count, numOfMotifs):
    return [list(map(lambda x: x/(numOfMotifs+4), row)) for row in count]

def FormScoreFromPseudoCount(count):
    cols=len(count[0])
    score=0
    for j in range(cols):
        col=[count[0][j], count[1][j], count[2][j], count[3][j]]
        maxValue=max(col)
        colScore=sum(col)-maxValue-3
        score+=colScore
    return score

import random
def RandomizedMotifSearchOneIteration(Dna, k, t):
    indexes=[random.randint(0,len(Dna[0])-k) for string in Dna]    
    motifs=[Dna[i][indexes[i]:(indexes[i]+k)] for i in range(len(Dna))]
    bestMotifs=[Dna[i][indexes[i]:(indexes[i]+k)] for i in range(len(Dna))]
    while(True):
        count=FormPseudoCount(motifs)
        profile=FormProfileFromPseudoCount(count, len(Dna))
        motifs=[ProfileMostProbableKmer(string, profile, k) for string in Dna]
        if FormScoreFromPseudoCount(FormPseudoCount(motifs))<FormScoreFromPseudoCount(FormPseudoCount(bestMotifs)):
            bestMotifs=[motif for motif in motifs]
        else:
            return bestMotifs

def RandomizedMotifSearch(Dna, k, t):
    bestMotifs=RandomizedMotifSearchOneIteration(Dna, k, t)
    for i in range(1, 1000):
        motifs = RandomizedMotifSearchAtom(Dna, k, t)
        if FormScoreFromPseudoCount(FormPseudoCount(motifs)) < FormScoreFromPseudoCount(FormPseudoCount(bestMotifs)):
            bestMotifs = [motif for motif in motifs]
    return bestMotifs

### ispis

sample_=''''''
sample=sample_.splitlines()
k, t=[int(x) for x in sample[0].split(" ")]
Dna=sample[1:]

res=RandomizedMotifSearch(Dna, k, t)
for r in res:
    print(r)
