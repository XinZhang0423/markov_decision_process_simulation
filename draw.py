import matplotlib.pyplot as plt
import networkx as nx
 

 
# 定义图的节点和边
nodes = ['0', '1', '2', '3', '4', '5', 'a', 'b', 'c']
edges = [('0', '0', 1), ('0', '1', 1), ('0', '5', 1), ('0', '5', 2), ('1', '2', 3), ('1', '4', 5), ('2', '1', 7),
         ('2', '4', 6), ('a', 'b', 0.5), ('b', 'c', 0.5), ('c', 'a', 0.5)]
 
plt.subplots(1, 2, figsize=(10, 3))
 
# 定义一个无向图和有向图
G1 = nx.Graph()
G1.add_nodes_from(nodes)
G1.add_weighted_edges_from(edges)
 
G2 = nx.DiGraph()
G2.add_nodes_from(nodes)
G2.add_edge('0','1')
G2.add_edge('1','0')
 
pos1 = nx.circular_layout(G1) # 圆形布局 起到美化作用
pos2 = nx.circular_layout(G2)
 

nx.draw(G2, pos2, with_labels=True, font_weight='bold')


 
plt.show()
