def HD(a,b):
  br=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      br=br+1

  return br

def PatternMatching(pattern,text,d):
  rj=[]
  for i in range(len(text)-len(pattern)+1):
    pattern_=text[i:i+len(pattern)]
    if (HD(pattern,pattern_)<=d):
      rj.append(str(i))

  return rj


sample_=''''''
sample=sample_.splitlines()
pattern=sample[0]
text=sample[1]
d=int(sample[2])

lista=PatternMatching(pattern,text,d)
ros=" ".join(lista)
print(ros)
