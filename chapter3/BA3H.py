def StringReconstruction(patterns,k):
    suffix=[]
    prefix=[]

    graph={}
    for kmer in patterns:
        suffix.append(kmer[1:])
        prefix.append(kmer[:-1])
        graph[kmer[:-1]]=kmer[k-1:k]

    for p in prefix:
        if p not in suffix:
            start=p
            break

    textStart=start+graph[start]

    for s in suffix:
        if s not in prefix:
            end=s
            break

    text=textStart
    while True:
        textRest=text[len(text)-k+1:len(text)]
        if textRest==end:
            break
        else:
            text+=graph[textRest]
    return text

### ispis

sample_='''4
CTTA
ACCA
TACC
GGCT
GCTT
TTAC'''
sample=sample_.splitlines()
k=int(sample[0])
patterns=sample[1:]

print(StringReconstruction(patterns,k))
