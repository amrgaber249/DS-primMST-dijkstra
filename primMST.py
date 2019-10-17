# adjacency matrix representation of the graph 
  
import sys # Library for (Infinity)
  
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        #A matrix initialized to 0's size V^2
        self.graph = [[0 for column in range(vertices)]  #Initially,The Graph is empty
                    for row in range(vertices)] 
  
    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, mstParent): 
        print("Edge \tWeight")
        #Loop on vertices number 
        for i in range(1,self.V): 
            print(mstParent[i],"-",i,"\t",self.graph[i][ mstParent[i] ] )

    def printShortest(self, distance): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node, "\t\t", distance[node])
  
    # A utility function to find the vertex with  
    # minimum key value, from the set of vertices  
    # included in MSTset to add it to the MST later 
    def minKey(self, key, mstSet): 
        # Initilaize min value 
        min = sys.maxsize #Large value Initially
        for v in range(self.V): 
            #if Weight(u,v)<v.key --> v.key=Weight(u,v)
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
        return min_index #The next vertex to examine

    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    #sptSet is meant to be the visited set
    def minDistance(self, distance, sptSet): 
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if distance[v] < min and sptSet[v] == False: 
                min = distance[v] 
                min_index = v 
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self,src): 
        min = sys.maxsize
        #Key values used to pick minimum weight edge in cut 
        key = [min] * self.V
        key[src] = 0 
        mstParent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V 
  
        mstParent[src] = -1 # First node is always the root of
  
        for j in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        mstParent[v] = u 
        self.printMST(mstParent)
  
g = Graph(5) #5 vertices
#Representaion is using Adjacency Matrix
#Matrix Size is V^2 ,in this case we have 5 vertices(0 --> 4)
#0 in matrix indicates no connecting edge
#Otherwise indicates the Weight of The Edge
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [-6, 8, 0, 0, -9],
            [0, -5, 7, 9, 0]]

#Checking no negative weigheted edges
for i in range(len(g.graph )):
        for j in range(len(g.graph [i])):
                if g.graph[i][j] < 0:
                    g.graph[i][j] *= -1

# for i in range(len(g.graph )):
#         for j in range(len(g.graph [i])):
#                 print(g.graph[i][j])
  
g.primMST(2);
print("--------")