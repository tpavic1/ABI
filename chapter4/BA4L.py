def LinearSpectrum(peptide):
    linear=[0]

    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            subPeptide=peptide[i:j]
            linear.append(sum([mass[p] for p in subPeptide]))

    return sorted(linear)

def LinearScore(peptide, spectrum):
    linear=LinearSpectrum(peptide)
    count=0
    for n in spectrum:
        if(n in linear):
            count+=1
            linear.remove(n)
    return count

def Trim(leaderboard, Spectrum, N):
    scores=list(map(LinearScore, leaderboard, [Spectrum]*len(leaderboard)))
    try:
        cut=sorted(scores, reverse=True)[N-1]
        return [leaderboard[i] for i in range(len(leaderboard)) if scores[i]>=cut]
    except:
        return leaderboard

### ispis

sample_=''''''
sample=sample_.splitlines()
leaderboard=sample[0].split(" ")
spectrum=list(map(int,sample[1].split(" ")))
N=int(sample[2])

res=Trim(leaderboard,spectrum, N)[:N]
print(" ".join(res))
