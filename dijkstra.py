from collections import defaultdict, deque

# The defaultdict will simply create any items that you try to access (provided of course they do not exist yet).
# returns a new empty list object.


# deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of
# container as deque provides an O(1) time complexity for append and pop operations as compared to list which
# provides O(n) time complexity.


class Graph(object):
    def __init__(self):
        # create nodes as a set (no duplicates)
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    # make the forward and the backward connections equal
    def add_edge_undirected(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        # handle the negative weights
        self.distances[(from_node, to_node)] = abs(distance)
        self.distances[(to_node, from_node)] = abs(distance)

    def add_edge_directed(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = abs(distance)

# construct a dijkstra from the provided graph
def dijkstra(graph, initial):
    # to mark the elements visited in the path and get the destination
    visited = {initial: 0}
    path = defaultdict(list)
    # create a separate set to not modify the graph nodes
    nodes = set(graph.nodes)
    # keep looping on each element in the set
    while nodes:
        # reset current node
        min_node = None
        # find the least path between the node and its neighbours
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        # there is no node to go to next
        if min_node is None:
            break
        # set it for next loop
        nodes.remove(min_node)
        # get the smallest current path and store it in the visited dict as a value to the min_node
        current_weight = visited[min_node]
        # get the current weight by traversing the edges
        for edge in graph.edges[min_node]:
            try:
                # get the total weight for the smallest path
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            # found a new edge or the total weight changed
            if edge not in visited or weight < visited[edge]:
                # mark the new edge as visited, store it as a key and the weight as a value
                visited[edge] = weight
                # store the total path (edges) visited
                path[edge] = min_node
    # path contains (destination, source)
    # visted contain (destination, distance from the initial)
    return visited, path


# print the smallest distance and the path taken to get get there from source to destination
def shortest_path(graph, source, destination):
    # construct dijkstra graph to get all the connections needed
    visited, paths = dijkstra(graph, source)
    # quicker than a list in appending
    full_path = deque()
    # a temp to store the nodes in the path before reaching the final destination
    _destination = paths[destination]
    # create a deque containing the full path from source to destination
    while _destination != source:
        full_path.appendleft(_destination)
        try:
            _destination = paths[_destination]
        except:
            return 'there is no direct path (connection) between', source, destination
    # add the source and the destination in their right position in the deque
    full_path.appendleft(source)
    full_path.append(destination)
    # get the distance from the visited array and get the full path deque as a list
    return visited[destination], list(full_path)

# running example
if __name__ == '__main__':
    graph = Graph()
    vertices = ['0', '1', '2', '3', '4', '5', '6', '7']

    for node in vertices:
        graph.add_node(node)

    graph.add_edge_undirected('2', '0', 3)
    graph.add_edge_undirected('2', '1', -6)
    graph.add_edge_undirected('2', '5', 5)
    graph.add_edge_undirected('2', '4', 6)
    graph.add_edge_undirected('1', '3', 4)
    graph.add_edge_undirected('4', '2', 7)
    graph.add_edge_undirected('4', '7', 5)
    graph.add_edge_undirected('5', '3', 3)
    graph.add_edge_undirected('6', '2', 3)

    source = '2'

    # if there is no self loop
    vertices.remove(source)

    # get all the path between the source and the destinations
    for v in vertices:
        print(shortest_path(graph, source, v))

    # path between 2 points (source, destination)
    # print(shortest_path(graph, '2', '7'))
