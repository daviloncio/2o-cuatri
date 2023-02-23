
class Empty (Exception):
    pass

class Stack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''
    
    def __init__(self):
        self._data = []       # nonpublic list instance
    
    def push (self, item):
        '''Add elemente to the top of stack'''
        self._data.append(item)
        
    def pop (self):
        '''Remove and return the top element from the stack;
        
        Raise a Empty exception  if the stack is empty'''
        
        if self.is_empty():
            raise Empty ('The stack is empty')
            
        return self._data.pop()
    
    def is_empty(self):
        '''Return True if stack does not contain any elements.'''
        
        if len(self._data):
            return False
        else:
            return True
        
    def top(self):
        '''Return a reference to the top element of stack, 
        without removing it; 
        
        Raise Empty exception if the stack is empty'''
        
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            return self._data[-1]
         
    def __len__(self)->int:
        return len(self._data)
    
    def __str__(self)->str:
        _str = "<"
        
        if self.is_empty():
            _str += " >"
            return _str
            
        for i in range(0, len(self._data) - 1):
            _str = _str + str(self._data[i]) + ","
        
        # Last element
        _str = _str + str(self._data[-1]) + ">"
            
        return _str
    
    def __iter__(self):
        for i in range(0, len(self._data)):
            yield self._data[i]
    
def main():    
    a = Stack()
    print(f'Stack: {a}, size: {len(a)}')
    
    a.push('hello')
    a.push('bye')
    
    print(f'Stack: {a}, size: {len(a)}')
    print("Stack top:", a.top())
    
    print('Popping:', a.pop())
    print(f'Stack: {a}, size: {len(a)}')

if __name__ == '__main__':
    main()
