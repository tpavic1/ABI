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

### ispis

sample_=''''''
sample=sample_.splitlines()
text=sample[0]
k=int(sample[1])
matrica=sample[2:]
profile=[]
for i in range(len(matrica)):
    matrica[i]=matrica[i].split(" ")
    row=[]
    for j in range(len(matrica[i])):
        row.append(float(matrica[i][j]))
    profile.append(row)

print(ProfileMostProbableKmer(text, profile, k))

