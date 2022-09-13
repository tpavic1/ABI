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

    if HasEdges(graph):
        return "the input graph is not a DAG"
    else:
        return ", ".join(lista)

### ispis

sample_=''''''
sample=sample_.splitlines()

graph={}
allNodes=set()
for line in sample:
    nodes=line.split(" -> ")
    node=nodes[0]
    connections=nodes[1].split(",")
    graph[node]=connections

outgoing = set()
for v in graph.values():
    outgoing.update(v)

candidates=[]
for k in graph.keys():
    if k not in outgoing:
        candidates.append(k)

print(TopologicalOrdering(graph, candidates))
