def Kmers(text,k):
  kmers=[]
  for i in range(len(text)-k+1):
    kmer=text[i:i+k]
    if (kmer not in kmers):
      kmers.append(kmer)
  return kmers

def HD(a,b):
  br=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      br=br+1
  return br

def Neighbors(pattern,d):
  nucleotides={"A","C","G","T"}
  if (d==0):
    return {pattern}
  if (len(pattern)==1):
    return {"A","C","G","T"}

  neighborhood=set()
  suffixNeighbors=Neighbors(pattern[1:],d)
  for s_neighbor in suffixNeighbors:
    if (HD(pattern[1:],s_neighbor)<d):
      for n in nucleotides:
        neighborhood.add(n+s_neighbor)
    else:
      neighborhood.add(pattern[0]+s_neighbor)
  
  return neighborhood


def AppearingInDna(pattern,k,d,Dna):
  sadrzi={}
  j=0
  for string in Dna:
    for i in range(len(string)-k+1):
      pattern_=string[i:i+k]
      if(HD(pattern,pattern_)<=d):
        sadrzi[j]=1
    j+=1
  
  if(sum(sadrzi.values())==len(Dna)):
    return True
  else:
    return False


def MotifEnumeration(Dna,k,d):
  patterns=set()
  for string in Dna:
    for kmer in Kmers(string,k):
      for neighbor in Neighbors(kmer,d):
        if AppearingInDna(neighbor,k,d,Dna):
          patterns.add(neighbor)
  
  return patterns

### ispis

sample_=''
sample=sample_.splitlines()
br=sample[0]
k_,d_=br.split(" ")
k=int(k_)
d=int(d_)
dna=sample[1:]

rj=MotifEnumeration(dna,k,d)
ros=" ".join(rj)
print(ros)
