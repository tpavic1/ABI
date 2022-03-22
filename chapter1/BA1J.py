def HD(a,b):
  br=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      br=br+1

  return br

from itertools import product

def AllKmers(k):
  kmers=[''.join(c) for c in product('ACGT', repeat=k)]

  return kmers

def Complement(letter):
  if(letter=="A"):
    return "T"
  elif(letter=="C"):
    return "G"
  elif(letter=="G"):
    return "C"
  else:
    return "A"
  
def ReverseComplement(pattern):
  comp=list(pattern)
  for i in range(len(pattern)):
    comp[i]=Complement(pattern[i])

  complement="".join(comp)
  rev_comp=complement[::-1]

  return rev_comp

def FreqWordsMismatchingAndRevComp(text,k,d):
  freq={}
  kmers=AllKmers(k)
  for kmer in kmers:
    rev_comp=ReverseComplement(kmer)
    for i in range(len(text)-k+1):
      kmer_=text[i:i+k]
      if(HD(kmer_,kmer)<=d):
        if(kmer not in freq.keys()):
          freq[kmer]=1
        else:
          freq[kmer]+=1
      if(HD(kmer_,rev_comp)<=d):
        if(kmer not in freq.keys()):
          freq[kmer]=1
        else:
          freq[kmer]+=1
  
  max_val=max(freq.values())
  rj=[]
  for key in freq:
    if (freq[key]==max_val):
      rj.append(key)

  return rj

### ispis
sample_=''''''
sample=sample_.splitlines()
text=sample[0]
brojevi=sample[1]
k_,d_=brojevi.split(" ")
k=int(k_)
d=int(d_)

lista=FreqWordsMismatchingAndRevComp(text,k,d)
ros=" ".join(lista)
print(ros)

