def MapToString(node):
    if node<0:
        return str(node)
    else:
        return "+"+str(node)

def CycleToChromosome(nodes):
    chromosome=[0]*(len(nodes)//2)

    for j in range(len(nodes)//2):
        if nodes[2*j]<nodes[2*j+1]:
            chromosome[j]=nodes[2*j+1]//2
        else:
            chromosome[j]=-nodes[2*j]//2
       
    return chromosome            

### ispis

sample='''(1 2 4 3 6 5 7 8)'''
nodes=list(map(int,sample[1:-1].split(" ")))
res=list(map(MapToString,CycleToChromosome(nodes)))
ros="("+" ".join(res)+")"
print(ros)
