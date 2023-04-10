        
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
        '''con esta función accedemos al contenido de las listas enlazadas 
        introducidas como parámetros, vaciándolas para luego devolver la lista enlazada principal con las cifras del
        resultado en orden inverso'''

        sum_extra=0
        while l1.is_empty()==False or l2.is_empty()==False:
            try:
                num1 = l1.delete_first()
            except:
                num1 = 0
            try:
                num2 = l2.delete_first()
            except:
                num2 = 0
            print(num1,num2)
            resultado_suma = num1+num2+sum_extra
            print(resultado_suma)
            if resultado_suma >= 10:
                sum_extra = 1
                resultado_suma -= 10
            else:
                sum_extra = 0
            self.add_first(resultado_suma)
        self.add_first(sum_extra)
        print(self)
            
        
        
    
    
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
    l1 = LinkedList()
    l2 = LinkedList()
    
    for i in (2,4,3):
        l1.add_last(i)
    for i in (5,6,7,9,9):
        l2.add_last(i)
            
    l.add_two_numbers(l1,l2)
    print(l)
    
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
    
    l.add_two_numbers
    
    
    
if __name__ == '__main__':
    main()        
    


