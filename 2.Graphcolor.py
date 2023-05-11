# Define the graph as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

# Define a function to color the graph
def color_graph(graph):
    # Create a dictionary to store the color assigned to each vertex
    colors = {}
    # Define a list of available colors
    available_colors = ['red', 'green', 'blue', 'yellow']
    # Loop through each vertex in the graph
    for vertex in graph:
        # Create a set of colors already assigned to adjacent vertices
        assigned_colors = set([colors.get(adjacent_vertex) for adjacent_vertex in graph[vertex] if adjacent_vertex in colors])
        # Choose the first available color that hasn't been assigned to adjacent vertices
        color = next((c for c in available_colors if c not in assigned_colors), None)
        # If no available color can be found, the graph cannot be colored
        if color is None:
            return None
        # Assign the chosen color to the vertex
        colors[vertex] = color
    # Return the color assigned to each vertex
    return colors

# Test the function with the example graph
colors = color_graph(graph)
print(colors)
