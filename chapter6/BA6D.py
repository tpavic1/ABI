def ChromosomeToCycle(kromosom):
    nodes=[]
    for el in kromosom:
        if el>0:
            nodes.append(2*el-1)
            nodes.append(2*el)
        else:
            nodes.append(-2*el)
            nodes.append(-2*el-1)
    return nodes
        

def ColoredEdges(P):
    edges=[]
    for kromosom in P:
        nodes=ChromosomeToCycle(kromosom)
        for j in range(1,len(nodes),2):
            if j!=len(nodes)-1:
                edges.append([nodes[j],nodes[j+1]])
            else:
                edges.append([nodes[j],nodes[0]])
    return edges

def nadiSljedeci(trenutni,edges):
    if len(edges)==0:
        return -1
    idx=0
    while not(trenutni[0] in edges[idx] or trenutni[1] in edges[idx]):
        idx+=1
        if idx==len(edges):
            return -1
    return edges[idx]

def CycleToChromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome
            
def NadiSljedeci2(trenutni, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    val = trenutni[1]
    if val % 2 == 0:
        val -= 1
    else:
        val += 1
    while not val in edges[idx]:
        idx += 1
        if idx == len(edges):
            return -1
    if val == edges[idx][1]:
        edges[idx].reverse()
    return edges[idx]

def GraphToGenome(graph):#graph je niz uredenih parova
    P = []
    ciklusi = []
    idx = 0
    while len(graph)>0:
        ciklus = []
        trenutni = graph[0]
        while trenutni != -1:#NadiSljedeci2(trenutni, graph) vraæa -1 ako smo potrošili sve cvorove
            ciklus += trenutni
            graph.remove(trenutni)
            sljedeci = NadiSljedeci2(trenutni, graph)
            trenutni = sljedeci
        ciklusi.append(ciklus)

    for nodes in ciklusi:
        nodes = [nodes[-1]] + nodes[:-1]
        Chromosome = CycleToChromosome(nodes)
        P.append(Chromosome)
    return P

def NadiCikluse(edges):
    ciklusi=[]#punit cemo ovaj niz netrivijalnim ciklusima(tj. ciklusima duljine vece od 2
    while len(edges)>0:
        start=edges[0]
        edges.remove(edges[0])
        trenutni=nadiSljedeci(start,edges)
        ciklus=[start]
        while trenutni!=-1:
            ciklus.append(trenutni)
            edges.remove(trenutni)
            trenutni=nadiSljedeci(trenutni,edges)
        if len(ciklus)>2:
            ciklusi.append(ciklus)
    return ciklusi

def TwoBreakOnGenomeGraph(genomeGraph,i1,i2,i3,i4):
    if [i1, i2] in genomeGraph:
        for i in range(len(genomeGraph)):
            if genomeGraph[i] == [i1, i2]:
                genomeGraph[i] = [i1, i3]
    else:
        for i in range(len(genomeGraph)):
            if genomeGraph[i] == [i2, i1]:
                genomeGraph[i] = [i3, i1]
    if [i3, i4] in genomeGraph:
        for i in range(len(genomeGraph)):
            if genomeGraph[i] == [i3, i4]:
                genomeGraph[i] = [i2, i4]
    else:
        for i in range(len(genomeGraph)):
            if genomeGraph[i] == [i4, i3]:
                genomeGraph[i] = [i4, i2]
    return genomeGraph
    
    

def TwoBreakOnGenome(P,i1,i2,i3,i4):
    genomeGraph=ColoredEdges(P)
    genomeGraph=TwoBreakOnGenomeGraph(genomeGraph,i1,i2,i3,i4)
    Q=GraphToGenome(genomeGraph)
    return Q
    
def ShortestTransformation(P,Q):
    rez=[P]
    redEdges=ColoredEdges(P)
    blueEdges=ColoredEdges(Q)
    BreakpointGraph=blueEdges+redEdges

    ciklusi=NadiCikluse(BreakpointGraph)
    while len(ciklusi)>0:
        nonTrivialCiklus=ciklusi[0]
        for i in range(0,len(nonTrivialCiklus)-1):
            if nonTrivialCiklus[i][0] in nonTrivialCiklus[i+1]:
                nonTrivialCiklus[i].reverse()
            if nonTrivialCiklus[i+1][1] in nonTrivialCiklus[i]:
                nonTrivialCiklus[i+1].reverse()
        idx=0
        while not nonTrivialCiklus[idx] in redEdges:
            idx+=1
        i1,i2=nonTrivialCiklus[idx]

        if idx+2!=len(nonTrivialCiklus):
            i3,i4=nonTrivialCiklus[idx+2]
        else:
            i3,i4=nonTrivialCiklus[0]
        redEdges.remove([i1,i2])
        redEdges.remove([i3,i4])
        redEdges.append([i1,i4])
        redEdges.append([i2,i3])

        BreakpointGraph=redEdges+blueEdges
        ciklusi=NadiCikluse(BreakpointGraph)
        P=TwoBreakOnGenome(P,i1,i2,i4,i3)
        rez.append(P)
    return rez
    

def Print(P):
    P=P[1:-1].split(")(")
    for i in range(len(P)):
        P[i]=list(map(int,P[i].split()))
    return P

### ispis

sample_='''(+4 -12 -1 +2 +7 +5 +10 -9 +3 +13 +14 +11 +6 +8)
(+14 -4 +6 +2 -8 +7 -11 +5 -1 -12 +13 -10 +9 -3)'''
sample=sample_.splitlines()
P=sample[0]
Q=sample[1]

P=Print(P)
Q=Print(Q)
rez=ShortestTransformation(P,Q)
for el in rez:
    for i in range(len(el)):
        el[i]="("+" ".join("+"+str(j) if j>0 else str(j)for j in el[i])+")"
    print("".join(el))

