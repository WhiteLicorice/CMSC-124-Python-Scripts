## Dijkstra's Algorithm implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023

import graph

def dijkstra(input_graph, source):

    ## Dictionary container for the shortest path to each vertex
    sp = {}
    ## Container used for backtracking the path
    prev = {}

    ## Initialize values for sp and prev
    initialize_sssp(input_graph, source, sp, prev)

    ## Container for explored vertices
    ## Initially containing source vertex
    explored = [source]

    ## Loop the algorithm until all nodes are explored
    while(len(explored) != input_graph.count_nodes()):
        
        ## Get valid edges using auxiliary function
        valid_edge = get_valid_edges(input_graph, explored)
        ## Assume that the first edge is the chosen edge
        chosen_edge = valid_edge[0]
        ## Total weight = weight of the edge + value of the path from source
        chosen_edge_weight = sp[chosen_edge[0]] + chosen_edge[2]

        ## Compare each edge
        for edge in valid_edge:
            ## Get the total weight of the current edge
            edge_weight = sp[edge[0]] + edge[2]
            ## Choose the edge that minimizes total weight
            if chosen_edge_weight > edge_weight:
                chosen_edge = edge
                
        ## Relax the chosen edge
        relax(chosen_edge[0], chosen_edge[1], chosen_edge[2], sp, prev, input_graph)
        ## Add the currently explored edge to the container
        explored.append(chosen_edge[1])

    ## Print sp and prev containers
    print("SP:", sp)
    print("Prev: ", prev)

    ## Return the desired values
    return sp, prev, source, input_graph
                
def get_valid_edges(input_graph, explored):    
    ## Container for valid edges
    valid_edges = []

    ## Iterate through each vertex
    for vertex in input_graph.list_nodes():
        ## Check if vertex is explored
        if vertex in explored:
            ## Get the neighbors of the explored vertex
            for neighbor in input_graph.get_neighbors(vertex):
                ## If the neighbor is unexplored then it is a valid edge
                if neighbor[0] not in explored:
                    valid_edges.append((vertex, neighbor[0], neighbor[1]))
                    
    ## Return the edges
    return valid_edges
        
    
def relax(A, B, weight, sp, prev, input_graph):
    ## Check shortest path to B is greater than shortest path to A + edge weight
    if sp[B] > sp [A] + weight:
        ## Update shortest path
        sp[B] = sp[A] + weight
        ## Update prev dict
        prev[B] = A
    
def initialize_sssp(input_graph, source, sp ,prev):

    ## Iterate through each vertex 
    for vertex in input_graph.list_nodes():
        ## Intial weight path to each vertex is infinite
        sp[vertex] = graph.INF_WEIGHT
        ## Initial previous of each vertex is None
        prev[vertex] = None

    ## Path to source is 0
    sp[source] = 0

def display_sssp_header(sp, source, input_graph):
    ## Header
    print("Source:  ",source)
    print("---Single Source Shortest Path---")

    ## Iterate sp
    for vertex in sp:
        ## Skip source vertex
        if vertex == source:
            continue
        ## Print path
        print(source,"--",sp[vertex],"-->",vertex)
    ## Footer
    print("---Single Source Shortest Path---")

## Driver function for testing module  
def test_graph():
    ## Create a new instance of the graph class
    g = graph.graph_udr_wgt()

    ## Recreate the graph with update_edge setter method
    g.update_edge("A", "B", 1)
    g.update_edge("A", "C", 2)
    g.update_edge("A", "D", 9)
    g.update_edge("A", "E", 6)
    
    g.update_edge("B", "C", 3)
    
    g.update_edge("C", "E", 4)
    g.update_edge("C", "D", 6)

    ## Store the output of Dijkstra's Algorithm
    sssp = dijkstra(g, "A")
    
    ## Output result with auxilliary function
    display_sssp_header(sssp[0], sssp[2], sssp[3])

  

        
