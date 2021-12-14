#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

def every_other(head):
    if head is None or head.next_node is None:
        return
    current = head
    
    while current is not None:
    
        
        if current.next_node is not None:
            second = current.next_node
            third = second.next_node

            current.next_node = third
        current = current.next_node
    
def pri(head):
    
    while head is not None:
        print(head.value)
        head = head.next_node
        
        
# head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
# head: 1 -> 2 -> 3 -> 4 -> 5 -> None
# pri(head)
# print()
#every_other(head)
# head: 1 -> 3 -> 5 -> None
# pri(head)


# In[ ]:




