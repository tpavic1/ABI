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

def deBrujin(paired_reads):
    D=dict()
    for prvi,drugi in paired_reads:
        D[(prvi[:-1],drugi[:-1])]=(prvi[1:],drugi[1:])
    return D

def EulerianPath(D):
    keys=list(D.keys())
    values=list(D.values())
    
    for i in range(len(keys)):
        if keys[i] not in values:
            prvi_cvor=keys[i]
    for i in range(len(values)):
        if values[i] not in keys:
            zadnji_cvor=values[i]

    #nadimo indeks od prvi_cvor u nizu keys:
    for i in range(len(keys)):
        if keys[i]==prvi_cvor:
            indeks=i
    #uzmemo njegov par u nizu values:
    njegov_par=values[indeks]
    put=[prvi_cvor,njegov_par]

    while njegov_par!=zadnji_cvor:
        for i in range(0,len(keys)):
            if keys[i]==njegov_par:
                index=i
                put.append(values[index])
                njegov_par=values[index]
    return put

def StringReconstruction(k,d,pairedReads):
    graph=deBrujin(pairedReads)
    path=EulerianPath(graph)  #s ovin dobijen ono iz zadatka L
    string=StringSpelledGappedPatterns(path,k,d)
    return string

### ispis

sample_='''4 2
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT'''
sample=sample_.splitlines()
k,d=list(map(int,sample[0].split(" ")))
gappedPatterns=[s.split("|") for s in sample[1:]]


print(StringReconstruction(k,d,gappedPatterns))
