def StringComposition(text,k):
  lista=[]
  for i in range(len(text)-k+1):
    lista.append(text[i:i+k])
  lita=lista.sort()
  
  return lista

### ispis

sample_=''''''
sample=sample_.splitlines()
k=int(sample[0])
text=sample[1]

for kmer in StringComposition(text,k):
  print(kmer)
