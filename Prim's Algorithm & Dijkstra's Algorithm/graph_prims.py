## Prim's Algorithm implemented by RA Jocsing for CMSC 124 LEC Term Paper S.Y. 2022-2023

import graph    

## Core function for Prim's Algorithm
def prims(g):
    ##Declare arrays for storage => t = current nodes in the spanning tree, t_edges = current edges in the spanning tree
    t = [ ]
    t_edges = [ ]
    
    ## Fetch random source node using getter method defined in the graph class
    ##source = g.random_node()
    
    ## Or simply set a node (A in this case) as the source
    source = "A"
    
    ## Add source to current nodes in the tree
    t.append(source)

    ## Add a dummy edge connecting the source node to itself
    t_edges.append((source, source, 0))

    ##Algorithm start => while not every node has been explored and added to the tree, keep looking for safe edges
    while (len(t) != g.count_nodes()):
        ## Get valid_edges using auxilliary function
        valid_edges = get_valid_edges(g, t)
        ## Assume that the safe edge is the first valid edge
        safe_edge = valid_edges[0]
        ## Validate assumption => check all valid edges and find the one with the minimum weight (recall: (src, dest, weight) tuples)
        for i in range(len(valid_edges) - 1):
            compare_edge = valid_edges[i+1] 
            if safe_edge[2] > compare_edge[2]:
                safe_edge = compare_edge
        ## Once the safe edge has been found, add the destination node to the nodes explored in the tree
        t.append(safe_edge[1])
        ## Add the safe edge to the current edges in the tree 
        t_edges.append(safe_edge)

    ## Return explicit safe edges and implicit path
    return t_edges

## Auxilliary function for finding valid edges 
def get_valid_edges(graph, tree):
    ## Create storage array for valid edges 
    valid_edges = [ ]

    ## Iterate through every vertex in the tree 
    for vertex in tree:
        ## Get the neighbors of the vertex from the graph using getter method 
        for node_weight in graph.get_neighbors(vertex):
            ## If the neighbor is not yet in the tree, then add its edge to the valid_edges 
            if node_weight[0] not in tree:
                valid_edges.append((vertex, node_weight[0], node_weight[1]))
    ## Return valid_edges
    return valid_edges

## Auxilliary function for printing a representation of the minimum spanning tree, along with the source node and its total weight 
def trace_path(graph, path):
    total_weight = 0
    
    print("---Minimum Spanning Tree Repr---")
    print(f"Source: {path[0][0]}")
    print("--Tree--")
    ## Simply iterate through all edges and print the paths 
    for i in range(len(path)):
        if i == 0:     ##Skip source node      
            continue
        else:
            print(f"{path[i][0]}--{path[i][2]}-->{path[i][1]}")
            total_weight += path[i][2]
            
    print("--Tree--")
    print(f"Total Weight: {total_weight}")
    print("---Minimum Spanning Tree Repr---")

## Auxilliary function for printing the minimum weight from the source node to all other nodes 
def trace_paths_all(g, path):
    dest = []
    
    for src_dest_wgt in path:
        dest.append(src_dest_wgt[1])

    src = dest[0]
    
    print("---Src-Wgt-Dest Repr---")
    print(f"Source: {src}")
    print("--Path--")

    ## Simply iterate through all the destination nodes (src also counts as one) 
    for node in dest:
        if node == src: ## Skip the source node 
            continue
        total_weight = 0 
        curr_dest = node
        ## Perform backtrace from edge with node == dest until dest == src to get total_weight of the path 
        while curr_dest != src:
            for edge in path:
                if curr_dest == edge[1]:
                    total_weight += edge[2]
                    curr_dest = edge[0]
                    break
        print(f"{src}--{total_weight}-->{node}")
    
    print("--Path--") 
    print("---Src-Wgt-Dest Repr---")   
                
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

    ## Store the edges that comprise the min_path from Prim's Algorithm 
    min_path = prims(g)

    ## Output using auxilliary function
    trace_path(g, min_path)
    print(f"{'-----------' : ^100}")
    trace_paths_all(g, min_path)
    

    
    
