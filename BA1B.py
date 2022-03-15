def MostFrequentKmers(text,k):
  freq={}
  for i in range(len(text)-k+1):
    kmer=text[i:(i+k)]
    if (kmer not in freq.keys()):
      freq[kmer]=1
    else:
      freq[kmer]+=1
  
  max_value=max(freq.values())
  most_freq=[]
  for key in freq:
    if (freq[key]==max_value):
      most_freq.append(key)
  
  return most_freq


### ispis

sample_=''
sample=sample_.splitlines()
text=sample[0]
k=int(sample[1])

lista=MostFrequentKmers(text,k)

ros=" ".join(lista)
print(ros)
