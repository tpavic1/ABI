def Cyclospectrum(peptide):
    mass = {
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
    cyclo=[0,sum([mass[p] for p in peptide])]
    extended=peptide+peptide[:-1]
    
    for i in range(len(peptide)):
        for j in range(1,len(peptide)):
            subPeptide=extended[i:i+j]
            cyclo.append(sum([mass[p] for p in subPeptide]))

    return sorted(cyclo)

def Score(peptide, spectrum):
    cyclo=Cyclospectrum(peptide)
    count=0
    for n in spectrum:
        if(n in cyclo):
            count+=1
            cyclo.remove(n)
    return count

### ispis

sample_=''''''
sample=sample_.splitlines()
peptide=sample[0]
spectrum=list(map(int,sample[1].split(" ")))
print(Score(peptide, spectrum))
