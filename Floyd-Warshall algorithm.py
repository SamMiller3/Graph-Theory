#Floyd-Warshall algorithm 07/07/25

import numpy as np

INF = 999999 # a value of 999999 denotes null or infinity (there is no direct connection)
# 0 is used for distance to reach itself
adjacency_matrix= np.array([
    [0,15,7,18,3],
    [15,0,INF,INF,INF],
    [7,5,0,4,9],
    [18,INF,4,0,3],
    [INF,INF,9,3,0]
]) 

n = len(adjacency_matrix)
predecessor_matrix = np.tile(np.arange(1, n+1), (n, 1)) # initialise 
distance_matrix = adjacency_matrix.copy()

for k in range(n): # intermediate values
    for i in range(n): # rows
        for j in range(n): # columns
            if distance_matrix[i,k]+distance_matrix[k,j] < distance_matrix[i,j]: # update shortest route based on intermediate
                distance_matrix[i,j] = distance_matrix[i,k]+distance_matrix[k,j]
                predecessor_matrix[i,j] = k+1

print("least distance matrix:")
print(distance_matrix)
print("predecessor matrix:")
print(predecessor_matrix)