#!/usr/bin/env python
# coding: utf-8

# In[22]:



class Node:
  def __init__(self, value, next_node):
      self.value = value
      self.next_node = next_node
      
class LinkedList: 

  def __init__(self): 
      self.value = None
      self.next_node = next_node

def reverse(head): 
      prev = None
      current = head 
      while(current is not None): 
          next = current.next_node
          current.next_node = prev 
          prev = current 
          current = next
      head = prev
      return head
  


# In[ ]:




