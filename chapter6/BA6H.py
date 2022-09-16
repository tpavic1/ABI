def ChromosomeToCycle(chromosome):
    nodes=[0]*2*len(chromosome)

    for j in range(len(chromosome)):
        i=chromosome[j]
        if i>0:
            nodes[2*j]=2*i-1
            nodes[2*j+1]=2*i
        else:
            nodes[2*j]=-2*i
            nodes[2*j+1]=-2*i-1

    return nodes

def ColoredEdges(P):
    edges=[]

    for chromosome in P:
        nodes=ChromosomeToCycle(chromosome)
        nodes.append(nodes[0])
        for j in range(len(chromosome)):
            edges.append((nodes[2*j+1],nodes[2*j+2]))
    
    return edges

### ispis

sample_='''(+1 -2 -3)(+4 +5 -6)'''
sample=sample_[1:-1].split(")(")
P=[list(map(int,s.split(" "))) for s in sample]

res=map(str,ColoredEdges(P))
print(", ".join(res))
