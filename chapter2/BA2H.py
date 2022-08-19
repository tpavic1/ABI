def HD(a,b):
  br=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      br=br+1
  return br

def Kmer(text, i, k):
    return text[i:(i+k)]

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k=len(pattern)
    distance=0
    for string in Dna:
        hammingDistance=len(pattern)
        for i in range(len(string)-k+1):
            pattern_=Kmer(string, i, k)
            if hammingDistance>HD(pattern, pattern_):
                hammingDistance=HD(pattern, pattern_)
        distance+=hammingDistance
    return distance

### ispis

sample_=''''''
sample=sample_.splitlines()
pattern=sample[0]
dna=sample[1].split(" ")

print(DistanceBetweenPatternAndStrings(pattern, dna))
