#Floyd-Warshall algorithm 07/07/25

import numpy as np

INF = float('inf') # a value of INF denotes not adjacent
# 0 is used for distance to reach itself
adjacency_matrix= np.array([
    [0,4,7,INF],
    [4,0,INF,9],
    [7,INF,0,INF],
    [1,9,INF,0],
]) 

n = len(adjacency_matrix)
route_matrix = np.tile(np.arange(1, n+1), (n, 1)) # initialise 
# A table where each cell route[i][j] tells you the next hop to reach node j starting from node i.
distance_matrix = adjacency_matrix.copy()

for k in range(n): # intermediate values
    for i in range(n): # rows
        for j in range(n): # columns
            if distance_matrix[i,k]+distance_matrix[k,j] < distance_matrix[i,j]: # update shortest route based on intermediate
                distance_matrix[i,j] = int(distance_matrix[i,k]+distance_matrix[k,j])
                route_matrix[i,j] = k+1
    
    print("least distance matrix:")
    print(distance_matrix)
    print("route matrix:")
    print(route_matrix)

print("least distance matrix:")
print(distance_matrix)
print("route matrix:")
print(route_matrix)
