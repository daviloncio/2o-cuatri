        
class LinkedList:
    
    #--------------- nested _Node class 
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        
        __slots__ = '_data', '_next'   # streamline memory usage
        
        def __init__(self, e):
            self._data = e
            self._next = None
            
    #------- LinkedList methods  ---------------------------------------
    
    def __init__(self) :
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty (self):
        return self._size == 0
    
    def add_first (self, e):
        newest = self._Node(e)     # create new node instance storing reference to element e
        newest._next = self._head  # set new node’s next to reference the old head node
        self._head = newest        # set variablehead to reference the new node
        self._size += 1            # increment the node count
        
        # Speccial case: only one node in the list
        if self._size == 1:
            self._tail = self._head
        
    def add_last(self, e):
        if self.is_empty():
            self.add_first(e)
            return
        
        newest = self._Node(e)  # create new node instance storing reference to element e
        self._tail._next = newest  # set old last node's next to reference the newest
        self._tail = newest        # set variable tail to reference the new node
        self._size += 1            # increment the node count
        
    def delete_first(self):
        if self.is_empty():
            raise Exception('The list is empty')
        
        data = self._head._data            # capture tha data storaged at tha first node
        self._head = self._head._next      # make head point to next node (or None)
        self._size -= 1                    # decrement the node count
    
        # Special case: Empty list
        if self.is_empty():
            self._tail = None
        
        return data
    
    def delete_last (self):
        '''cost O(n)'''
        
        # Less than one node in the list
        if self._size <= 1:
            return self.delete_first()
        
        # Traverse the list to stop BEFORE the last node
        auxiliar = self._head
        while auxiliar._next._next != None: 
            auxiliar = auxiliar._next
        
        data = auxiliar._next._data    # capture tha data storaged at tha first node
        self._tail = auxiliar          # set the node referenced by auxiliar the new last
        self._tail._next = None        # set the next of the last node 
        self._size -= 1                # decremet 
        
        return data
    
    def first(self):
        if self.is_empty():
            raise Exception('The list is empty')
        return self._head._data 

    def last(self):
        if self.is_empty():
            raise Exception('The list is empty')
        return self._tail._data 
    
    def __len__(self):
        '''Return the number of elements in the list'''
        return self._size
        
    def __iter__(self):
        '''Permite que la lista enlazada sea un objeto iterable. Coste O(n)'''
        auxiliar = self._head
        while auxiliar != None:
            yield auxiliar._data
            auxiliar = auxiliar._next
    
    def __str__(self): 
        str_ = '< '
        for elem in self:
            str_ += str(elem) + ' '
            
        str_ += '>'
        return str_
    def add_two_numbers(self, l1, l2):
        
    
    
def eliminar(L:LinkedList,maximo=None):
    if L.is_empty():
        if maximo== None:
            return
        else:
            L.add_last(maximo)
            return  
    if maximo == None:
        maximo = L.delete_last()
        eliminar(L,maximo)
    if maximo > L.last():
        L.delete_last()
        eliminar(L,maximo)
    elif L.last() > maximo:
        ha_sido_maximo = maximo
        maximo = L.last()
        L.delete_last()
        eliminar(L,maximo)
        L.add_last(ha_sido_maximo)
        
    
    
def main():
    l = LinkedList()
    
    l.add_first(-21)
    l.add_first(-23)
    l.add_first(13)
    l.add_first(2)
    l.add_first(-5)
    l.add_first(32)
    l.add_first(24)
    l.add_first(12)
    l.add_first(1)
    l.add_first(0)
    l.add_first(98)
    print(l)
    eliminar(l)
    print(l)
    
    
    
if __name__ == '__main__':
    main()        
    


