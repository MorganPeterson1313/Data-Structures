import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList 


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
    def enqueue(self, value):
        # value = self.size
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # new_queue = self.storage
        
        if self.size  > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
            
            
        else:
            return None
            
    def __len__(self):
        return self.size
        # elif self.size[0:n] == self.size:
        #     return 1 + len(self.size[n-1])
        # else:
        # #     return len(self.size[n-1])
        
        # count = self.size
        # for i in :
        #     count +=1
        # return count
        
