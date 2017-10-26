#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:07:54 2017

@author: wahidari

# Algoritma Greedy Permasalahan Penentuan Jalur

Diketahui:
	Jalur: A, B, C, D, E, F, G, H, I
Ditanya:
	Jalur dengan jarak terpendek dari A ke I
Jawab:
	Solusi = {'A', 'C', 'D', 'E', 'F', 'B'}
    
# Kekurangan: 
- misalnya tidak adanya penanganan kasus jika titik tujuan tidak ditemukan, 
- atau jika terdapat node yang memiliki nilai negatif (bergerak balik). 
"""
import networkx as nx
import matplotlib.pyplot as plt

def shortest(maps, asal, tujuan): # mencari jalur terpendek dari maps (graph yg dibangun)
    result = [] # node dengan jarak terpendek simpan ke dalam list
    result.append(asal) # inisialisasi node pertama dengan nilai asal

    while tujuan not in result: # telusuri graph sampai tujuan ditemukan
        current_node = result[-1] # -1 == list di index terakhir
        print ("Node Terakhir :",current_node)
        jarak_terpendek = min(maps[current_node].values()) # Cari local maximum (nilai/jarak terkecil dari node terakhir ke node selanjutnya)
#        print ("Node Dengan Jarak Terpendek Dari Node Terakhir :|", jarak_terpendek)
       
        for node, jarak in maps[current_node].items(): # iterasi mencari node selanjutnya
            print ("Node Selanjutnya :",node,"| Jarak :",jarak)
            if jarak == jarak_terpendek:
                 # ambil node dengan jarak terpendek dan tambahkan ke list result
                 # agar iterasi selanjutnya dimulai dari node sekarang.
                result.append(node)

    return result

full_maps = { # graph direpresentasikan dengan menggunakan dictionary di dalam dictionary,
        'A': {'B': 6, 'C': 4},
        'B': {'H': 8},
        'H': {'I': 7},
        'C': {'D': 6, 'E': 7},
        'E': {'I': 12},
        'D': {'F': 6, 'G': 5},
        'F': {'H': 2},
        'G': {'I': 7}
       }

simple_maps = { # graph direpresentasikan dengan menggunakan dictionary di dalam dictionary,
        'A': {'B': 6, 'C': 4},
        'B': {'F': 8},
        'C': {'D': 6},
        'D': {'E': 6},
        'E': {'F': 2}
       }

def draw(maps):
    g = nx.DiGraph()
    color = []
    if (maps == int(1)):
        g.add_edge("A", "C", weight="4 km")
        g.add_edge("A", "B", weight="6 km")
        g.add_edge("C", "D", weight="6 km")
        g.add_edge("D", "E", weight="6 km")
        g.add_edge("E", "F", weight="2 km")
        g.add_edge("B", "F", weight="8 km")
        color = ['g','b','b','b','b','r']
    if (maps == int(2)):
        g.add_edge("A", "C", weight="4 km")
        g.add_edge("A", "B", weight="6 km")
        g.add_edge("C", "D", weight="6 km")
        g.add_edge("C", "E", weight="7 km")
        g.add_edge("D", "F", weight="6 km")
        g.add_edge("D", "G", weight="5 km")
        g.add_edge("F", "H", weight="2 km")
        g.add_edge("B", "H", weight="8 km")
        g.add_edge("E", "I", weight="12 km")
        g.add_edge("G", "I", weight="7 km")
        g.add_edge("H", "I", weight="7 km")
        color = ['g','b','b','b','b','b','b','b','r']
    pos = nx.shell_layout(g)
    edge_labels = { (u,v): d['weight'] for u,v,d in g.edges(data=True) }
    nx.draw_networkx_nodes(g,pos,node_size=1000, node_color=color)
    nx.draw_networkx_edges(g,pos)
    nx.draw_networkx_labels(g,pos)
    nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
    plt.title("MAPS")
    plt.axis("off")
    plt.show()
    
def _main():
    choose = int(input("Choose Maps :\n1. Simple Maps\n2. Full Maps\n\n"))
    if (choose == 1):
        print ("\nSimple Maps :")
        draw(choose)
        maps = shortest(simple_maps,"A","F")
        print ("\nJalur Dari 'A' ke 'F' :", maps)
    if (choose == 2):
        print ("\nFull Maps :")
        draw(choose)
        maps = shortest(full_maps,"A","I")
        print ("\nJalur Dari 'A' ke 'I' :", maps)
    
if __name__ == '__main__':
    _main()
