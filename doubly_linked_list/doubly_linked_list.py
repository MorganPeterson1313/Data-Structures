"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create new node with value
        new_node = ListNode(value)
        #update pointer of new head ->'head'
        self.head.insert_after(new_node)
        #inserting into empty list
        if self.head is None:
            #  mark new node as head and tail
            self.head = new_node
            self.tail = new_node
        # inserrting into a list wit 1+ nodes
        else:
            # mark new node as head
            new_node = self.head
            self.head.insert_before(new_node)
            #marke new head as previous
            # new_node = self.prev
        
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #remove from empty list. if head is equal to None then implied empty
        if self.head == self.tail:
            self.head == node
            self.tail == node
        elif self.head is None:
            return node
            #self.head == None
        else:
            return self.head.delete()

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #create new node with value
        new_node = NodeList(value)
        #insert into empty list
        if self.tail is None:
            #mark ne node as head and tail
            self.head = new_node
            self.tail = new_node
        #insert with 1+ nodes in List
        else:
            self.tail = new_node
            self.tail.insert_after(new_node)
            # new_node = self.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            # self.tail.insert_before(new_node)
            return node

        elif self.head == self.tail:
            self.head == node
            self.tail == node
        else:
            return self.tail.delete()

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
