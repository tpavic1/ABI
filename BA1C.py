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

### ispis

print(ReverseComplement(""))
