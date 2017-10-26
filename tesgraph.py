import networkx as nx
import matplotlib.pyplot as plt

def _main():
    g = nx.DiGraph()

    g.add_edge("A", "C", weight="4 km")
    g.add_edge("A", "G", weight="9 km")
    g.add_edge("G", "E", weight="6 km")
    g.add_edge("C", "D", weight="6 km")
    g.add_edge("C", "H", weight="12 km")
    g.add_edge("D", "E", weight="7 km")
    g.add_edge("H", "F", weight="15 km")
    g.add_edge("E", "F", weight="8 km")
    g.add_edge("F", "B", weight="5 km")
    
    pos = nx.circular_layout(g)
    
#    g.add_edge("A", "C", weight=4)
#    g.add_edge("A", "G", weight=9)
#    g.add_edge("G", "E", weight=6)
#    g.add_edge("C", "D", weight=6)
#    g.add_edge("C", "H", weight=12)
#    g.add_edge("D", "E", weight=7)
#    g.add_edge("H", "F", weight=15)
#    g.add_edge("E", "F", weight=8)
#    g.add_edge("F", "B", weight=5)

#    pos = nx.spring_layout(g)

    edge_labels = { (u,v): d['weight'] for u,v,d in g.edges(data=True) }
    color = ['g','b','b','b','b','b','b','r']

    nx.draw_networkx_nodes(g,pos,node_size=1000, node_color=color)
    nx.draw_networkx_edges(g,pos)
    nx.draw_networkx_labels(g,pos)
    nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)

    plt.title("MAPS")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    _main()
