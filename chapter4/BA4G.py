massDict = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

def Expand(peptides):
    return [peptide+[m] for peptide in peptides for m in set(massDict.values())]

def Mass(peptide):
    return sum(peptide)

def CycloSpectrum(peptide):
    cyclo=[0]
    extended=peptide+peptide[:-1]

    for i in range(len(peptide)):
        for j in range(1, len(peptide)):
            subPeptide=extended[i:i+j]
            cyclo.append(sum(subPeptide))

    return sorted(cyclo)

def Score(peptide, spectrum):
    cyclo=CycloSpectrum(peptide)
    count=0
    for n in spectrum:
        if(n in cyclo):
            count+=1
            cyclo.remove(n)
    return count

def Trim(leaderboard, Spectrum, N):
    scores=list(map(Score, leaderboard, [Spectrum]*len(leaderboard)))
    try:
        cut=sorted(scores, reverse=True)[N-1]
        return [leaderboard[i] for i in range(len(leaderboard)) if scores[i]>=cut]
    except:
        return leaderboard
   

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    leaderboard=[[]]
    leaderPeptide=[]
    parentMass=max(Spectrum)

    while leaderboard:
        leaderboard=Expand(leaderboard)
        #print(leaderboard)
        for peptide in leaderboard.copy():
            if Mass(peptide)==parentMass:
                if Score(peptide, Spectrum)>Score(leaderPeptide, Spectrum):
                    leaderPeptide=peptide
            elif Mass(peptide)>parentMass:
                leaderboard.remove(peptide)
        leaderboard=Trim(leaderboard, Spectrum, N)

    return leaderPeptide

### ispis

sample_=''''''
sample=sample_.splitlines()
N=int(sample[0])
spectrum=list(map(int,sample[1].split(" ")))
res=map(str,LeaderboardCyclopeptideSequencing(spectrum,N))
print("-".join(res))
