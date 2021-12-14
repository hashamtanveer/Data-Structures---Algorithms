class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class HashTable:
    def __init__(self, n, hash_func):
        
        self.hash_func = hash_func
        self.n = n
        self.table = [None for i in range(n)]

    def get(self, key):
        
        i = self.hash_func(key, self.n)
        slot = self.table[i]
        
        
        while slot is not None:
            
            if slot.data[0] == key:
                
                return slot.data[1]
            
            slot = slot.next_node
        
        return None

    def insert(self, key, value):
        
        i = self.hash_func(key, self.n)
        slot = self.table[i]
        
        if slot is None:
            
            self.table[i] = Node((key, value), None)
            
            return
        
        while slot is not None:
            
            if slot.data[0] == key:
                slot.data = (key, value)
                return
            
            else:
                
                last = slot
                slot = slot.next_node
        
        slot = Node((key, value), None)
        last.next_node = slot

    def remove(self, key):
        
        i = self.hash_func(key, self.n)
        slot = self.table[i]
   
        
        last = None
        while slot is not None:
            
            if slot.data[0] == key:
                
                a = slot.data[1]
                
                if last is not None:
                    
                    last.next_node = slot.next_node
                    slot = None
                    
                else:
                  
                    self.table[i] = None
                    
                return a
            last = slot
            slot = slot.next_node
