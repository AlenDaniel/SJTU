from srccode import *

# 使用示例
data = [7,6,2,1,0]
data_edg = [(0,1,1),(0,2,4),(1,2,2),(1,3,5),(1,4,12),(2,3,2),(3,4,3)]
nodes = []
edgs = []
row = 0
col = 0
graph = Graph()
for id,x in enumerate(data):
    if id%3!=0:
        row+=1
    else:
        col=int(id/3)
        row = 0
    node = Node(id=id,h_scores=x,coordinates=(col,row))
    nodes.append(node)
    graph.add_node(node)

for x in data_edg:
    node1 = nodes[x[0]]
    node2 = nodes[x[1]]
    w = x[2]
    edg = Edge(start=node1,end=node2,weight=w)
    graph.add_edge(edg)

graph.set_start_and_goal(nodes[0], nodes[4])


try:
    astart = AStar()
    shortest_path_nodes = astart.a_star_search(graph)
    print(f"Shortest path nodes: {[node.coordinates for node in shortest_path_nodes]}")
except ValueError as e:
    print(e)