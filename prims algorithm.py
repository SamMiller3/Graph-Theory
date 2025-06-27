# Prims algorithm to find a minimum spanning tree given a distance matrix
# 27/06/2025

# a value of 999999 denotes null or infinity
distance_matrix=[
    [999999,16,12,21,999999,999999,999999],
    [16,999999,999999,17,20,999999,999999],
    [12,999999,999999,28,999999,31,999999],
    [21,17,28,999999,18,19,23],
    [999999,20,999999,18,999999,999999,11],
    [999999,999999,31,19,999999,999999,27],
    [999999,999999,999999,23,11,27,999999]
]

# look along the rows, and delete columns (by replacing with 999999)
current_row=0
MST_weight=0
for row in distance_matrix:
        row[0] = 999999
MST="A" # start at A
visited_nodes=[0]

for i in range(len(distance_matrix)-1):
    # find next node
    distance=999999
    for node in visited_nodes:
        if distance>min(distance_matrix[node]):
            distance=min(distance_matrix[node])
            current_column=distance_matrix[node].index(distance)

    MST+=chr(65+current_column)
    MST_weight+=distance
    visited_nodes.append(current_column)
    # eliminate current column
    for row in distance_matrix:
        row[current_column] = 999999
        
print(MST, MST_weight)
    