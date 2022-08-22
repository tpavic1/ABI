import random
def EulerianCycle(graph):
    startNode=str(random.randint(0,len(graph)-1))
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
                if(node in graph):
                    newCycle=cycle[num:-1]+cycle[:num+1]
                    cycle=newCycle
                    currentNode=node
                    break
    return cycle

### ispis

sample_=''''''
sample=sample_.splitlines()
graph={}
for line in sample:
    elements=line.split(" -> ")
    node=elements[0]
    graph[node]=elements[1].split(",")

res=EulerianCycle(graph)
print("->".join(res))
