from stackarray import Stack

class Tree:
    class Node:
        __slots__ = '_data', '_left', '_right'
        def __init__(self, element,parent = None):
            self._data = element
            self._left = None
            self._right = None
            self._parent = parent
            
    def __init__(self):
        self._root = None
        self._size = 0
    def is_empty(self):
        return self._root == None
    def inorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _inorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                _inorder(node._left,lista)
                
                lista.append(node._data)
                
                if node._right != None:
                    _inorder(node._right,lista)
                    
        _inorder(self._root,result)
        return result
        
    def preorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _preorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                lista.append(node._data)
                
                _preorder(node._left,lista)
                #si tiene nodo hijo derecho
                if node._right != None:
                    _preorder(node._right,lista)
                    
        _preorder(self._root,result)
        return result
    def postorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _postorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                _postorder(node._left,lista)
                #si tiene nodo hijo derecho
                if node._right != None:
                    _postorder(node._right,lista)
                
                lista.append(node._data)
            
        _postorder(self._root,result)
        return result
        pass
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise.
        """
        def _recurse(node, level):
        # Base case
            if node == None:
                return ''
        # General case
            s = ''
            s += _recurse(node._right, level + 1)
            s += "| " * level
            s += str(node._data) + "\n"
            s += _recurse(node._left, level + 1)
            return s
        return _recurse(self._root, 0)
    def num_nodes(self):
        def _num_nodes(node:self.Node):
            if self.is_empty():
                return 0
            else:
                return 1 + _num_nodes(node._left) + _num_nodes(node._right)
        _num_nodes(self._root)
    def mirror(self):
        def _mirror(node):
  
            if node._left == None: #no tendrá hijos
                return
            else:
                _mirror(node._left)
                if node._right != None:  #comprobación de que existe el hijo derecho

                    node._right._data,node._left._data = node._left._data,node._right._data
                    _mirror(node._right)  
                    
        _mirror(self._root) #no devolvemos nada, estamos modificando el árbol
                            #por lo que hacemos un print para comprobar y ya

    def print_path_recursive(self,item):
        '''tree tiene su propio print path como BSTree.Este es recursivo
        el caso base se da al encontrar al elemento.USA EL PARENT'''
        camino=''
        def recursive(node:self.Node,item):
            if node._data == item:
                return f'{node._data}'
            if (node._left,node._right) == (None,None):
                return None
            if node._left != None:
                busco_izq=recursive(node._left,item)
                
            if busco_izq == None and node._right != None: 
                #solo si hay hijo derecho y si no hemos encontrado por la derecha
                busco_der = recursive(node._right,item)
                
                if busco_der != None: #encontramos algo por la derecha
                    busco_der = f'{node._data}->'+busco_der   
                return busco_der #sino devolvemos None
            
            if busco_izq != None: #ha habido suerte por la izq
                busco_izq = f'{node._data}->'+busco_izq 
            return busco_izq #devolvemos None
        print(recursive(self._root,item))

class BSTree(Tree):
    """A link-based binary search tree implementation.
    Non-repeated elements
    """
    class Node:
        '''Node includes attibute parent'''
        __slots__ = '_data', '_left', '_right', '_parent'
        def __init__(self, element, parent = None):
            self._data = element
            self._left = None
            self._right = None
            self._parent = parent # Solo necesario para el borrado en ABdB
    
    def insert(self, item):
        '''Adds item to its proper place in the tree'''
        
        def _insert(node, item):
            '''Assume BSTreee is not empty'''
            if item < node._data:   #nada más llamamos a la función, la primera compraración es con el nodo raíz
                if node._left == None:
                    node._left = self.Node(item,node)
                    
                else:
                    _insert(node._left, item)
            elif item > node._data:
                if node._right == None:
                    node._right = self.Node(item,node)
                else:
                    _insert(node._right, item)
            else:
                return
            """if self.find(item) != None:
            raise Exception('ese número ya está dentro del árbol')"""
        if self.is_empty():
            self._size += 1
            self._root = self.Node(item)
        else:
            _insert(self._root,item)
            self._size += 1

    def find(self, item):
        def _find(node:self.Node,item):
            
            if node == None:
                return None
            
            if item == node._data:
                return node
            
            if (node._left,node._right) == (None,None):
                return None
            
            else:
                buscar_item = _find(node._left,item)
                if buscar_item == None:  #si yendo por la izq con la recursión no hemos encontrado lo que buscábamos
                    if node._right != None: #probamos recursión preguntando si hay un nodo hijo derecho
                        return (_find(node._right,item))
                    else:
                        return None
                else:
                    return buscar_item
                
        z=_find(self._root,item)
        return z
    def print_path(self,item):
        def _print_path(node:self.Node,item):
            if node == None:
                return 
            if node._data == item:
                s = Stack()
                
                while node._parent != None:
                    s.push(node._data)
                    node = node._parent
                s.push(node._data)
                strng = ""
                strng = strng + str(s.pop())
                
                while s.is_empty() == False:
                    strng = strng + "->" + str(s.pop())
                    
                print (strng)
            else:
                _print_path(node._right,item)
                _print_path(node._left,item)
                          
        _print_path(self._root,item)
    def _successor(self,x):
        '''si tiene hijo derecho,el sucesor será el menor del subárbol
           sino, buscará al primer hijo izquierdo por arriba y cogerá a su padre
           si nos encontramos con la raíz y no hemos dado con un hijo izq devolvemos None'''
        if x._right != None:
            buscar_min= x._right
            while buscar_min._left != None:
                buscar_min = buscar_min._left
            return buscar_min
        
        buscar_hijo_izq = x
        while buscar_hijo_izq._parent != None:
            
            if buscar_hijo_izq._parent._left == buscar_hijo_izq:
                return buscar_hijo_izq._parent
            
            buscar_hijo_izq=buscar_hijo_izq._parent
    def successor(self, item):
        x = self.find(item) # returns the node with item as data
        if x != None:
            y = self._successor(x)
        else:
            y = None
        if y != None:
            return y._data
        return None
    
    def _transplant(self, u, v):
        if u._parent == None:
            self._root = v
        elif u == u._parent._left:
            u._parent._left = v
        
        else:
            u._parent._right = v
        if v._data != None:
            v._parent = u._parent
            
'''j = BSTree()
for i in (15,6,18,3,7,17,20,2,4,13,9):
    j.insert(i)

print(j)

print(j.successor(15))'''
     
               
   

   

            
            
            
            




    
