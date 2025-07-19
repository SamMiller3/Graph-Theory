# Djisktras shortest path algorithm on an adjacency matrix 
# implemented using dynamic programming by updating the cumulative distance choosing the local optimal node each
# iteration (greedy)
# 08/07/2025 - 09/07/2025

# Djisktras shortest path algorithm

import numpy as np

INF = float('inf') # a value of INF denotes not adjacent
# 0 is used for distance to reach itself
adj_mat= np.array([
    [0,32,16,75,INF,95,INF,INF],
    [32,0,INF,33,15,INF,INF,INF],
    [16,INF,0,50,INF,70,105,113],
    [75,33,50,0,17,INF,50,INF],
    [INF,15,INF,17,0,30,INF,INF],
    [INF,INF,INF,INF,30,0,25,41],
    [INF,INF,105,50,INF,25,0,10],
    [INF,INF,113,INF,INF,41,10,0]
])  # edit this adj matrix to construct a different graph

start_node = int(input("what is the start node? (eg 0, 1, 5, 7 note it is 0 indexed): "))
dis_mat = adj_mat.copy() # Working matrix that gets updated with cumulative distances from source
predecessor = {} # store the predecessor to construct the path at the end
distances = {} # store the distance to each node from the source

visited_nodes = [start_node]
distances[start_node]=[0]
dis_mat[:, start_node] = INF # delete first column so not to revist
predecessor[start_node] = start_node 

# Main algorithm loop - visit all nodes
while len(visited_nodes)!=len(adj_mat):
    min_distance = INF
    # Find closest unvisited node from any visited node
    for node in visited_nodes:
        if min_distance > np.min(dis_mat[node]): # check each visited node to see closest adj node
            min_distance = np.min(dis_mat[node]) # store distance
            next_node = np.argmin(dis_mat[node]) # and next node
            prev_node = node # store predecessor
    visited_nodes.append(next_node)
    distances[next_node] = min_distance
    dis_mat[:, next_node] = INF # delete next column so not to visit it twice
    dis_mat[next_node] += min_distance # Update all edges from this node with cumulative distance from source
    predecessor[next_node] = prev_node

target_node = int(input("what is the target node? "))

# construct path
prev_node = target_node
path = str(prev_node)
while predecessor[prev_node] != start_node:
    prev_node = predecessor[prev_node]
    path = str(prev_node) + "-" + path
path = str(start_node) + "-" + path
print(f"shortest path is: {path}")
print(f"distance is {distances[target_node]}")
