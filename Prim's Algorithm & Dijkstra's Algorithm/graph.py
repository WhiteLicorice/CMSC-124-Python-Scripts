## An undirected weighted graph data structure implementation by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023

import random

INF_WEIGHT = 999999999999999999999999   ##Global value for effective infinite weight

class graph_udr_wgt:

    ## Constructor => an undirected weighted graph implemented with Python's dictionary (hashmap) as a base
    def __init__(self):
        self.graph = dict()

    ## Setter => inserts/updates an edge between two vertices in the graph, automatically creating vertices if they do not exist
    def update_edge(self, vertex_one, vertex_two, weight):
        if vertex_one not in self.graph:
            self.graph[vertex_one] = []     ## Create new adjacency list => vertex_one as the key and the list as its value
        if vertex_two not in self.graph:
            self.graph[vertex_two] = []     ## Similarly for vertex_two

        ## Check if the weight input is a valid int, throwing an error if not 
        try:
            weight = int(weight)
        except:
            raise Exception("TypeError: weight object must be typable int.")

        ## Update the adjacency lists of both vertices with a (vertex, weight) tuple representing an edge and its cost between them
        self.graph[vertex_one].append((vertex_two, weight))                
        self.graph[vertex_two].append((vertex_one, weight))

    #Getter => Get the edge weight of the input vertices
    def get_weight(self, vertex_one, vertex_two):
        for vertex, adjacency_list in self.graph.items():
            if (vertex == vertex_one):
                for weight in adjacency_list:
                    if weight[0] == vertex_two:
                        return weight[1]
            
    ## Getter => Get a representation of the graph (source--weight-->destination) 
    def show_graph(self):
        for source, adjacency_list in self.graph.items():
            for node_weight in adjacency_list:
                print(f"{source}--{node_weight[1]}-->{node_weight[0]}") 

    ## Getter => Get random vertex from graph
    def random_node(self):
        return random.choice(list(self.graph))

    ## Getter => Get a list representation of the vertices in the graph
    def list_nodes(self):
        return list(self.graph)

    ## Getter => Get number of vertices in the graph 
    def count_nodes(self):
        return len(self.list_nodes())

    ## Getter => Get the dictionary repr. of the graph
    def get_graph(self):
        return self.graph

    ## Getter => Get the neighbors of a vertex in a list
    def get_neighbors(self, vertex):
        return self.graph[vertex]
    
def test_graph():
    g = graph_udr_wgt()

    g.update_edge("A", "B", 1)
    g.update_edge("A", "C", 2)
    g.update_edge("A", "D", 9)
    g.update_edge("A", "E", 6)
    
    g.update_edge("B", "C", 3)
    
    g.update_edge("C", "E", 4)
    g.update_edge("C", "D", 6)

    g.show_graph()
    print(g.list_nodes())
    print(g.count_nodes())
    print(g.get_weight("A","B"))

