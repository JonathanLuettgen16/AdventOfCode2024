import networkx as nx

def createGraphFromMatrix(input_matrix):
    # Initialize directed graph
    G = nx.DiGraph()
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    start_nodes = []
    end_nodes = []

    # Helper function to add edges
    def addEdgeIfValid(x1, y1, x2, y2):
        # Ensure that next point is in bounds of the matrix and the value is one more than the current
        if 0 <= x2 < rows and 0 <= y2 < cols and input_matrix[x2][y2] == input_matrix[x1][y1] + 1:
            G.add_edge((x1, y1), (x2, y2))

    # Add nodes and edges
    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j] == 0:
                G.add_node((i, j))
                start_nodes.append((i, j))
            # Check and add edges to north, east, south, and west neighbors
            if input_matrix[i][j] != 9:  # Nodes with value 9 are end points
                # North
                addEdgeIfValid(i, j, i-1, j)
                # South
                addEdgeIfValid(i, j, i+1, j)
                # West
                addEdgeIfValid(i, j, i, j-1)
                # East
                addEdgeIfValid(i, j, i, j+1)
            elif input_matrix[i][j] == 9:
                end_nodes.append((i, j))

    return G, start_nodes, end_nodes


def countReachableEndpoints(graph, start):
    def dfsPart1(current, visited):
        visited.add(current)
        count = 0
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                if matrix[neighbor[0]][neighbor[1]] == 9:
                    count += 1
                dfsPart1(neighbor, visited)
            return count
    return dfsPart1(start, set())



def countPaths(graph, start, end, max_path_length = 9):
    def dfsPart2(current, end, visited, steps):
        if steps > max_path_length:
            return 0
        if current == end and steps == max_path_length:
            print(f"Found path {visited} --> {current}")
            return 1
        visited.add(current)
        path_count = 0
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                path_count += dfsPart2(neighbor, end, visited, steps + 1)
        visited.remove(current)
        return path_count
    return dfsPart2(start, end, set(), 0)

# Example matrix
matrix = open("Data_Day10_Test.txt", "r").read().splitlines()
matrix = [[int(char) for char in row] for row in matrix]
# print(matrix)
# print(len(matrix))
# print(len(matrix[0]))

# Create graph from matrix
graph, starts, ends = createGraphFromMatrix(matrix)
# print(starts)
# print(ends)

reachable_counts = {}
for start in starts:
    reachable_counts[start] = countReachableEndpoints(graph, start)

print(reachable_counts)

# total_paths = 0
# for start in starts:
#     print(start)
#     x_low_bound, x_upper_bound = max(0, start[0] - 9), min(start[0] + 9, len(matrix[0]))
#     y_low_bound, y_upper_bound = max(0, start[1] - 9), min(start[1] + 9, len(matrix))
#     for end in ends:
#         print(end)
#         total_paths += countPaths(graph, start, end)
#     print(total_paths)

# print(total_paths)

# Draw the graph
# import matplotlib.pyplot as plt
# pos = {(x, y): (y, -x) for x, y in graph.nodes()}
# nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=200, font_size=15)
# plt.show()

