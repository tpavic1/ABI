def FreqKmersT(text,k,t):
  freq={}
  for i in range(len(text)-k+1):
    kmer=text[i:(i+k)]
    if (kmer not in freq.keys()):
      freq[kmer]=1
    else:
      freq[kmer]+=1

  lista=[]
  for k in freq.keys():
    if(freq[k]>=t):
      lista.append(k)
  return lista


def ClumpFinding(genome,k,L,t):
  rj=set()
  for i in range(len(genome)-L+1):
    interval=genome[i:i+L]
    for f in FreqKmersT(interval,k,t):
      rj.add(f)
  return rj


sample_=''
sample=sample_.splitlines()
genome=sample[0]
brojevi=sample[1]
k_,L_,t_=brojevi.split(" ")
k=int(k_)
L=int(L_)
t=int(t_)

skup=ClumpFinding(genome,k,L,t)
ros=" ".join(skup)
print(ros)

