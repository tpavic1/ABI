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

### ispis

sample_=''''''
sample=sample_.splitlines()
peptide=sample[0]
spectrum=list(map(int,sample[1].split(" ")))

print(LinearScore(peptide, spectrum))
