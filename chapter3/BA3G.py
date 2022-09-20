import random
def EulerianCycle(graph, start):
    startNode=start
    currentNode=startNode
    cycle=[startNode]
    while graph:
        if currentNode in graph:
            cycle.append(graph[currentNode][0])
            if len(graph[currentNode])==1:
                graph.pop(currentNode)
            else:
                graph[currentNode].pop(0)
            currentNode=cycle[-1]
        else:
            for num, node in enumerate(cycle):
                if(node in graph.keys()):
                    newCycle=cycle[num:-1]+cycle[:num+1]
                    cycle=newCycle
                    currentNode=node
                    break
    return cycle


from collections import Counter

def addEdge(graph):
    inEdges=Counter()
    outEdges=Counter()

    for key, value in graph.items():
        outEdges[key]+=len(value)
        for v in value:
            inEdges[v]+=1
   
    start=list(inEdges-outEdges)[0]
    end=list(outEdges-inEdges)[0]

    graph[start]=[end]
    
    return start, end

def EulerianPath(graph):
    start, end=addEdge(graph)
    cycle=EulerianCycle(graph, start)
    for i in range(len(cycle)):
        if cycle[i]==start and cycle[i+1]==end :
            return cycle[i+1:]+cycle[:i+1]

### ispis

sample_='''0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6'''
sample=sample_.splitlines()
graph={}
for line in sample:
    elements=line.split(" -> ")
    node=elements[0]
    graph[node]=elements[1].split(",")

res=EulerianPath(graph)
print("->".join(res))
