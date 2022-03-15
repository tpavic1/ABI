def PatternCount(text,pattern):
  count=0
  for i in range(len(text)-len(pattern)+1):
    if(text[i:i+len(pattern)]==pattern):
      count+=1
  return count

### ispis

sample_=''
sample=sample_.splitlines()

text=sample[0]
pattern=sample[1]

print(PatternCount(text,pattern))
