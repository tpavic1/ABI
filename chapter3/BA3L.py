def StringSpelledGappedPatterns(gappedPatterns,k,d):
    FirstPatterns=[g[0]for g in gappedPatterns]
    SecondPatterns=[g[1]for g in gappedPatterns]

    PrefixString=FirstPatterns[0]
    SufixString=SecondPatterns[0]
    
    for i in range(1,len(FirstPatterns)):
        PrefixString+=FirstPatterns[i][-1]
        
    for i in range(1,len(SecondPatterns)):
        SufixString+=SecondPatterns[i][-1]

    for i in range(k+d+1,len(PrefixString)):
        if PrefixString[i]!=SufixString[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return PrefixString+SufixString[len(SufixString)-k-d:]

### ispis

sample_='''4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA'''
sample=sample_.splitlines()
k,d=list(map(int,sample[0].split(" ")))
gappedPatterns=[s.split("|") for s in sample[1:]]

print(StringSpelledGappedPatterns(gappedPatterns, k, d))
