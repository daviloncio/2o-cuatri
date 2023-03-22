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
        str_ = ''
        for elem in self:
            str_ += str(elem) + ''
            
        str_ += ''
        return str_


class Edge:
    def __init__(self, from_, to_, weight = None):
        self._from = from_
        self._to = to_
        self._weight = weight
    def endpoints(self):
        return (self._from, self._to, self._weight)
    def __str__(self) -> str:
        
        return f'({self._from},{self._to},{self._weight})'
x = Edge(1,2,3)
print(x)

class Vertex:
    def __init__(self, vertex): 
        
        self._attributes = {'key' : vertex,
        'd' : 0, # discover time DFS  #supongo que modificaremos estos valores a la hora de hacer el set_attribute para cambiar el color.
        'f' : 0, # finalization DFS
        'degree' : 0, # vertex degree
        'color' : 'WHITE', # to mark nodes
        'parent' : None } # to the dfs-tree+
        self._adyacents = list()
    def adyacent(self,vertex):
        self._adyacents.append(vertex)
    def get_attribute(self, name):
        '''Returns the attribute name of the vertex
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys():
            return self._attributes[name]
        raise TypeError("There is not such attribute")

    def set_attribute(self, name, value):
        '''Set the attribute name of the vertex to value
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys():
            self._attributes[name] = value 
        else:
            raise TypeError("There is not such attribute")
    def get_adyacents(self):  #SUPONGO QUE ESTE MÉTODO TAMBIÉN HABRÁ QUE QUITARLO
        '''Returns a geneartor over the outcoming adyacent vertices'''
        for element in self._adyacents:
            yield element
    def __str__(self):
        v = ' [' + str(self._attributes['key']) + ','
        v += ' atributos: ' + str(self._attributes )+ '] '
        return v
        
class Graph:
    '''Representation of a simple graph using an adjacency list'''
    def __init__(self):
        '''Create an empty directed graph.'''
        self._vertices_count = 0
        self._edges_count = 0
        self._vertices = dict() # Dictionary of vertices
        self._adyacents = dict() # Adyacency list

        
    def add_vertex(self, vertex:str):
        '''Add a node with the given label to the graph.
        Raise a TypeError exception if the vertex already exists
        '''
        if vertex in self._vertices:
            raise TypeError("Vertex already in the graph")
        else:
            self._vertices[vertex] = Vertex(vertex)
            self._vertices_count += 1

    def add_edge_from_to(self, v_from, v_to:str, weight = None):
        if v_from in self._vertices and v_to in self._vertices:
            if v_from in self._adyacents:
                self._adyacents[v_from].add_last(Edge(v_from,v_to,weight))
                self._vertices[v_from].adyacent(v_to)
            else:
                self._adyacents[v_from]=LinkedList()
                self._adyacents[v_from].add_last(Edge(v_from,v_to,weight))
                self._vertices[v_from].adyacent(v_to)
            self._edges_count += 1
            self._vertices[v_from].set_attribute("degree",(self._vertices[v_from].get_attribute("degree")+1))
                               
        else:
            raise TypeError("There is no such vertex")
    def vertices(self):
        '''Return an iterator over the graph vertices.'''
        for vertice in self._vertices():
            yield vertice   
    def neighbors(self, v):
        '''Returns a genearator over the outgoing edges of the vertex v'''
        for vertice in self._vertices[v].get_adyacents():  #puedo usar directamente la función iter, pero esto viene a ser lo mismo
            yield (vertice) #si quitamos str devolverá el objeto
                
#cuestión del profe:devería volver el objeto vértice en si o solo el nombre del vertice?
#al parecer, nos será util para el futuro devolver el objeto, es una cuestion que quiere que tratemos
    def vertices_count(self):
        '''Returns the number of vertices in the graph'''
        return self._vertices_count
    def edges_count(self):
        '''Returns the number of edges in the graph'''
        return self._edges_count
    def get_vertices_attribute(self, name):  
        '''name es un parámetro que debe ser un atributo del diccionario que cada vértice tiene.
        devuelve un diccinario de nombres de vértices(clave) y el atributo que queramos(valor)
        '''
        dic = {}
        for nombres_vertices in self._vertices:
            objeto_vertice = self._vertices[nombres_vertices]
            dic[nombres_vertices] = objeto_vertice._attributes[name]
        return dic

            
    def set_vertices_attribute(self, name, value = 'WHITE'):  #creo que name solo puede ser key,degree,color o parent
        '''Set name attribute of vertices to a value
        '''   
        for nombres_vertices in self._vertices:
            self._vertices[nombres_vertices].set_attribute(name,value)
            
            
    def get_vertex_attribute(self, v, name):
        '''Returns the attribute of the vertex v
        Raise TypeError exception if there is no such vertex
        '''
        return self._vertices[v].get_attribute(name)

        
    def set_vertex_attribute(self, v, name, value):
        '''
        Set name attributes of a vertex to a value
        Returns the attribute of the vertex v
        '''
        if v in self._vertices:
            self._vertices[v].set_attribute(name,value)

        
    def __str__(self): #cambiar
        '''Returns the string representation of the graph'''
        h='{'
        for vertex in self._vertices.keys():
            h += f'[{vertex}, adj:{str(self._adyacents[vertex])}]'
        h+= '}'
        return h

        





