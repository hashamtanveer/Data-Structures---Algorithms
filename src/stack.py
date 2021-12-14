#!/usr/bin/env python
# coding: utf-8

# In[10]:




class Node:
def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node

class LinkedListStack:
def __init__(self):
    self.curr = None
    self.prev = None


def push(self, value):
    if self.prev is None:
        self.prev = Node(value, None)
        self.curr = self.prev
        return
    n = Node(value, self.curr)
    self.curr = n

    
def pop(self):
    if self.curr is None:
        return None
    out = self.curr.value
    self.curr = self.curr.next_node
    return out

    
    
    
    
# example output
s = LinkedListStack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop()) # 3
print(s.pop()) # 2
print(s.pop()) # 1
print(s.pop()) # None


# In[ ]:




