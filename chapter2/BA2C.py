def Kmers(text,k):
  kmers=[]
  for i in range(len(text)-k+1):
    kmer=text[i:i+k]
    if (kmer not in kmers):
      kmers.append(kmer)
  return kmers


def ProfileKmer(text,k,profile):
  probabilities={}
  for kmer in Kmers(text,k):
    prob=1
    for i in range(k):
      if (kmer[i]=="A"):
        prob=prob*profile[0][i]
      elif (kmer[i]=="C"):
        prob=prob*profile[1][i]
      elif (kmer[i]=="G"):
        prob=prob*profile[2][i]
      else:
        prob=prob*profile[3][i]
    
    probabilities[kmer]=prob

  max_val=max(probabilities.values())
  for k in probabilities:
    if (probabilities[k]==max_val):
      max_kmer=k
      break

  return max_kmer

### ispis

sample_=''''''

sample=sample_.splitlines()
text=sample[0]
k=int(sample[1])
matrica=sample[2:]
profile=[]
for i in range(len(matrica)):
  matrica[i]=matrica[i].split(" ")
  row=[]
  for j in range(len(matrica[i])):
    row.append(float(matrica[i][j]))
  profile.append(row)

print(ProfileKmer(text,k,profile))

