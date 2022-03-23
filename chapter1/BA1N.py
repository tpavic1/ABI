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

###ispis
sample_='''CGCTTAGAGA
2'''
sample=sample_.splitlines()
pattern=sample[0]
d=int(sample[1])

rj=Neighbors(pattern,d)
for n in rj:
  print(n)