if __name__ == '__main__':
    G = Graph()


    for i in range(1, 4):
        G.add_vertex(i)
    # add edges
    G.add_edge_from_to(1, 2, 10)
    G.add_edge_from_to(1, 3, 5)
    G.add_edge_from_to(2, 3, 6)
    G.add_edge_from_to(3, 2, 1)
    print('Total edges in the graph:', G.edges_count())
    print('Total vertices in the graph:', G.vertices_count())
    print('\nPrint graph:\n', G)
    atr = 'degree'
    print(f'\n Attribute {atr} of vertices:\n {G.get_vertices_attribute(atr)}')


        
#10.3: Busqueda de anchura
from stackarray import Stack

def DFS_iter(G: Graph,vertex:int):
    G.set_vertices_attribute("color","WHITE")
    s = Stack()
    s.push(vertex)
    while s.is_empty() == False:
        v = s.pop()
        if G.get_vertex_attribute(v,"color") == "WHITE":
            G.set_vertex_attribute(v,"color","black")

            for w in G.neighbors(v):
                if G.get_vertex_attribute(w,"color")== "WHITE":
                    G.set_vertex_attribute(w,"parent",v)
                    s.push(w)
                    
                    
#para comprobar que la siguiente función de definir es correcta,
#añadimos un cuarto vértice, que será vecino de 3.
G.add_vertex(4)
G.add_edge_from_to(3, 4, 6)  
G.add_vertex(5)
G.add_edge_from_to(2, 5, 6) 
def path_from_to(G:Graph(), v_from, v_to, f):
    """Return a path from v_from to v_to after traverse the graph with
    the procedure f
    
    >>> path_from_to(G,1,5,DFS_iter)
    empezamos desde 1, y hacemos el siguiente recorrido:
    de 1 a 3
    de 3 a 2
    de 2 a 5
    >>> path_from_to('not_a_graph',1,5,DFS_iter)
    Traceback (most recent call last):
      File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\lib\doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.path_from_to[1]>", line 1, in <module>
        path_from_to('not_a_graph',1,5,DFS_iter)
      File "c:/Users/juanj/OneDrive/Documentos/2� cuatri/repositorio1/Linked bueno.py", line 313, in path_from_to
        raise KeyError("There is no such graph")
    KeyError: 'There is no such graph'
    
    >>> path_from_to(G,'hola',5,DFS_iter)
    Traceback (most recent call last):
      File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\lib\doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest __main__.path_from_to[2]>", line 1, in <module>
        path_from_to(G,'hola',5,DFS_iter)
      File "c:/Users/juanj/OneDrive/Documentos/2� cuatri/repositorio1/Linked bueno.py", line 329, in path_from_to
        raise KeyError("Uno de los vertices introducidos no esta presente en el grafo.")
    KeyError: 'Uno de los vertices introducidos no esta presente en el grafo.'
    """
    if type (G) != Graph:
        raise KeyError("There is no such graph")    
    elif v_from not in G._vertices.keys() or v_from not in G._vertices.keys():
        raise KeyError("Uno de los vertices introducidos no esta presente en el grafo.")
    
    f(G,v_from)
    
    padre_punto = G.get_vertex_attribute(v_to,'parent')
    
    if padre_punto == None:
        print(f'empezamos desde {v_from}, y hacemos el siguiente recorrido:')
    else:
        path_from_to(G,v_from,padre_punto,DFS_iter)
        print(f'de {padre_punto} a {v_to}')




path_from_to(G,1,5,DFS_iter)

if __name__ == "__main__":
    import doctest
    doctest.testmod()