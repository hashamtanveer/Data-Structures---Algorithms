
import math

class MinHeap:
    def __init__(self, length):
        """Creates heap array with length empty slots,
        initialized to None. Array length should never change."""
        self.length = length 
        self.heap_array = [None]*self.length
        self.avail_slots = length
        self.slots_filled = 0
    
    def get_parent_index(self, n):
        return math.floor(((n-1)/2))
        
    def get_right_child_index(self, n):
        return n*2 + 2
        
    def get_left_child_index(self, n):
        return  n*2 + 1
    
    def upheap(self, node_index):
        while (node_index > 0):
            parent_index = self.get_parent_index(node_index)
                
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                return
            else:
                self.heap_array[node_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[node_index]
                node_index = parent_index
            
    
    def insert(self, value):
        """Takes numeric value as argument. Returns nothing.
        Inserts value into heap using upheap algorithm.
        If heap has no empty slots remaining, do nothing."""
        
        if value is None:
            return

        if self.avail_slots != 0: 
            node_index = self.length - self.avail_slots
            self.heap_array[node_index] = value
            self.upheap(node_index)
            self.avail_slots -= 1
            self.slots_filled += 1
 
    
    def downheap(self, node_index, last_index):
        right_child = self.get_right_child_index(node_index)
        left_child = self.get_left_child_index(node_index)
        
        if (right_child > last_index and left_child > last_index):
            return 
        
        elif (right_child <= last_index and left_child <= last_index):
                if self.heap_array[right_child] < self.heap_array[left_child]:
                    min_child = right_child
                else:
                    min_child = left_child
                    
                if self.heap_array[node_index] > self.heap_array[min_child]:
                    self.heap_array[node_index], self.heap_array[min_child] = self.heap_array[min_child], self.heap_array[node_index]
                    node_index = min_child
                else:
                    return
                    
        elif (right_child <= last_index and left_child > last_index): 
            if self.heap_array[node_index] > self.heap_array[right_child]:
                self.heap_array[node_index], self.heap_array[right_child] = self.heap_array[right_child], self.heap_array[node_index]
                node_index = right_child
            else:
                return
            
        elif (left_child <= last_index and right_child > last_index): 
            if self.heap_array[node_index] > self.heap_array[left_child]:
                self.heap_array[node_index], self.heap_array[left_child] = self.heap_array[left_child], self.heap_array[node_index]
                node_index = left_child
            else:
                return 
            
            
        self.downheap(node_index, last_index)

    def extract_min(self):
        """Takes no arguments. Removes and returns
        min value in heap using downheap algorithm.
        If heap is empty, return None."""
        
        if self.slots_filled == 0:
            return None
        else:
            root_index = 0
            last_index = self.slots_filled-1
            to_remove = self.heap_array[root_index]
            self.heap_array[root_index], self.heap_array[last_index] = self.heap_array[last_index], self.heap_array[root_index]
            self.heap_array[last_index] = None
            self.slots_filled -= 1
            last_index = self.slots_filled-1
            self.downheap(root_index, last_index)
            return to_remove
        

    def get_heap_array(self):
        """Takes no arguments. Returns internal heap array
        for automated grading tests."""
        return self.heap_array

    
length = 8
values = [18, 6, 7, -3, 44, 10, 8]

heap = MinHeap(length)
print(heap.get_heap_array()) # [None, None, None, None, None, None, None, None]

for value in values:
    heap.insert(value)
print(heap.get_heap_array()) # [-3, 6, 7, 18, 44, 10, 8, None]

print(heap.extract_min()) # -3
print(heap.get_heap_array()) # [6, 8, 7, 18, 44, 10, None, None]








