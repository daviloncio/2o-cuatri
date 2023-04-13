class Tree:
    class Node:
        __slots__ = '_data', '_left', '_right'
        def __init__(self, element):
            self._data = element
            self._left = None
            self._right = None
            
            
    def __init__(self):
        self._root = None
        self._size = 0
    def is_empty(self):
        return self._root == None
    def inorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        def _inorder(node:self.Node):
            if (node._left,node._right) == (None,None):
                return
                
                _inorder(node._left)
        
        
        _inorder(self._root)
    def preorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        pass
    def postorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
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
            if item == node._data:
                return node
            else:
                if node._left != None:
                    return(_find(node._left,item))
                if node._right != None:
                    return(_find(node._right,item))
                
        z=_find(self._root,item)
        return z._data
j = BSTree()
for i in (2,3,5,32,351):
    j.insert(i)
print(j.find(5))

    
