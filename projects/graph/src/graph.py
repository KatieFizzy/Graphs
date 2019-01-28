"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # below: a dictionary mapping vertex labels to edges
        self.vertices = {}

    # ---- DAY 1 -------
    # below: methods to add to/build the graph

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            print(f"No {vertex} vertex found")

    def bf_traversal(self, starting_v):
        #create queue
        q = Queue()
        visited = set()
        #enqueue the starting vertex
        q.Enqueue(starting_v)
        #while the queue is not empty, 
            #dequeue a vertex from the queue 
            #mark it as visited 
            #enqueue all of it's children that have not been visited 
        pass
    def df_traversal(self, starting_v):
        #create stack
        s = Stack()
        visited = set()
        #push starting vertex
        s.Push(starting_v)
        #while the stack is not empty, 
            #pop a vertex from the stack
            #mark it as visited 
            #push all of it's children that have not been visited 
        pass
    def dft_stack():
        pass
    def dft_recursion(self, starting_v, visited=None):
        if visited is None:
            visited = set()
        #if the node has not been visited 
            #mark node as visited
            #call dft_recursion on all children 
            dft_recursion(child_v, visited)
        pass
    #day 2
    def bfs_search(self, starting_v, target_v):
        #create queue
        q = Queue()
        visited = set()
        #enqueue the starting vertex
        q.Enqueue(starting_v)
        #while the queue is not empty, 
            #dequeue a vertex from the queue 
            #mark it as visited 
            # ---*---- if node == target_node: return true
            #enqueue all of it's children that have not been visited 
        #return false 
    
        pass
    def dft_search():
        pass

