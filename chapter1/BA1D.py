def PatternMatching(pattern,text):
  indices=[]
  k=len(pattern)
  for i in range(len(text)-k+1):
    pattern_=text[i:i+k]
    if(pattern==pattern_):
      indices.append(str(i))

  return indices

### ispis

sample_=''
sample=sample_.splitlines()
pattern=sample[0]
text=sample[1]

lista=PatternMatching(pattern,text)
ros=" ".join(lista)
print(ros)
