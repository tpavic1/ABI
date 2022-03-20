def MinimumSkew(genome):
  d={}
  c=0
  g=0
  for i in range(len(genome)):
    if(genome[i]=="C"):
      c+=1
    elif(genome[i]=="G"):
      g+=1
    diff=g-c
    d[i+1]=diff
  
  min_val=min(d.values())
  rj=[]
  for k in d.keys():
    if (d[k]==min_val):
      rj.append(str(k))

  return rj


lista=MinimumSkew('')
ros=" ".join(lista)
print(ros)
