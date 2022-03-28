def StringGenomePath(patterns):
    text=patterns[0]
    for pattern in patterns[1:]:
        text=text+pattern[-1]

    return text
  
### ispis
  
sample_=''''''
sample=sample_.splitlines()

print(StringGenomePath(sample))
