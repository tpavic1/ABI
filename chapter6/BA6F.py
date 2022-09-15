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

    return list(map(str,nodes))

### ispis

sample='''(+1 -2 -3 +4)'''
chromosome=list(map(int,sample[1:-1].split(" ")))

res=ChromosomeToCycle(chromosome)
ros="("+" ".join(res)+")"
print(ros)
