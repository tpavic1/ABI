def DeBrujinGraph(text,k):
    graph={}
    for i in range(len(text)-k+1):
        node=text[i:i+k-1]
        if(node not in graph.keys()):
            graph[node]=[text[i+1:i+k]]
        else:
            graph[node].append(text[i+1:i+k])
    
    for key in graph:
        graph[key]=sorted(graph[key])

    return graph
  
### ispis
  
sample_=''''''
sample=sample_.splitlines()
k=int(sample[0])
text=sample[1]

graph=DeBrujinGraph(text,k)

for key in sorted(graph):
    ispis=''
    for i in range(len(graph[key])):
        if(i==(len(graph[key])-1)):
            ispis+=graph[key][i]
        else:
            ispis+=graph[key][i]+","
    print(key+" -> "+ispis)
