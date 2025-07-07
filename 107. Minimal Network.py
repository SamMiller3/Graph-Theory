# Project Euler Problem 107. Minimal Network
# 27/06/2025

adjacency_matrix=[] # process text file and convert to distance matrix
INF = float('inf')
with open('network.txt', 'r') as file:
    for line in file:
        row = []
        for val in line.strip().split(','):
            if val == '-':
                row.append(INF) # convert null values to INF
            else:
                row.append(int(val))
        adjacency_matrix.append(row)

# find weight of network

weight=0
for i in range(1,len(adjacency_matrix)):
    for j in range(i):
        if adjacency_matrix[i][j]!=INF:
            weight+=adjacency_matrix[i][j]
print(weight)


# look along the rows, and delete columns (by replacing with INF)
current_row=0 # start at first row
MST_weight=0
for row in adjacency_matrix:
        row[0] = INF
visited_nodes=[0]

for i in range(len(adjacency_matrix)-1):
    # find next node
    distance=INF
    for node in visited_nodes:
        if distance>min(adjacency_matrix[node]):
            distance=min(adjacency_matrix[node])
            current_column=adjacency_matrix[node].index(distance)

    MST_weight+=distance
    visited_nodes.append(current_column)
    # eliminate current column
    for row in adjacency_matrix:
        row[current_column] = INF
        
print(MST_weight)
print(weight-MST_weight)
