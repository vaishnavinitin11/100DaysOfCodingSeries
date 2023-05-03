# Day 84 coding Statement: 

def dfs(graph,start):
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    return visited


N=int(input('enter number of vertices: '))
M=int(input('Enter color: '))
E=int(input('Enter number of edges to be entered: '))
Edges=[]
for ed in range(E):
    edg=tuple(map(int,input('Enter edge '+str(ed+1)+': ').split()))
    Edges.append(edg)

# to convert from edges to graph
graph={}

for v,q in Edges:
    if v not in graph:
        graph[v]=[]
    if q not in graph:
        graph[q]=[]

for d in graph:
    for (x,y) in Edges:
        if x==d:
            graph[d].append(y)
        if y==d:
            graph[d].append(x)

# main coding part
visited=dfs(graph,0)

f={}
t=len(visited)
tr=0
m=M
m1=m
while t!=0:
    if m1==0:
        m1=m
    
    if t==1 and (m1==f[visited[tr-1]] and m1==f[visited[0]]):
        if (m1+1)<=m:
            m1+=1
        else:
            break

    elif t==1 and (m1==f[visited[tr-1]] or m1==f[visited[0]]) :
        if (m1+1)<=m:
            m1+=1
        elif m1==m:
            m1-=1
    f[visited[tr]]=m1
    m1-=1
    tr+=1
    t-=1
if f[visited[-1]]==f[visited[0]] or f[visited[-1]]==f[visited[-2]]:
    print('Output: 0')
else:
    print('Output: 1')

