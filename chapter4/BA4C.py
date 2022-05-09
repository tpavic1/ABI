def TheoreticalSpectrum(text):

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

    res=[]
    extended=text+text[:-1]
    for i in range(len(text)):
        for j in range(1,len(text)):
            substring=extended[i:i+j]
            res.append(sum([mass[x] for x in substring]))

    res.append(0)
    res.append(sum([mass[x] for x in text]))
    
    return map(str,sorted(res))

### ispis

sample='AYGGVYHYKSVT'
lista=TheoreticalSpectrum(sample)

print(" ".join(lista))

