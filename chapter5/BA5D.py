def HasIncomingEdges(node, graph):
    for key in graph:
        if node in graph[key]:
            return True
    return False

def TopologicalOrdering(graph, candidates):
    lista=[]

    while candidates:
        a=candidates[0]
        lista.append(a)
        candidates.remove(a)
        if a in graph:
            for b in graph[a].copy():
                graph[a].remove(b)
                if not HasIncomingEdges(b, graph):
                    candidates.append(b)

    return lista

def Predcessors(node, graph):
    return [n for n in graph if node in graph[n]]

def Weight(a,b, weights):
    node=a+"->"+b
    return int(weights[node])

def GraphCopy(graph):
    copy={}
    for node in graph:
        copy[node]=[n for n in graph[node]]
    return copy

def Final(final, source):
    for i in range(len(final)):
        if final[i]==source:
            indexFirst=i
    return final[indexFirst:]
   
def LongestPath(graph, candidates, weights, source, sink):
    final=[source]
    s={}

    for node in graph:
        s[node]=float('-inf')
    s[source]=0

    graphNew=GraphCopy(graph)
    graphT=TopologicalOrdering(graphNew, candidates)
    indexStart=graphT.index(source)
   
    for node in graphT[indexStart+1:]:
        predcessors=Predcessors(node, graph)  
        if(len(predcessors)>0):
            values=[s[p]+Weight(p,node,weights) for p in predcessors]
            maxVal=max(values)
            index=values.index(maxVal)
            s[node]=maxVal
            final.append(predcessors[index])

        if(node==sink):
            final.append(sink)
            break
    
    return s[sink], Final(final, source)

### ispis

sample_=''''''
sample=sample_.splitlines()

source=sample[0]
sink=sample[1]


graph={}
weights={}
for line in sample[2:]:
    w=line.split(":")
    weights[w[0]]=w[1]
    nodes=line.split("->")
    connection=nodes[1].split(":")

    if nodes[0] not in graph:
        graph[nodes[0]]=[connection[0]]
    else:
        graph[nodes[0]].append(connection[0])

outgoing = set()
for v in graph.values():
    outgoing.update(v)

candidates=[]
for k in graph.keys():
    if k not in outgoing:
        candidates.append(k)

res=LongestPath(graph, candidates, weights, source, sink)
print(res[0])
print("->".join(res[1]))
