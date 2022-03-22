def symbolToNumber(symbol):
  if(symbol=="A"):
    return 0
  elif(symbol=="C"):
    return 1
  elif(symbol=="G"):
    return 2
  else: 
    return 3

def PatternToNumber(pattern):
  if(len(pattern)==0):
    return 0
  symbol=pattern[-1]
  prefix=pattern[:-1]
  return 4*PatternToNumber(prefix)+symbolToNumber(symbol)

def ComputingFrequencies(text,k):
  freq_arr=[]
  for i in range(4**k):
    freq_arr.append(0)
  for i in range(len(text)-k+1):
    pattern=text[i:i+k]
    j=PatternToNumber(pattern)
    freq_arr[j]=freq_arr[j]+1

  return freq_arr

### ispis
sample_=''''''
sample=sample_.splitlines()
text=sample[0]
k=int(sample[1])
rj=ComputingFrequencies(text,k)
list_string = map(str, rj) 
ros=" ".join(list_string)
print(ros)
