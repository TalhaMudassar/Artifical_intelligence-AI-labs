MyGraph = {
    'S' : {'A':3,'C':2,'D':2},
    'D' : {'B':3,'G':8},
    'B' : {'E':2},
    'E' : {'G':2},
    'C' : {'F':1},
    'F' : {'E':0,'G':4},
}
def UCS(MyGraph,Start):
    cost=0
    path=["S"]
    Queue, Visited = [cost,path],[]
    while Queue:
        minIndex=0
        i=0
        while i<len(Queue):
            if Queue[minIndex] > Queue[i]:
                minIndex=i
            i=i+2

        cost = Queue.pop(minIndex)
        path = Queue.pop(minIndex)
        last=path[len(path)-1]
        if last not in Visited:
            Visited.append(last)
            if last=="G":
                path.append("Total Cost: "+str(cost))
                return path
            if last not in MyGraph:
                continue
            for N in MyGraph[last].keys():
                NewPath=list(path)
                NewPath.append(N)
                Queue.append(cost+MyGraph[last][N])
                Queue.append(NewPath)
    return 0

print(UCS(MyGraph,'A'))