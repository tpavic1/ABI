def DeBrujinGraphKmers(patterns):
    graph={}
    for pattern in patterns:
        node=pattern[:-1]
        if(node not in graph.keys()):
            graph[node]=[pattern[1:]]
        else:
            graph[node].append(pattern[1:])

    for key in graph:
        graph[key]=sorted(graph[key])
    
    return graph

### ispis

sample_=''''''
sample=sample_.splitlines()

graph=DeBrujinGraphKmers(sample)

for key in sorted(graph):
    ispis=''
    for i in range(len(graph[key])):
        if(i==(len(graph[key])-1)):
            ispis+=graph[key][i]
        else:
            ispis+=graph[key][i]+","
    print(key+" -> "+ispis)
