#!/usr/bin/env python
# coding: utf-8

# In[15]:



import math

class MinHeap:
    def __init__(self, length):
        """Creates heap array with length empty slots,
        initialized to None. Array length should never change."""
        self.heap_array = [[None, None] for i in range(length)]
        self.next = 0
        self.identifier_index = {}

    def upheap(self, i):
        while i > 0:
            if self.heap_array[i][1] >= self.heap_array[self.parent(i)][1]:
                return
            else:
                self.swap(i, self.parent(i))
                i = self.parent(i)

    def insert(self, identifier, value):
        """Takes numeric value as argument. Returns nothing.
        Inserts value into heap using upheap algorithm.
        If heap has no empty slots remaining, do nothing."""
        if value == None:
            return
        i = self.next
        if i == len(self.heap_array):
            return
        self.heap_array[i] = [identifier, value]
        self.identifier_index[identifier] = i
        self.upheap(i)
        self.next += 1

    def parent(self, i):
        return (i - 1) // 2

    def children(self, i):
        return (2*i+1, 2*i+2)

    def swap(self, a, b):
        self.identifier_index[self.heap_array[a][0]] = b
        self.identifier_index[self.heap_array[b][0]] = a
        temp = self.heap_array[b]
        self.heap_array[b] = self.heap_array[a]
        self.heap_array[a] = temp
        return

    def downheap(self, i):
        length = self.next
        child = self.children(i)
        n = 2
        while child[0] < length:
            min_value = self.heap_array[i][1]
            min_index = i
            if self.heap_array[child[0]] is None:
                return
            if self.heap_array[child[1]] is None:
                n = 1
            for j in range(n):
                if self.heap_array[child[j]][1] < min_value:
                    min_value = self.heap_array[child[j]][1]
                    min_index = child[j]
            if min_value == self.heap_array[i][1]:
                return
            self.swap(i, min_index)
            i = min_index
            child = self.children(i)

    def extract_min(self):
        """Takes no arguments. Removes and returns
        min value in heap using downheap algorithm.
        If heap is empty, return None."""
        if self.next == 0:
            return None
        min_node = self.heap_array[0]
        last = self.next - 1
        self.swap(last, 0)
        self.heap_array[last] = None
        self.next -= 1
        self.downheap(0)
        return min_node


    def get_heap_array(self):
        """Takes no arguments. Returns internal heap array
        for automated grading tests."""
        return self.heap_array
    

def dijkstra(graph, edges, source):
    """Takes an adjacency list dictionary, edge weight dictionary,
    and a source node label. Returns a dictionary mapping node labels
    to their minimum distances from the source node."""
    Dict = {}
    for node in graph.keys():
        Dict[node] = math.inf
    for val in graph.values():
        for node in val:
            Dict[node] = math.inf
    Dict[source] = 0
    h = MinHeap(len(Dict))
    for node in Dict:
        h.insert(node, Dict[node])
    for node in Dict:
        if node not in graph:
            graph[node] = []
    while h.next != 0:
        u = h.extract_min()
        h.identifier_index[u[0]] = None 
        for v in graph[u[0]]:
            if Dict[v] > Dict[u[0]] + edges[(u[0], v)]:
                Dict[v] = Dict[u[0]] + edges[(u[0], v)]
                h.heap_array[h.identifier_index[v]][1] = Dict[v] 
                h.upheap(h.identifier_index[v])
    return Dict



def shortest_path(graph, source, dest):
    edges = {}
    for key, values in graph.items():
        for value in values:
            tu = (key, value)
            edges[tu] = 1
    
    distances = dijkstra(graph, edges, source)
    return distances[dest]
            






graph = {
    "a": ["b"],
    "b": ["d"],
    "c": ["b", "e"],
    "d": ["a", "c"],
    "e": ["a"],
}




path = shortest_path(graph, "a", "e")
print(path) # should print ["a", "b", "d", "c", "e"]
path = shortest_path(graph, "c", "a")
print(path) # should print ["c", "e", "a"]

    




# In[ ]:




