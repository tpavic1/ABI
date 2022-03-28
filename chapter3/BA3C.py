def Prefix(text):
    return(text[:-1])

def Sufix(text):
    return(text[1:])

def Overlap(patterns):
    graph={}

    for pattern in patterns:
        for pattern_ in patterns:
            if(Sufix(pattern)==Prefix(pattern_)):
                if(pattern not in graph.keys()):
                    graph[pattern]=[pattern_]
                else:
                    graph[pattern].append(pattern_)

    return graph
    
### ispis

sample_=''''''
sample=sample_.splitlines()

d=Overlap(sample)
for key in sorted(d):
    for value in d[key]:
        print(key+" -> "+value)
