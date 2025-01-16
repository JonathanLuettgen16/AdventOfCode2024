import networkx as nx
file = open("Data_Day12_Test.txt", "r")
data = file.read().splitlines()
file.close()
matrix = [[char for char in sublist] for sublist in data]


def create_undirected_graph(matrix):
    G = nx.Graph()
    rows = len(matrix)
    cols = len(matrix[0])
    perim_matrix = [[0] * cols for _ in range(rows)]

    def add_edge_if_valid(x1, y1, x2, y2):
        if 0 <= x2 < rows and 0 <= y2 < cols and matrix[x1][y1] == matrix[x2][y2]:
            G.add_edge((x1, y1), (x2, y2))
        else:
            perim_matrix[x1][y1] += 1

    for i in range(rows):
        for j in range(cols):
            G.add_node((i, j))
            add_edge_if_valid(i, j, i- 1, j)  # North
            add_edge_if_valid(i, j, i + 1, j)  # South
            add_edge_if_valid(i, j, i, j - 1)  # West
            add_edge_if_valid(i, j, i, j + 1)  # East

    return G, perim_matrix


def countNodesInSections(graph):
    components = list(nx.connected_components(graph))
    section_sizes = [len(component) for component in components]
    return section_sizes, components


def countCorners(graph, nodes):
    print(nodes)
    print(graph)
    boundary_nodes = nx.node_boundary(graph, nodes)
    print(boundary_nodes)
    corners = [node for node in boundary_nodes if graph.degree[node] <= 2]
    return len(corners), len(boundary_nodes)


# print(matrix)
# Create the graph
graph, perimeter_matrix = create_undirected_graph(matrix)
# print(perimeter_matrix)

sections, components = countNodesInSections(graph)
# comp_list = [list(component) for component in components]
perimeter_list1 = []
perimeter_list2 = []
corner_count = []
for component in components:
    temp_perim = 0
    p2, corners = countCorners(graph, component)
    perimeter_list2.append(p2)
    corner_count.append(corners)
    for (i, j) in component:
        temp_perim += perimeter_matrix[i][j]
    perimeter_list1.append(temp_perim)
print(sections)
print(perimeter_list1)
print(perimeter_list2)
print(corner_count)

# cost = 0
# for area, perimeter in zip(sections, perimeter_list):
#     cost += area * perimeter
# print(cost)
#
# Draw the graph
import matplotlib.pyplot as plt

pos = {(x, y): (y, -x) for x, y in graph.nodes()}
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
plt.show()
