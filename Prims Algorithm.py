# Prims algorithm to find a minimum spanning tree given an adjacency matrix
# 27/06/2025

INF = float('inf')

adjacency_matrix=[
    [INF,16,12,21,INF,INF,INF],
    [16,INF,INF,17,20,INF,INF],
    [12,INF,INF,28,INF,31,INF],
    [21,17,28,INF,18,19,23],
    [INF,20,INF,18,INF,INF,11],
    [INF,INF,31,19,INF,INF,27],
    [INF,INF,INF,23,11,27,INF]
]

# look along the rows, and delete columns (by replacing with INF)
current_row=0
MST_weight=0
for row in adjacency_matrix:
        row[0] = INF
MST="A" # start at A, assumes each node is laballed A, B, C in order in the matrix
visited_nodes=[0]

for i in range(len(adjacency_matrix)-1):
    # find next node
    distance=INF
    for node in visited_nodes:
        if distance>min(adjacency_matrix[node]):
            distance=min(adjacency_matrix[node])
            current_column=adjacency_matrix[node].index(distance)

    MST+=chr(65+current_column)
    MST_weight+=distance
    visited_nodes.append(current_column)
    # eliminate current column
    for row in adjacency_matrix:
        row[current_column] = INF
        
print(MST, MST_weight)
    
