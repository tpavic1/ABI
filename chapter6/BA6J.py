def BreakOnGenomeGraph(GenomeGraph, i, I, j, J):
     if (i,I) in GenomeGraph:
         GenomeGraph.remove((i,I))
     else:
         if (I,i) in GenomeGraph:
             GenomeGraph.remove((I, i))
     if (j,J) in GenomeGraph:
         GenomeGraph.remove((j,J))
     else:
         if (J,j) in GenomeGraph:
             GenomeGraph.remove((J, j))
     GenomeGraph.append((i,j))
     GenomeGraph.append((I,J))
     return GenomeGraph

## ispis

sample_='''(1, 4), (3, 6), (5, 7), (8, 9), (10, 11), (12, 14), (13, 15), (16, 17), (18, 20), (19, 21), (22, 24), (23, 25), (26, 28), (27, 29), (30, 31), (32, 34), (33, 35), (36, 37), (38, 40), (39, 41), (42, 43), (44, 46), (45, 47), (48, 49), (50, 52), (51, 54), (53, 55), (56, 58), (57, 59), (60, 62), (61, 64), (63, 66), (65, 67), (68, 69), (70, 71), (72, 73), (74, 76), (75, 77), (78, 79), (80, 81), (82, 84), (83, 85), (86, 87), (88, 90), (89, 92), (91, 93), (94, 95), (96, 98), (97, 99), (100, 101), (102, 103), (104, 105), (106, 107), (108, 109), (110, 111), (112, 113), (114, 116), (115, 117), (118, 119), (120, 121), (122, 124), (123, 126), (125, 127), (128, 129), (130, 131), (132, 134), (133, 135), (136, 137), (138, 2)
50, 52, 10, 11'''
sample=sample_.splitlines()

edges = sample[0]
edges = edges[1:-1]
p = edges.split("), (")
for i in range(len(p)):
    a = p[i].split(", ")
    p[i] = (int(a[0]), int(a[1]))
indices = sample[1].split(", ")
for i in range(len(indices)):
    indices[i] = int(indices[i])
  
res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
for i in range(len(res)):
    res[i] = str(res[i])
res = ", ".join(res)
print(res)
