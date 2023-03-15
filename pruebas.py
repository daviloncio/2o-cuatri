import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(1, 4):
        G.add_node(i)
        
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)   
 

color_map = []
for node in G:
     color_map.append('grey')
    

nx.draw(nx.bfs_tree(G,1), node_color=color_map, with_labels=True)


plt.show()



'''

# add vertices
for i in range(1, 4):
        G.add_vertex(i)

      
# add edges

G.set_vertices_attribute("color","white")
print('Total edges in the graph:', G.edges_count())
print('Total vertices in the graph:', G.vertices_count())
print('\nPrint graph:\n', G)

# DFS_iter
DFS_iter(G, 1)
atr = 'parent'
print(f'\nAfter DFS_iter, Attribute {atr} of vertices:\n {G.get_vertices_attribute(atr)}')
    
# DFS_rec
G.set_vertices_attribute('color', 'WHITE')
DFS_rec(G, 1)
atr = 'parent'
print(f'\n After DFS_rec, attribute {atr} of vertices:\n {G.get_vertices_attribute(atr)}')'''